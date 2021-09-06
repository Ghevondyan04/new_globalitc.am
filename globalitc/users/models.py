from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_freelancer = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)
    is_edcenter = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name}"


class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name}"


class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name}"


class Cooperation(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Համագործակցության նպատակ'
        verbose_name_plural = 'Համագործակցության նպատակներ'


class Institution(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Ուս․ Հաստատության տեսակ'
        verbose_name_plural = 'Ուս․ Հաստատության տեսակներ'


class EducationCenter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    cooperation = models.ForeignKey('Cooperation', on_delete=models.PROTECT, null=True)
    institution = models.ForeignKey('Institution', on_delete=models.PROTECT, null=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Activity(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Գործունեության ոլորտ'
        verbose_name_plural = 'Գործունեության ոլորտներ'


class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    cooperation = models.ForeignKey('Cooperation', on_delete=models.PROTECT, null=True)
    activity = models.ForeignKey('Activity', on_delete=models.PROTECT, null=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
