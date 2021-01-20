from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ModelViewSet 
from rest_framework.response import Response 
from rest_framework import serializers 
from raterapi.models import Game, Categories
from django.db.models import Q


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Categories
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True)

    class Meta:
        model = Game
        url = serializers.HyperlinkedIdentityField(
            view_name='game',
            lookup_field='id'
        )
        fields = ('id', 'url', 'title', 'designer', 'year_released', 'number_of_players', 'time_to_play', 'age', 'categories', 'reviews', 'pictures', 'avg_rating')
        depth = 3


class Games(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_queryset(self):
        search_text = self.request.query_params.get('q', None)
        sort_option = self.request.query_params.get('orderby', None)
        if search_text is not None:
            filterset = Game.objects.filter(
                Q(title__icontains=search_text) |
                Q(description__icontains=search_text) |
                Q(designer__icontains=search_text)
            )
            return filterset
        elif sort_option is not None:
            sortset = Game.objects.order_by(sort_option)
            return sortset
        else:
            return self.queryset
