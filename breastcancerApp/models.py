from django.db import models

class MedicalCenter(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255)
    accessibility = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class WalkChallenge(models.Model):
    steps = models.IntegerField(default=0)

    donation = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True,)
    
    def save(self, *args, **kwargs):
        self.donation = (self.steps // 1000) * 1  # 1$ pour chaque 1000 pas
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.steps} steps on {self.date}"
