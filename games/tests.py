from django.test import TestCase

from games.models import Game


class GameTestCase(TestCase):
    def setUp(self):
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
