def make_album(artist_name, album_title, num_tracks=None):
    """Erstellt ein Wörterbuch, das Informationen über ein Musikalbum enthält."""
    album = {
        'artist': artist_name,
        'title': album_title
    }
    
    # Optionale Anzahl der Tracks hinzufügen, falls angegeben
    if num_tracks:
        album['tracks'] = num_tracks
    
    return album

# Erstellen von drei Wörterbüchern, die unterschiedliche Alben repräsentieren
album1 = make_album("Pink Floyd", "The Dark Side of the Moon")
album2 = make_album("Led Zeppelin", "IV")
album3 = make_album("Nirvana", "Nevermind", num_tracks=12)

# Ausgabe der erstellten Alben
print(album1)
print(album2)
print(album3)