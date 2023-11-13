from django.db import models

# Create your models here.




class Training_plan(models.Model):
     
    BASIC = 'basic'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'

    PLAN_CHOICES = [
        (BASIC, 'Basic Plan - Nrs 1000'),
        (INTERMEDIATE, 'Intermediate Plan - Nrs 2000'),
        (ADVANCED, 'Advanced Plan - Nrs 3000'),
    ]

    
    training_plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    current_weight = models.FloatField()
    target_weight_category = models.CharField(max_length=100)
    sauna = models.BooleanField(default=False)
    swimming = models.BooleanField(default=False)
    private_trainer = models.BooleanField(default=False)
    private_coaching_hours = models.PositiveIntegerField(default=0)
