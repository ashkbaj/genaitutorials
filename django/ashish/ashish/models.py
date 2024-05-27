from django.db import models

class Movie(models.Model):
    movieid = models.AutoField(default='1001')
    name = models.CharField(max_length=100)
    release = models.IntegerField(default=0000)

    def __str__(self):
        return (f'{self.name} from {self.release}')


