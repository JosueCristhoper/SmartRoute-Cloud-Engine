from django.db import models

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=225)
    origin_lat = models.FloatField()
    origin_long = models.FloatField()
    dest_lat = models.FloatField()
    dest_long = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name