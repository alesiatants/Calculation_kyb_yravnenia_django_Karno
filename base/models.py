from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Equation(models.Model):
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    d = models.FloatField()
    x1 = models.TextField()
    x2 = models.TextField()
    x3 = models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.a)+","+str(self.b)+","+str(self.c)+","+str(self.d)
    def get_absolute_url(self):
         return reverse("base:main", kwargs={"koef":(self.a, self.b,self.c,self.d),"korni":(self.x1,self.x2, self.x3)})
