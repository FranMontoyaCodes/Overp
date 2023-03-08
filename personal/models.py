from django.db import models

# Create your models here.
class Users(models.Model):
	UserID 					= models.CharField(verbose_name="UserID", max_length=60, unique=True)
	Username				= models.CharField(verbose_name="Username", max_length=60, unique=True)
	Email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	Password 				= models.CharField(max_length=25,)
	created					= models.DateTimeField(verbose_name='crated', auto_now_add=True)
	is_active				= models.BooleanField(default=True)
	
	def __str__(self):
		return self.UserID
