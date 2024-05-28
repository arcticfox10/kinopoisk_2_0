from django.db import models

class Rating(models.Model):
    class Rate(models.IntegerChoices):
        ONE_STAR =1 
        TWO_STAR=2
        TREE_STAR=3
        FOUR_STAR=4
        FIVE_STAR=5
        SIX_STAR=6
        SEVEN_STAR=7
        EIGHT_STAR=8
        NINE_STAR=9
        TEN_STAR=10
    class Meta:
        ordering = ["-date"]
    name= models.CharField(max_length=30)
    text = models.TextField(blank=False)
    date=models.DateTimeField(auto_now_add=True)
    rate = models. IntegerField(choices=Rate.choices)

# Create your models here.
