from django.urls import path
from .views import top_five_games, bottom_five_games,games_per_category

urlpatterns = [
    path('reports/topfive', top_five_games),
    path('reports/bottomfive', bottom_five_games),
    path('reports/gamespercategory', games_per_category),
]
