from django.db import models
from django.utils import timezone


class BowlingAlley(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Lane(models.Model):
    bowling_alley = models.ForeignKey(BowlingAlley, on_delete=models.CASCADE, related_name='lanes')
    number = models.CharField(max_length=100)

    def __str__(self):
        return f"Lane {self.number} in {self.bowling_alley.name}"


class Reservation(models.Model):
    lane = models.ForeignKey(Lane, on_delete=models.CASCADE, related_name='reservations')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)  # Provide a default value
    user_name = models.CharField(max_length=100, null=True, blank=True)
    user_email = models.EmailField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"Reservation by {self.user_name} from {self.start_time} to {self.end_time}"

    class Meta:
        unique_together = ('lane', 'start_time', 'end_time')


