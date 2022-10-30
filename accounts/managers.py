from tkinter.tix import Tree
from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):

    def  create_user( self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email is must required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user