from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class CustomManager(BaseUserManager):
    def _create_user(self, phone_number, first_name, last_name, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone_number:
            raise ValueError("Phone number not given")
        if not first_name:
            raise ValueError("First name not given")
        if not last_name:
            raise ValueError("Last name not given")
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            **extra_fields
        )
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, first_name, last_name, password, **extra_fields)

    def create_superuser(self, phone_number, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, first_name, last_name, password, **extra_fields)