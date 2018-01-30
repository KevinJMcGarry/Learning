class Song(object):
    """ Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the song's creator
        duration (int): The duration of the song in seconds. Duration could be 0
    """

    def __init__(self, title, artist, duration=0):  # duration default set to 0
        self.title = title
        self.artist = artist
        self.duration = duration

class Album(object):
    """ Class to represent an Album, using its track list

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist (Artist): The artists responsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artists"
        tracks (List[Song]): A list of the songs on an album

    Methods:
        add_song: Used to add a new song to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")  # this is from the Artist class
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds a song to the track list

        Args:
            song (Song): A song to add
            position (Optional[int]: If specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary
                Otherwise, the song will be appended to the end of the list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

class Artist(object):
    """ Basic class to store artist details

    Attributes
        name (str): The name of the artist
        albums (List[Album]): A list of the albums by this artist
            This list includes only those albums in this collection, it is not
            an exhaustive list of the artist's published albums

    Methods:
        add_album: Used to add a new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Add a new album to the list

        Args:
            album (Album): Album object to add to the list
                If album is already present in the list, do not add again
        """
        # to do, add self.albums.append logic

def load_data():  # function to load artist/song data from file and create tuple data to be used
    new_artist = None
    new_album = None
    artist_list = []

    with open("./albums.txt", "r") as inputfile:
        for line in inputfile:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_filed = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)  # converted to int as it is a number
            print(artist_field, album_field, year_field, song_filed)

if __name__ == "__main__":  # only run this if the file is run as a script
    load_data()

"""
To do
start putting data into the classes flowing naturally from the data --
as each row is read, create a song object, then add it to the album
and when a new album is found in the data, the current album is stored in the artist's album list
and a new album object will be created with that current row's details
"""








