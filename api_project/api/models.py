from django.db import models

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name