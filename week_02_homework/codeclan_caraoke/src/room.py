class Room:

    def __init__ (self, name, genre, capacity):
        self.name = name
        self.genre = genre
        self.capacity = capacity
        self.attendance = []
        self.playlist = []

    def add_guest_to_list(self, guest):
        self.attendance.append(guest)

    def remove_guest_from_list(self, guest):
        self.attendance.remove(guest)

    def find_guest_in_attendance(self, list):
        for x in list:
            print(x.name)

    def add_song_to_playlist(self, song):
        if song.genre == self.genre:
            self.playlist.append(song)

    def find_song_in_list(self, list):
        for song in list:
            print(song.name)

    def guest_goes_berserk(self, guest):
        # guest_vibe = guest.berserk
        for song in self.playlist:
            if guest.favourite_song.name == song.name:
                guest.berserk = "Whoo!"
                return guest.berserk

    # Should the berserk thing be a return?




