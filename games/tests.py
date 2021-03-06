import pytest

from django.test import TestCase, Client

from alocai_test.models import MediaTypes

from games.models import Game


api_base = '/api/v1/'


class GameModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Game.objects.create(name='Super Game', price=71.7, space=1073741824)
        Game.objects.create(name='Extra Game', price=100.78, space=2147483648)
        Game.objects.create(name='Avengers', price=90.2, space=3521483648)

    def test_game_best_value_non_empty(self):
        max_space = 5000000000
        # verify the case where some game records are returned
        selected_games, used_space = Game.objects.get_best_value(max_space)
        self.assertNotEqual(len(selected_games), 0)
        self.assertNotEqual(used_space, 0)
        # also verify the selected games
        self.assertEqual(selected_games[0].name, "Extra Game")
        self.assertEqual(selected_games[1].name, "Super Game")

    def test_game_best_value_empty(self):
        max_space = 0
        # verify the case where some game records are returned
        selected_games, used_space = Game.objects.get_best_value(max_space)
        self.assertEqual(len(selected_games), 0)
        self.assertEqual(used_space, 0)


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_game_create_success(client):
    test_url = api_base + 'games'
    new_game_dict = {
        "name": "GTA V",
        "price": 99.8,
        "space": 890
    }

    game_response = client.post(test_url, new_game_dict, MediaTypes.JSON)

    assert game_response.status_code == 200
    assert game_response.json()['id'] is not None


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_game_best_value_api_no_games_success(client):
    test_url = api_base + 'best_value_games'

    game_response = client.post(test_url + '?pen_drive_space=888999')

    assert game_response.status_code == 200
    assert game_response.json()['total_space'] == 0


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_game_best_value_api_success(client):
    Game.objects.create(name='Super Game', price=71.7, space=10737)

    test_url = api_base + 'best_value_games'

    game_response = client.post(test_url + '?pen_drive_space=888999')

    assert game_response.status_code == 200
    assert game_response.json()['total_space'] != 0


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_game_best_value_api_bad_request(client):
    test_url = api_base + 'best_value_games'

    game_response = client.post(test_url + '?pen_')

    assert game_response.status_code == 400
