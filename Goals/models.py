from django.db import models

# Create your models here.
class Goals(models.Model):
	GoalID 					= models.CharField(verbose_name="GoalID", max_length=60, unique=True)
	UserID					= models.CharField(verbose_name="UserID", max_length=60, unique=True)
	Name 					= models.CharField(max_length=70,)
	Description 			= models.CharField(max_length=70,)
	created					= models.DateTimeField(verbose_name='crated', auto_now_add=True)
	DateTimeField			= models.DateTimeField(verbose_name='date', auto_now_add=True)
	is_active				= models.BooleanField(default=True)
	
	def __str__(self):
		return self.Name

