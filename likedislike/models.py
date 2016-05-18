from django.db import models
from django.utils import timezone


class Rate(models.Model):
    author = models.ForeignKey('auth.User')
    comment_id = models.PositiveIntegerField(null=True, blank=True)
    rating = models.IntegerField(default=0)


    def publish(self):
        self.rating = 0
        self.save()

    def __unicode__(self):              # __str__ on Python 3
        return str(self.rating)


    def __str__(self):
        return self.rating


    class Meta:
        verbose_name_plural = "rate"


