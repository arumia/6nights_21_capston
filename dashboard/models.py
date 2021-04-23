from django.db import models

# Create your models here.
class Write(models.Model):
    item_num = models.IntegerField() #작물 번호
    age = models.IntegerField() #작물연식
    latitude = models.FloatField() #위도
    longitude = models.FloatField() #경도
    Altitude = models.FloatField() #높이(해발고도)

    def __str__(self):
        return f'[{self.pk}]{self.item_num}'