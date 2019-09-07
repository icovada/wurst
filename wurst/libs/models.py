from django.db import models

# Create your models here.

class Directory(models.Model):
    name = models.TextField()
    number = models.TextField(unique=True)
    department = models.TextField
    speeddial = models.TextField(unique=True, null=True, blank=True)

    def __str__(self):
        return('{} - {} - {}'.format(self.name, self.number, self.speeddial))