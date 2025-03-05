from rest_framework import viewsets, permissions
from .serializers import TaskSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
import jwt
from rest_framework.permissions import AllowAny
import datetime
from .serializers import UserRegistrationSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.tasks.all()  # Only return tasks of logged-in user

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set the user automatically


class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Generate email confirmation token
            token = jwt.encode(
                {"user_id": user.id, "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=24)},
                settings.SECRET_KEY,
                algorithm="HS256"
            )

            # Email confirmation link
            verification_link = f"http://127.0.0.1:8000/api/verify-email/{token}/"

            # Send email
            send_mail(
                "Email Verification",
                f"Click the link to verify your account: {verification_link}",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            return Response({"message": "User created. Check email for verification link."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VerifyEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload["user_id"])

            if user.is_active:
                return Response({"message": "User already verified."}, status=status.HTTP_200_OK)

            user.is_active = True  # ✅ Activate user
            user.save()
            return Response({"message": "Email verified successfully!"}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError:
            return Response({"error": "Verification link expired."}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError:
            return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)