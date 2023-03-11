import unittest
from src.room import *
from src.guest import *
from src.song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Clive", 50)
        self.guest2 = Guest("Burt", 20)
        self.guest3 = Guest("Barnabus", 5)
        self.guest4 = Guest("Otto", 25)
        self.songfunk1 = Song("Can't be funked", "Funk")
        self.songfunk2 = Song("Funkless task", "Funk")
        self.songfolk1 = Song("When the folk will that be", "Folk")
        self.songfolk2 = Song("The folk you talking about", "Folk")
        self.room1 = Room("Funk Bunk", "Funk", 5)
        self.room2 = Room("Folkin Hell", "Folk", 2)

    def test_room__has_name(self):
        self.assertEqual("Funk Bunk", self.room1.name)

    def test_room__has_attendance_list(self):
        self.room1.add_guest_to_list(self.guest1)
        self.room1.add_guest_to_list(self.guest2)
        self.assertEqual(2, len(self.room1.attendance))

    def test_room__can_remove_guests(self):
        self.room1.add_guest_to_list(self.guest1)
        self.room1.remove_guest_from_list(self.guest1)
        self.assertEqual(0, len(self.room1.attendance))

    def test_room__guest_list(self):
        self.room1.add_guest_to_list(self.guest1)
        self.room1.add_guest_to_list(self.guest2)
        self.room1.find_guest_in_attendance(self.room1.attendance)

    def test_room__playlist_has_songs(self):
        self.room1.add_song_to_playlist(self.songfunk1)
        self.room1.add_song_to_playlist(self.songfunk2)
        self.room1.add_song_to_playlist(self.songfolk1)
        self.assertEqual(2, len(self.room1.playlist))

    def test_room__can_display_songs_by_name(self):
        self.room1.add_song_to_playlist(self.songfunk1)
        self.room1.add_song_to_playlist(self.songfunk2)
        self.room1.find_song_in_list(self.room1.playlist)
        self.assertEqual("Can't be funked", self.room1.playlist[0].name)




 

