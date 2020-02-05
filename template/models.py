from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.

CHOICES = (
	('Y','Yet To Start'),
	('I','In Progress'),
	('C','Completed'),

)

class Template(models.Model):
	title = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	class Meta:
		unique_together = ("user","title")


	# def get_absolute_url(self):

	# 	return reverse('template-detail', kwargs={'pk':self.pk})


class TempData(models.Model):
	item = models.CharField(max_length=255)
	status = models.CharField(max_length=1, choices=CHOICES)
	template = models.ForeignKey(Template, on_delete=models.CASCADE)



