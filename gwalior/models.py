from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Complaints(models.Model):
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	username = models.CharField(max_length=128, blank=True, null=True)  #.ForeignKey(register)
	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

	age = models.IntegerField(default=0)
	address = models.CharField(max_length=1024)
	area = models.CharField(max_length=512)
	pin = models.IntegerField(default=0)
	telephone = models.BigIntegerField(blank=True, null=True, default='0')
	mobile = models.BigIntegerField()
	email = models.EmailField(blank=True, null=True)

	CIVIC = 'CA'
	EDUCATION = 'ED'
	ENVIRONMENT = 'EN'
	HOSPITAL = 'HO'
	JAIL = 'JA'
	OTHERS = 'OT'
	POLICE = 'PO'
	SERVICE = 'SE'

	TYPEOFCOMP_CHOICES = (
		(CIVIC, 'civic_amenities'),
		(EDUCATION, 'education'),
		(ENVIRONMENT, 'environment'),
		(HOSPITAL, 'hospital'),
		(JAIL, 'jail'),
		(OTHERS, 'others'),
		(POLICE, 'police'),
		(SERVICE, 'service'),
		)
	type_of_complaint = models.CharField(max_length=2,
									choices=TYPEOFCOMP_CHOICES,
									default=OTHERS)


	complaint_title = models.CharField(max_length=200)
	complaint_desc = models.TextField()

	SOLVED='SOLVED'
	UNSOLVED='NOT SOLVED'
	CON = 'UNDER CONSIDERATION'
	SOLVED_CHOICES = (
		(SOLVED, 'solved'),
		(UNSOLVED, 'unsolved'),
		(CON, 'under consideration')
		)
	solved = models.CharField(max_length=50,
							choices=SOLVED_CHOICES,
							default=UNSOLVED)

	PREFERENCE_CHOICE = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
		) 

	comment = models.TextField()
	preference = models.IntegerField(choices=PREFERENCE_CHOICE,
									default=0)

	def __unicode__(self):
		return self.type_of_complaint



		


# class UserProfile(models.Model):
# 	user = models.OneToOneField(User)
# 	#reenter_password = models.CharField(max_length=200)
	

# 	first_name = models.CharField(max_length=128)
# 	last_name = models.CharField(max_length=128)
# 	address = models.CharField(max_length=1024)
# 	area = models.CharField(max_length=512)
# 	pin = models.IntegerField(default=0)
# 	telephone = models.BigIntegerField(blank=True, null=True)
# 	mobile = models.BigIntegerField(unique=True)

# 	GRA = 'GR'
# 	POST = 'PG'
# 	VOCA = 'VO'
# 	HIGHSEC = 'HS'
# 	SECOND = 'SE'
# 	ELEMENT = 'EL'
# 	NONE = 'NO'


# 	EDUCATION_CHOICES = (
# 		(GRA, 'Graduation'),
# 		(POST, 'Post Graduation'),
# 		(VOCA, 'Vocational'),
# 		(HIGHSEC, 'Higher Secondary'),
# 		(SECOND, 'Secondary'),
# 		(ELEMENT, 'Elementary'),
# 		(NONE, 'None')
# 		)
# 	education = models.CharField(max_length=8,
# 							choices=EDUCATION_CHOICES,
# 							default=NONE)

# 	picture = models.ImageField(upload_to = 'profile_images', blank=True)

# 	def __unicode__(self):
# 		return self.user.username





	