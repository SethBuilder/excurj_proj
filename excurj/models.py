from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime

class City(models.Model):
	city_id = models.CharField(primary_key=True, max_length=150)
	name = models.CharField(max_length=128)
	country = models.CharField(max_length=128)
	description = models.CharField(max_length=1000, blank=True)
	city_image = models.ImageField(blank=True, upload_to='city_pictures')
	slug = models.SlugField(unique=True)

	class Meta:
		verbose_name_plural = 'Cities'

	def __str__(self):
		return self.name + ", " + self.country

	@property
	def photo_url(self):
	    if self.city_image and hasattr(self.city_image, 'url'):
	        return self.city_image.url

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name + " " + self.country)
		super(City, self).save(*args, **kwargs)


class Request(models.Model):
	"""traveler requests local to take her out upon liking her profile"""
	traveler = models.ForeignKey(User, related_name='traveler_requests')
	local = models.ForeignKey(User, related_name='local_requested')
	message = models.CharField(max_length=500)
	date = models.DateField()
	local_approval = models.BooleanField(default=True)

	def __str__(self):
		return self.traveler.first_name + " " + self.local.first_name


class RequestReference(models.Model):
	""" traveler requests local to take her out on an excursion. 
	After they have gone out they leave each other a reference"""

	#Each request gets a reference instance
	request = models.OneToOneField(Request, on_delete=models.CASCADE, primary_key=True)

	traveler_desc = models.CharField(max_length=500, blank=True)#Traveler's reference description
	local_desc = models.CharField(max_length=500, blank=True)

	traveler_fun = models.BooleanField(default=True)#Did the traveler have fun ?
	local_fun = models.BooleanField(default=True)#Did the local have fun ?

	# traveler_date = models.DateField(default=datetime.datetime.now())#When the traveler leave the reference
	# local_date = models.DateField(default=datetime.datetime.now())#When the local leave the reference

	class Meta:
		get_latest_by = "request.id"

	def __str__(self):
		return self.traveler_desc	

# class OfferReference(models.Model):
# 	""" Local offers traveler to take her out. 
# 	For ex: I'm in London and a person is coming to London soon, then I offer to take her out
# 	After they have met, they leave a reference for each other """

# 	#Each offer gets a reference instance
# 	offer = models.OneToOneField(Offer, on_delete=models.CASCADE, primary_key=True)

# 	traveler_desc = models.CharField(max_length=500, blank=True)#Traveler's reference description
# 	local_desc = models.CharField(max_length=500, blank=True)

# 	traveler_fun = models.BooleanField()#Did the traveler have fun ?
# 	local_fun = models.BooleanField()#Did the local have fun ?

# 	# traveler_date = models.DateField(default=datetime.datetime.now())#When the traveler leave the reference
# 	# local_date = models.DateField(default=datetime.datetime.now())#When the local leave the reference

# 	class Meta:
# 		get_latest_by = "request.id"

# 	def __str__(self):
# 		return self.description	



class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='profile', primary_key=True) #Each User is related to only one User Profile
	city = models.ForeignKey(City, blank=True, null=True) #Each User Profile must be related to one city.
	prof_pic = models.ImageField(blank=True, upload_to='profile_pictures')
	dob = models.DateField(blank=True, null=True)
	sex = models.CharField(max_length=10, blank=True)
	education = models.CharField(blank=True, max_length=200)
	career = models.CharField(blank=True, max_length=200)
	about_you = models.CharField(max_length=500, blank=True)
	music_movies_books = models.CharField(max_length=200, blank=True)
	friendship = models.CharField(max_length=500, blank=True)
	what_will_you_show_visitors = models.CharField(max_length=1000, blank=True)
	#to add more later

	def __str__(self):
		return self.user.first_name

class Excursion(models.Model):
	"""traveler lists his trips so local could see them and possibly offer to take him out"""
	traveler = models.ForeignKey(User, related_name='traveler_lists_excursion')
	city = models.ForeignKey(City, related_name='visited_city', blank=True, null=True) #Each excursion is connected to one City.
	message = models.CharField(max_length=500)#message to all locals of that city "Hey good people of Edinburgh!"
	date = models.DateField()

class Offer(models.Model):
	""" local offers traveler to take her out based on the trips listed by traveler """
	# traveler = models.ForeignKey(User, related_name='traveler_receives_offer')#not needed since trip already has traveler
	local = models.ForeignKey(User, related_name='local_offers_excursion')
	message = models.CharField(max_length=500)
	trip = models.ForeignKey(Excursion)
	traveler_approval = models.BooleanField(blank=True)
