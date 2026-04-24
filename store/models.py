from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from tools.path import get_upload_path
from django.urls import reverse
from PIL import Image
from django.core.validators import MinValueValidator
from django.conf import settings
from django.db.models import Prefetch


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self", on_delete=models.PROTECT, blank=True, related_name="children", null=True
    )
    slug = models.SlugField(unique=True, blank=True)
    # images for category
    icon_code = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to="category/", blank=True)

    # status and show
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)

    # SEO
    meta_title = models.CharField(max_length=200, blank=True, verbose_name="Meta Title")
    meta_description = models.TextField(
        max_length=500, blank=True, verbose_name="Meta Description"
    )
    meta_keywords = models.CharField(
        max_length=300, blank=True, verbose_name="Meta Keywords"
    )
    # Thống kê
    product_count = models.PositiveBigIntegerField(
        default=0, verbose_name="Count the products"
    )

    # Timestamps
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_descendants(self, include_self=False):
        """Lấy tất cả danh mục con, cháu, chắt..."""
        descendants = []
        if include_self:
            descendants.append(self)

        for child in self.children.all():
            descendants.append(child)
            descendants.extend(child.get_descendants())

        return descendants

    def get_descendants_ids(self):
        """Lay list ID cua all descendants (de fielter Product)"""
        return [cat.id for cat in self.get_descendants(include_self=True)]


    def get_grouped_products(self):
        """Lấy sản phẩm theo nhóm danh mục CON, bao gồm cả chính nó"""
        if self.children.exists():

            children = self.children.prefetch_related(
                Prefetch("products", queryset=Product.objects.filter(is_active=True))
            )

            result = []
            # Lấy sản phẩm trực tiếp từ danh mục con
            for child in children:
                products = child.products.filter(is_active=True)

                if products:
                    result.append({"category": child, "products": products})

            return result
        else:
            # Nếu không có children, lấy sản phẩm của chính nó
            products = self.products.filter(is_active=True)
            if products:
                return [
                    {
                        "category": self,
                        "products": products,
                    }
                ]

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

        ordering = ["display_order", "name"]
        indexes = [
            models.Index(fields=["name", "is_active"]),
            models.Index(fields=["parent", "is_active"]),
        ]

    # create and save slug
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} - {self.name}"
        return self.name


class Product(models.Model):
    class ColorChoice(models.TextChoices):
        BLACK = "BLACK", "Black"
        GOLD = "GOLD", "Gold"
        RED = "RED", "Red"

    # Thông tin cơ bản
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="category"
    )
    slug = models.SlugField(unique=True, blank=True)
    # Mô tả sản phẩm
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=300, blank=True)
    # Thông tin giá và tồn kho
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Import prcie", default=2.00
    )
    sku = models.CharField(max_length=100, unique=True, verbose_name="Code SKU")
    barcode = models.CharField(max_length=100, blank=True, verbose_name="Barcode", db_index=True)

    # Quản lý tồn kho
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")
    low_stock_threshold = models.PositiveIntegerField(
        default=5, verbose_name="Low inventory alert threshold"
    )
    track_stock = models.BooleanField(default=True, verbose_name="Inventory tracking")
    # Trạng thái sản phẩm
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False, verbose_name="Product is featered")
    is_bestseller = models.BooleanField(
        default=False, verbose_name="Product is bestseller"
    )

    # Thông số kỹ thuật
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Weight (kg)",
    )
    dimensions = models.CharField(
        max_length=100, blank=True, verbose_name="Demensions (width x hight x high)"
    )
    color = models.CharField(
        max_length=20,
        choices=ColorChoice.choices,
        default=ColorChoice.BLACK,
    )
    material = models.CharField(max_length=50, blank=True, verbose_name="Material")

    # SEO và phân tích

    meta_title = models.CharField(max_length=200, blank=True, verbose_name="Meta Title")
    meta_description = models.TextField(
        max_length=500, blank=True, verbose_name="Meta Description"
    )
    meta_keywords = models.CharField(
        max_length=300, blank=True, verbose_name="Meta Keywords"
    )

    # Thống kê
    view_count = models.PositiveIntegerField(default=0, verbose_name="Wiewed")
    sold_count = models.PositiveIntegerField(default=0, verbose_name="Đã bán")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date publish")
    update_at = models.DateTimeField(auto_now_add=True, verbose_name="Date update")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["name", "is_active"]),
            models.Index(fields=["category", "is_active"]),
        ]

    # Sock status
    def is_in_stock(self):
        return self.stock > 0 and self.is_active

    # Validation
    def clean(self):
        if self.price <= 0:
            raise ValidationError("Price must be greater than zero")
        if self.stock < 0:
            raise ValidationError("Stock cannot be negative")

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


# Images for product
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="images"
    )
    image = models.ImageField(upload_to=get_upload_path)
    is_main = models.BooleanField(default=False)
    order = models.PositiveIntegerField(
        default=0, db_index=True
    )  # db_indext = True Giúp dữ liệu nhanh hơn

    class Meta:
        verbose_name = "ProductImage"
        verbose_name_plural = "Images of Product"
        ordering = ["order"]
        unique_together = (
            "product",
            "order",
        )  # Khi nào gặp lỗi: Tùy chọn, tránh trùng order trong 1 product

    def __str__(self):
        return f"{self.product.name} image"

    # Chua dung den
    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

    # Tối ưu ảnh

    def save(self, *args, **kwargs):
        if self.pk:
            old = type(self).objects.get(pk=self.pk)
            if old.image == self.image:
                return super().save(*args, **kwargs)

        super().save(*args, **kwargs)

        if self.image:
            try:
                img = Image.open(self.image.path)

                if img.width > 800 or img.height > 800:
                    img.thumbnail((800, 800))

                img.save(self.image.path, optimize=True, quality=70)

            except FileNotFoundError:
                print("Image file not found, skip processing")

    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        return "/static/images/default/default.png"


class Order(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        PAID = "PAID", "Paid"
        SHIPPED = "SHIPPED", "Shipped"
        CANCELLED = "CANCELLED", "Cancelled"

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders"
    )
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def can_be_cancelled(self):
        return self.status in [
            self.Status.DRAFT,
            self.Status.PAID,
        ]

    # Thêm sản phẩm vào cart
    def add_product(self, product, quantity=1):
        item, created = self.items.get_or_create(
            product=product, defaults={"price": product.price}
        )

        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()

    # Cập nhật giỏ hàng
    def update_item(self, product, quantity=1):
        try:
            item = self.items.get(product=product)
            if quantity <= 0:
                item.delete()
            else:
                item.quantity = quantity
                item.save()

        except OrderItem.DoesNotExist:
            pass

    @property
    def get_total(self):
        return sum(item.subtotal for item in self.items.all())

    class Meta:
        ordering = ["-created_at"]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    @property
    def subtotal(self):
        return self.price * self.quantity

    def clean(self):
        if self.quantity <= 0:
            raise ValidationError("Quantity must be greater than zero")
        if not self.product.is_in_stock():
            raise ValidationError("Product is out of stock")

    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     super().save(*args, **kwargs)
