from django.db import models

# Create your models here.


class CPE(models.Model):
    credits = models.DecimalField(decimal_places=1, max_digits=6)
    course_name = models.CharField(max_length=200)
