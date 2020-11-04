from django.db import models

# Article Model
class Article(models.Model):

	title = models.CharField(max_length=200)
	preview = models.TextField(max_length=500)
	content = models.TextField(max_length=5000)
	posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Researchpaper(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	abstract = models.TextField(max_length=1000)
	pdf_url = models.CharField(max_length=100)
	pub_date = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)

	def __str__(self):
		return self.title


class SubscribeModel(models.Model):
	sys_id = models.AutoField(primary_key=True, null=False, blank=True)
	email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
	status = models.CharField(max_length=64, null=False, blank=True)
	created_date = models.DateTimeField(null=False, blank=True)
	updated_date = models.DateTimeField(null=False, blank=True)

	def __str__(self):
		return self.email