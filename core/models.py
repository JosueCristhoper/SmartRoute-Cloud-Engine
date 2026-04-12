import math
from django.db import models

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=225)
    origin_lat = models.FloatField()
    origin_long = models.FloatField()
    dest_lat = models.FloatField()
    dest_long = models.FloatField()
    # Añadimos el nuevo campo
    distance = models.FloatField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # Realizamos funcion para despues que guarde una Ruta Django salude
    def save(self, *args, **kwargs):
        # 1. Convertimos grados a radianes
        long1, lat1 = math.radians(self.origin_long), math.radians(self.origin_lat)
        long2, lat2 = math.radians(self.dest_long), math.radians(self.dest_lat)

        # 2. Formula de Haversine -> entiende que la tierra es una esfera y no plano
        dlong = long2 - long1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlong/2)**2
        c = 2 * math.asin(math.sqrt(a))

        # 3. Multiplicamos por el radio de la Tierra en Km (6371)
        self.distance = c * 6371

        # Logica: Ponemos nombre siempre en Mayus antes de guardar
        self.name = self.name.upper()
        super().save(*args, **kwargs)