from django.db import models




class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    Email = models.EmailField()
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return ('core/contact.html')

