from django.db import models
from mongoengine import Document, fields
# Create your models here.


class User(models.Model):
	message = models.CharField(max_length=200)

	def __str__(self):
		return self.message


class Blogs(Document):
   username = fields.StringField()
   password = fields.StringField()
   date = fields.DateTimeField()