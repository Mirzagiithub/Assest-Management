from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from assetmanagement import settings
from django.contrib.auth.signals import user_logged_out
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)

    class Meta:
        managed = True
        db_table = 'login_customuser'
        verbose_name_plural = "CustomUser"

    def random_username(sender, instance, **kwargs):
        if not instance.username:
            # Query the database to find the latest username that starts with "user"
            last_user = sender.objects.filter(username__startswith='user').order_by('username').last()

            if last_user:
                # Extract the numeric part from the last username (e.g., '0001' from 'user0001')
                last_number = int(last_user.username[4:])  # Get the number after 'user'
                new_number = last_number + 1
            else:
                # Start with 1 if no usernames exist
                new_number = 1

            # Generate the new username with the incremented number, zero-padded to 4 digits
            instance.username = f'user{new_number:04d}'

    models.signals.pre_save.connect(random_username, sender=settings.AUTH_USER_MODEL)