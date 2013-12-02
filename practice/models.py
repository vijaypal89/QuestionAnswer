from django.db import models

# Create your models here.

class Post(models.Model):
	image = models.ImageField(null=True, upload_to="image/")
	mp3 = models.FileField(null=True, upload_to="image/")
	text = models.TextField()
	def __unicode__(self):
		return self.text
