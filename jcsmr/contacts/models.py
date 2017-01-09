from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    email = models.CharField(max_length = 80)
    message = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.first_name, self.email)