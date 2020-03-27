from django.db import models
from django.utils import timezone

# Create your models here.
class FlashCardFactory():
    def __init__(self):
        pass

    def createflashcard(self,title,addedby,description):
        f = FlashCard(title=title, added_by=addedby, added_on=timezone.now(),description=description)
        f.save()
        return True


class FlashCard(models.Model):
    title = models.CharField(max_length=200)
    added_on = models.DateTimeField('date published')
    added_by = models.CharField(max_length=50)
    description = models.CharField(max_length=1500)


    def addbulletpoint(self, bulletpoint):
        self.bulletpoint_set.create(point = bulletpoint)
        self.save
        return True

class BulletPoint(models.Model):
    flashcard = models.ForeignKey(FlashCard, on_delete=models.CASCADE)
    point = models.CharField(max_length=2500)
