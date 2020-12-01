from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    designer = models.CharField(max_length=35)
    year_released = models.DateField()
    number_of_players = models.IntegerField()
    time_to_play = models.IntegerField()
    age = models.IntegerField()
    categories = models.ManyToManyField("Categories", related_name="game_categories", related_query_name="game_category")
