from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("dashboard/", views.StaffDashboardView.as_view(), name="dashboard"),
    # Url Category
    path("category/", views.CategoryListView.as_view(), name="category_list"),
    path(
        "category/create/", views.CategoryCreateView.as_view(), name="category_create"
    ),
    path(
        "category/<slug:slug>/edit",
        views.CategoryUpdateView.as_view(),
        name="category_edit",
    ),
]
