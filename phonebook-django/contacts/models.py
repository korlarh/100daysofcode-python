from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=50)
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    phone_work = models.CharField(max_length=14)
    phone_mobile = models.CharField(max_length=14)
    phone_home = models.CharField(max_length=14)
    email_work = models.EmailField(max_length=255)
    email_home = models.EmailField(max_length=255)
    groups = models.CharField(max_length=255)
    address = models.TextField()
    relationship = models.CharField(max_length=255)
    web_address = models.CharField(max_length=255)


