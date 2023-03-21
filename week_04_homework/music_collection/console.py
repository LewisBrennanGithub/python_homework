from models.artist import Artist
from models.album import Album

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Barry Feltz")
artist_repository.save(artist1)

artist2 = Artist("Ray Knockers")
artist_repository.save(artist2)

album1 = Album("I Feltzumthin", "Disco", artist1)
album_repository.save(album1)

album2 = Album("A Day With Ray", "Prog", artist2)
album_repository.save(album2)

result = album_repository.select_all()

for album in result:
    print(f"{album.title} is assigned to {album.artist.name}")

artist1_albums = album_repository.albums_for_artist(artist1)

print(f"{artist1.name}'s albums:")
for album in artist1_albums:
    print(f"{album.title}")

    




