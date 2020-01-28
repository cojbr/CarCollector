from django.db import models
from django.urls import reverse
from datetime import date

# cars = [
#     Car('Laser', 'Plymouth', 'Foul little speed demon.', 1987),
#     Car('Cabriolet', 'Volkswagen', 'Ecstacy on four wheels.', 1991),
#     Car('Town Car', 'Lincoln', 'An absolute boat.', 1985),
#     Car('Wrangler', 'Jeep', 'A hunk-a-junk.', 2018)
# ]

MAINTENANCE = (
    ('R', 'Running'),
    ('A', 'Available for Sale')
)

# Create your models here.
class Car(models.Model):
    make = models.TextField(max_length=100)
    model = models.TextField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

    def maintained_today(self):
        return self.maintenance_set.filter(date=date.today()).count() >= len(MAINTENANCE)

class Maintenance(models.Model):
    date = models.DateField('Vehicle last checked on')
    maintain = models.CharField('Maintenance Type',
        max_length=10,
        choices=MAINTENANCE,
        default=MAINTENANCE[0][0]
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_maintain_display()} on {self.date}"

    # change the default sort
    class Meta:
        ordering = ['-date']