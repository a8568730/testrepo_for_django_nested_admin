from django.db import models

# Create your models here.


class HeadWord(models.Model):
    word = models.CharField(max_length=25)
    category = models.ManyToManyField(
        'Category',
        through='CategoryMapping',
        through_fields=('headword', 'category'),
        blank=True,
    )


class Pronunciation(models.Model):
    headword = models.ForeignKey("HeadWord", on_delete=models.CASCADE)
    pronunce = models.CharField(max_length=50)
    order = models.PositiveIntegerField(help_text="the order of priority")

    class Meta:
        ordering = ['order', ]


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class CategoryMapping(models.Model):
    headword = models.ForeignKey("HeadWord", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    order = models.PositiveIntegerField(help_text="the order of priority")

    class Meta:
        ordering = ['order', ]
        constraints = [
            models.UniqueConstraint(
                fields=["headword", "category"],
                name="unique_headword_category"
            )
        ]
