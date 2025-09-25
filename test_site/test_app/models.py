from django.db import models

# Create your models here.


class HeadWord(models.Model):
    word = models.CharField(max_length=25)


class Pronunciation(models.Model):
    headword = models.ForeignKey("HeadWord", on_delete=models.CASCADE)
    pronunciation = models.CharField(max_length=50)
