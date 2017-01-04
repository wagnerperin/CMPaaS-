from __future__ import unicode_literals

from django.db import models

# Create your models here.
 
class Map(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	question = models.CharField(max_length=200, blank=True, default='')
	description = models.TextField()
	author = models.ForeignKey('auth.User', related_name='maps')

	def __str__(self):
		return '%d - %s' % (self.id, self.title)

class Version(models.Model):
	map = models.ForeignKey(Map, related_name='versions', on_delete=models.CASCADE)
	updated = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	author = models.ForeignKey('auth.User', related_name='versions', default=1)

	def __str__(self):
		return '%d - %s - v. %d' % (self.map.id, self.map.title, self.id)
