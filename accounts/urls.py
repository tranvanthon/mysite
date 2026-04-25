from django.urls import path, include
from accounts import views
from accounts import views as accounts_view

urlpatterns = [
    path(
        "password_reset/",
        accounts_view.CustomPasswordResetView.as_view(),
        name="account_reset_password",
    ),
    path("login/", accounts_view.LoginCustomView.as_view(), name="account_login"),
    path("signup/", accounts_view.SignupView.as_view(), name="account_signup"),
    path("logout/", accounts_view.logout_view, name="account_logout"),
    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("profile/upload-avatar/", views.upload_avatar, name="upload_avatar"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("staff-dashboard/", views.staff_dashboard, name="staff_dashboard"),
    path("customer-dashboard/", views.customer_dashboard, name="customer_dashboard"),
    path("accounts/social/", include("allauth.socialaccount.urls")),
]
