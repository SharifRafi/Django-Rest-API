from django.db import models

# Create your models here.
#from django.db import models

# Create your models here.
class student(models.Model):

	student_name 	   		 = models.CharField(max_length=50, null=False, blank=True)
	department               = models.CharField(max_length=50, null=False, blank=True)
	#blood_gp                = models.CharField(max_length=50, null=False, blank=True)
	#gender                  = models.CharField(max_length=25, null=False, blank=True)
	contact                  = models.CharField(max_length=25, null=False, blank=True)
	#email                   = models.CharField(max_length=50, null=False, blank=True)
	#group_number            = models.CharField(max_length=50, null=False, blank=True)
	#image_file              = models.ImageField(null =False, blank=True)

	def __str__(self):
		return self.student_name
