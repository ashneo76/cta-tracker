from django.db import models
from django.utils import timezone


class Direction(models.Model):
	direction = models.CharField(max_length = 40, null=True)

	def __unicode__(self):
		return self.direction

class Stop(models.Model):
	stop_id = models.CharField(max_length = 8, primary_key=True)
	stop_name = models.CharField(max_length = 100)
	latitude = models.FloatField()
	longitude = models.FloatField()

	def __unicode__(self):
		return self.stop_name


class Route(models.Model):
	route_id = models.CharField(max_length = 8, primary_key=True)
	route_name = models.CharField(max_length = 100)
	directions = models.ManyToManyField(Direction, blank=True, null=True)
	stops = models.ManyToManyField(Stop, blank=True, null=True, through='StopToRoute')

	def __unicode__(self):
		return self.route_name


class Vehicle(models.Model):
	pass
	
	
class StopToRoute(models.Model):
	route = models.ForeignKey(Route)
	stop = models.ForeignKey(Stop)
	direction = models.ForeignKey(Direction)