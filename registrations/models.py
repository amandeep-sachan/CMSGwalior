from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfiles(models.Model):
	user = models.OneToOneField(User)
	#reenter_password = models.CharField(max_length=200)
	

	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='None')
	age = models.IntegerField(default=0)
	address = models.CharField(max_length=1024)
	area = models.CharField(max_length=512)
	pin = models.IntegerField(default=0)
	telephone = models.BigIntegerField(blank=True, null=True)
	mobile = models.BigIntegerField(unique=True, null=True)

	GRA = 'GR'
	POST = 'PG'
	VOCA = 'VO'
	HIGHSEC = 'HS'
	SECOND = 'SE'
	ELEMENT = 'EL'
	NONE = 'NO'


	EDUCATION_CHOICES = (
		(GRA, 'Graduation'),
		(POST, 'Post Graduation'),
		(VOCA, 'Vocational'),
		(HIGHSEC, 'Higher Secondary'),
		(SECOND, 'Secondary'),
		(ELEMENT, 'Elementary'),
		(NONE, 'None')
		)
	education = models.CharField(max_length=8,
							choices=EDUCATION_CHOICES,
							default=NONE)

	picture = models.ImageField(upload_to = "profile_images/", blank=True)

	def __unicode__(self):
		return self.user.username

# def create_userprofiles_user_callback(sender, instance, **kwargs):
# 	registration, new = UserProfiles.objects.get_or_create(user=instance)
# post_save.connect(create_userprofiles_user_callback, User)

