from django.urls import path, include
from accounts import views

urlpatterns = [
    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("profile/upload-avatar/", views.upload_avatar, name="upload_avatar"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("staff-dashboard/", views.staff_dashboard, name="staff_dashboard"),
    path("customer-dashboard/", views.customer_dashboard, name="customer_dashboard"),
    path("", include("allauth.urls")),
]
