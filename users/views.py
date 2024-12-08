# users/views.py
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

class PasswordResetRequest(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            reset_token = get_random_string(32)
            user.profile.reset_token = reset_token  # Save token in the user's profile
            user.profile.save()

            reset_link = f"https://your-domain.com/reset-password/{reset_token}"
            send_mail(
                "Password Reset Request",
                f"Click the link to reset your password: {reset_link}",
                "support@your-domain.com",
                [email],
            )
            return Response({"message": "Password reset email sent."}, status=200)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)

class PasswordResetConfirm(APIView):
    def post(self, request, token):
        try:
            user_profile = UserProfile.objects.get(reset_token=token)
            user = user_profile.user
            new_password = request.data.get('password')
            user.set_password(new_password)
            user.save()
            user_profile.reset_token = None
            user_profile.save()
            return Response({"message": "Password reset successful."}, status=200)
        except UserProfile.DoesNotExist:
            return Response({"error": "Invalid token."}, status=400)
