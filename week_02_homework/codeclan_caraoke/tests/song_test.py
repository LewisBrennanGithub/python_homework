import unittest
from src.song import *


class TestSong(unittest.TestCase):

    def setUp(self):
        self.songfunk1 = Song("Can't be funked", "Funk")
        self.songfunk2 = Song("Funkless task", "Funk")
        self.songfolk1 = Song("When the folk will that be", "Folk")
        self.songfolk2 = Song("The folk you talking about", "Folk")

    def test_song__has_name(self):
        self.assertEqual("Can't be funked", self.songfunk1.name)
        self.assertEqual("The folk you talking about", self.songfolk2.name)

    def test_song__has_genre(self):
        self.assertEqual("Folk", self.songfolk2.genre)
