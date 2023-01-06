from django.db import models
from django.utils import timezone
from house import models as core_models
# Create your models here.

class Reservation(core_models.TimeStampedModel):
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"
    STATUS_CHOICE = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICE, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()

    guest = models.ForeignKey(
        "users.User", related_name="reservation", on_delete=models.CASCADE
    )

    house = models.ForeignKey(
        "house.House", related_name="reservation", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.house} - {self.check_in}"
    
    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out
    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out
    is_finished.boolean = True

