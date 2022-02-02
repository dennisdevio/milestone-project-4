from django.db import models

class Contact(models.Model):
    """ A model to save the contact form the db """

    full_name = models.CharField(max_length=55,  blank=False)
    email = models.EmailField(max_length=254,  blank=False)
    subject = models.CharField(max_length=55, blank=False)
    message = models.CharField(blank=False, max_length=1000)

    def __str__(self):
        return self.full_name