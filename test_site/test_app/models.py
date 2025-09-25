from django.db import models

# Create your models here.


class HeadWord(models.Model):
    word = models.CharField(max_length=25)


class Pronunciation(models.Model):
    headword = models.ForeignKey("HeadWord", on_delete=models.CASCADE)
    pronunce = models.CharField(max_length=50)
    order = models.PositiveIntegerField(help_text="the order of priority")

    class Meta:
        ordering = ['order', ]
