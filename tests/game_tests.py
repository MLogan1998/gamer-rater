import json
from rest_framework import status
from rest_framework.test import APITestCase
from raterapi.models import Categories, Game, Ratings, Player
from django.contrib.auth.models import User


class GameTests(APITestCase):
    def setUp(self):
        url = "/register"
        data = {
            "username": "matt",
            "password": "Admin8*",
            "email": "matt@test.com",
            "first_name": "Matt",
            "last_name": "Logan"
        }

        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)   
        self.token = json_response["token"]      
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = User()
        user.save()

        player = Player()
        player.user = user
        player.save()

        game_category = Categories()
        game_category.category = "Board game"
        game_category.save()

        game = Game()
        game.title = "Dungeons and Dragons"
        game.number_of_players = 4
        game.time_to_play = 4
        game.age = 13
        game.designer = "Milton Bradley"
        game.year_released = "1999-12-29"
        game.description = "This is the best game of all time."
        game.save()


    def test_create_game(self):
        url = "/games"
        data = {
            "categoryId": 1,
            "title": "Clue",
            "description": "a description",
            "designer": "Milton Bradley",
            "yearReleased": "1999-12-29",
            "timeToPlay": 5,
            "numberOfPlayers": 4,
            "age": 9,
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["title"], "Clue")
        # self.assertEqual(json_response["description"], "a description")
        self.assertEqual(json_response["designer"], "Milton Bradley")
        self.assertEqual(json_response["year_released"], "1999-12-29")
        self.assertEqual(json_response["time_to_play"], 5)
        self.assertEqual(json_response["number_of_players"], 4)
        self.assertEqual(json_response["age"], 9)

    
    def test_add_game_rating(self):
        url = "/rating"
        data = {
          "rating": 2,
          "player": 1,
          "game": 1
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json_response["rating"], 2)
        self.assertEqual(json_response["player"], 1)
        self.assertEqual(json_response["game"], 1)

    
    def test_delete_game(self):
        game = Game()
        game.title = "Dungeons and Dragons"
        game.number_of_players = 4
        game.time_to_play = 4
        game.age = 13
        game.designer = "Milton Bradley"
        game.year_released = "1999-12-29"
        game.description = "This is the best game of all time."
        game.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.delete(f"/games/{game.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f"/games/{game.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
