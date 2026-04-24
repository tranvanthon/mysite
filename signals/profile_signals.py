from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from accounts.models import Profile

@receiver(post_save, sender=User, dispatch_uid="create_profile_for_new_user")
def create_user_profile(sender, instance, created, **kwargs):
    """
    Tự động tạo Profile khi tạo User mới
    """
    if created:
        Profile.objects.create(
            user=instance,
            phone='',
            email=instance.email or ''
        )


@receiver(post_save, sender=User, dispatch_uid="save_profile_when_user_updated")
def save_user_profile(sender, instance, **kwargs):
    """
    Khi User được cập nhật (edit username, email...), thì cũng save Profile
    """
    if hasattr(instance, 'profile'):   # kiểm tra xem có profile chưa
        instance.profile.save()