from django.db import models
from django.db.models import CASCADE

class Images(models.Model):
    image_url = models.ImageField()
    player = models.ForeignKey("Player", on_delete=CASCADE)
    game = models.ForeignKey("Game", on_delete=CASCADE)
