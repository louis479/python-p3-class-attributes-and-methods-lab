class Song:
    count = 0
    genres = []  # Store unique genres
    artists = []  # Store unique artists
    genre_count = {}  # Store genre counts
    artist_count = {}  # Store artist counts

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)  # FIX: Pass `artist`, not `genre`
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Create song instances
song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")
song3 = Song("Hotline Bling", "Drake", "Rap")
song4 = Song("Formation", "Beyonce", "Pop")
song5 = Song("Bohemian Rhapsody", "Queen", "Rock")

# Output results
print("Total Songs:", Song.count)
print("Unique Genres:", Song.genres)
print("Unique Artists:", Song.artists)
print("Genre Count:", Song.genre_count)
print("Artist Count:", Song.artist_count)
