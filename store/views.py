from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic.base import TemplateView

from store.models import Category, Product, ProductImage, Order, OrderItem
from django.urls import reverse_lazy, reverse


class HomeView(TemplateView):
    template_name = "store/index.html"


class StaffDashboardView(TemplateView):

    template_name = "dashboard/staff_dashboarb.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Dashboarf of the staff"
        context["categories"] = Category.objects.filter(parent__isnull=True)
        return context


# Quản lý hàng hoá
class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = [
        "name",
        "icon_code",
        "image",
        "is_featured",
        "meta_title",
        "meta_description",
        "meta_keywords",
    ]

    def get_success_url(self):
        return reverse("store:category_list", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Category list"
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    success_url = reverse_lazy("store:dashboard")
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create category"
        return context
