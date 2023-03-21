from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        new_album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(new_album)
    return albums

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select(id):
    album = None
    sql  = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        selected_album = results[0]
        artist = artist_repository.select(selected_album['artist_id'])
        album = Album(selected_album['title'], selected_album['genre'], artist, selected_album['id'])
    return album

def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)

def albums_for_artist(artist):
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)
    artist_albums = []
    for row in results:
        album = Album(row['title'], row['genre'], artist, row['id'])
        artist_albums.append(album)
    return artist_albums
