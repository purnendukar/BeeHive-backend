from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, NotFound

from apps.base.mixins import MultiRequestValidatorMixin
from apps.user.models import User
from apps.user.serializers import (
    AuthRequestSerializer,
    UserAuthSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer,
    SignRequestSerializer,
)
from apps.user.tokens import get_user_for_password_reset_token
from apps.user.emails import SendPasswordResetEmail


# Create your views here.
class AuthViewset(MultiRequestValidatorMixin, viewsets.GenericViewSet):
    model = User
    queryset = model.objects.all()
    serializer_class = UserAuthSerializer
    request_serializer_classes = {
        "signup": SignRequestSerializer,
        "login": AuthRequestSerializer,
        "forgot_password": PasswordResetSerializer,
        "password_reset_confirm": PasswordResetConfirmSerializer,
    }

    @action(methods=["POST"], detail=False, permission_classes=[])
    def signup(self, request):
        data, context = self.request_valiator()
        user = self.model.objects.create_user(**data)
        serializer = self.get_serializer(user, context=context)
        return Response(
            serializer.data,
            status.HTTP_201_CREATED,
        )

    @action(methods=["POST"], detail=False, permission_classes=[])
    def login(self, request):
        data, context = self.request_valiator()
        user = authenticate(**data)
        if not user:
            raise AuthenticationFailed
        serializer = self.get_serializer(user, context=context)
        return Response(serializer.data)

    @action(methods=["POST"], detail=False)
    def logout(self, request):
        request.auth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        methods=["POST"],
        detail=False,
        permission_classes=[],
        url_path="forgot-password",
    )
    def forgot_password(self, request):
        data, context = self.request_valiator()

        user = User.objects.filter(email=data["email"]).first()
        if not user:
            raise NotFound

        # send_password_reset_email_task.apply_async([str(user.id)])
        reset_mail = SendPasswordResetEmail(user)
        reset_mail.send_email()

        return Response(
            {"message": "Further instructions will be sent to the email if it exists"}
        )

    @action(
        methods=["POST"],
        detail=False,
        permission_classes=[],
        url_path="password-reset-confirm",
    )
    def password_reset_confirm(self, request):
        data, context = self.request_valiator()

        # Set user password
        user = get_user_for_password_reset_token(data["token"])
        user.set_password(data["new_password"])
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
