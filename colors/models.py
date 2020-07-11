from django.db import models

class Item(models.Model):
	name = models.CharField(max_length=16)

	def __str__(self):
		return self.name

class Color(models.Model):
	name = models.CharField(max_length=16)

	def __str__(self):
		return self.name

class Review(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
	color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='reviews')
	score = models.IntegerField()
