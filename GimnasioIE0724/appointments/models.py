from django.db import models
from django.contrib.auth.models import User

# Create your models here.
HOURS = [
    ('M', 'Mañana'),
    ('T', 'Tarde'),
    ('N', 'Noche'),
]

class Appointments(models.Model):
    # Si eliminamos user, se elimina todas sus citas(CASCADE), puede ser empty. 
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True) 
    #day = models.PositiveIntegerField(blank=True)
    day = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 32)], blank=True)
    month = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 13)], blank=True)
    hour = models.CharField(max_length=1, choices=HOURS) 
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True) # Cuando se crea, lo guarda

    def __str__(self):
        return str(self.day) + ' / ' + str(self.month) + ' / ' + 'en la ' + self.hour
    
    class Meta:
        ordering = ['-month'] # Ordenar por mes