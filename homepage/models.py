from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, default='No Name', blank=True, null=True)#blank og null so field can be empty
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)#auto_now_add save on create, auto_now saves on update
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email