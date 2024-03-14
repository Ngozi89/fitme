from django.db import models

# Create your models here.
class Member(models.Model):
    memb_name = models.CharField(max_length=50, null=False, blank=False)
    memb_email = models.CharField(max_length=50, null=False, blank=False)