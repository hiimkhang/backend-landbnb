from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """Time Stamped Abstract Definition"""

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True