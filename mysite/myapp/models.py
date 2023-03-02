from django.db import models
# specifying gender choices
gender_choices = (
	("male", "male"),
	("female", "female")
)

# Create your models here.
# import the standard Django Model
# from built-in library
from django.db import models

# declare a new model with a name "GeeksModel"
class intern(models.Model):

	# fields of the model
	first_name = models.CharField(max_length = 15)
	last_name= models.CharField(max_length = 15)
	email_address = models.CharField(max_length = 20)
	gender = models.CharField(max_length= 10, choices = gender_choices, default = '1')
	date_of_birth = models.DateField()

	# renames the instances of the model
	# with their title name
def __str__(self):
	return self.first_name

