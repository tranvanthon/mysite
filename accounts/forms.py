from django.contrib.auth.forms import (
    PasswordResetForm,
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm,
)
from django import forms

from accounts.models import CustomUser
from accounts.models import Profile
from django.core.exceptions import ValidationError

INPUT_CLASSCES = "form-control"


class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model = CustomUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {
                # 'class': INPUT_CLASSCES,
                "placeholder": "Mật khẩu mới",
                "label": "",
            }
        )


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["old_password"].widget.attrs.update(
            {
                # 'class': INPUT_CLASSCES,
                "placeholder": "Mật khẩu cũ",
                "label": "",
            }
        )
        self.fields["new_password1"].widget.attrs.update(
            {
                # 'class': INPUT_CLASSCES,
                "placeholder": "Mật khẩu mới",
                "label": "",
            }
        )

        self.fields["new_password2"].widget.attrs.update(
            {
                # 'class': INPUT_CLASSCES,
                "placeholder": "Nhập lại mật khẩu",
                "label": "",
            }
        )


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tùy chỉnh widget sau khi super().__init__ đã tạo ra các trường
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": "Email",
            }
        )
        # UserCreationForm tự sinh ra password1 và password2, bạn gọi đúng tên này:
        if "password1" in self.fields:
            self.fields["password1"].widget.attrs.update({"placeholder": "Mật khẩu"})
        if "password2" in self.fields:
            self.fields["password2"].widget.attrs.update(
                {"placeholder": "Nhập lại mật khẩu"}
            )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "username" in self.fields:
            self.fields["username"].widget.attrs.update(
                {
                    "placeholder": "Email/Tên đăng nhập",
                }
            )
        self.fields["password"].widget.attrs.update(
            {
                "placeholder": "Mật khẩu",
            }
        )
        self.error_messages = {
            "invalid_login": "Tên đăng nhập hoặc mật khẩu không chính xác. Vui lòng thử lại.",
            "inactive": "Tài khoản này đã bị vô hiệu hóa.",
        }
