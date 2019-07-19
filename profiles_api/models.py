from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
	"""Manager for User Profile"""
	def create_user(self,email,name,password=None):
		"""Create a new User Profile"""
		if not email:
			raise ValueError("User must have an email Address")
		email=self.normalize_email(email)
		user=self.model(email=email, name=name)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,name,password):
		"""Create and save a new superUser with given details"""
		user=self.create_user(email,name,password)
		user.is_superuser=True
		user.is_staff=True
		user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""Database model for user in the system"""
	email=models.EmailField(max_length=255, unique=True)
	name=models.CharField(max_length=255)
	is_activate=models.BooleanField(default=True)
	is_staff=models.BooleanField(default=True)

	objects=UserProfileManager()

	USERNAME_FIELD='email'
	REQUIRED_FIELD=['name']

	def get_full_name(self):
		"""Retrive full name of user"""
		return self.name
	def get_short_name(self):
		"""Retrive short name of user"""
		return self.name
	def __str__(self):
		"""Return string  representation of our user"""
		return self.email
