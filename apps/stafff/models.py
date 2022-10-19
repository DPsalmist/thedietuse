from django.db import models
from apps.home.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
	gender = (
			('Select Gender', 'Select Gender'),
			('Male','Male'),
			('Female','Female'),
		)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	headline = models.CharField(max_length=50, default='Your headline', blank=True)
	photo = models.ImageField(default='default_profile_pic.jpeg', upload_to='profile_pics', blank=True)
	timeline_picture = models.ImageField(default='img-1-1000x600.jpg', upload_to='timeline_pics/', blank=True)
	gender = models.CharField(max_length=30, choices=gender, default='Select Gender')
	staff_bio = models.CharField(max_length=200, blank=True)
	staff_id = models.CharField(max_length=100, blank=True, null=True)
	school_name = models.CharField(max_length=100, blank=True, default='School Name')
	department = models.CharField(max_length=200, blank=True)
	school_type = models.CharField(max_length=200, blank=True)
	staff_class = models.CharField(max_length=200, blank=True, default='None')
	staff_subject = models.CharField(max_length=200, blank=True)
	staff_no_of_subjects = models.IntegerField(default=0)
	bank = models.CharField(max_length=30, default='State Your Bank')
	account_no = models.CharField(max_length=30, default='Enter Account Number')
	account_name = models.CharField(max_length=30, default='Enter Account Name')
	phone_no = models.CharField(max_length=30, default='+234-08000000', blank=True)
	address = models.TextField(max_length=150, default='my address', blank=True)
	city = models.CharField(max_length=50, default='Your current city', blank=True)
	country = models.CharField(max_length=50, default='Your current country', blank=True)
	state_of_origin = models.CharField(max_length=50, default='Enter state of origin', blank=True)
	nationality = models.CharField(max_length=50, default='Nigerian', blank=True)
	religion = models.CharField(max_length=50, default='Enter religion', blank=True)

	def __str__(self): 	
		return f'{self.user.username} Profile'

	#To resize the image though the save method exist in the parent class, we'll create ours.
	#In order to override the default save, you'll have to use *args & *kwargs	
	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.photo.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.photo.path)