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

    with open("./albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)  # converted to int as it is a number
            print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)  # creating an Artist object
            elif new_artist.name != artist_field:
                # this would arise if we just had read new data from the file and assigned it to the new_artist variable
                # in this scenario we would store the current album in the current artist's collection
                # and then create a new Artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # we've just read a new album for the current artist
                # we need to store the current album in the artist's collection and then create a new Album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # now we want to create a new song object and add that to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # at this point, have completely read through albums text file and created objects
        # the last line read will contain an artist and an album that haven't been stored.
        # This is because the way the app is designed, is that the objects (artist, album) aren't stored in their
        # collections until a new record is read from the file. So until new data read, current data not written to
        # collection.
        #
        # For example, the current album is only added to the Artist album list when a record containing
        # a different album is read
        # So ultimately what this means is that the last set of data read won't be stored until next block of code
        # is executed
        if new_artist is not None:  # this should evaluate to True
            if new_album is not None:  # this should evaluate to True
                new_artist.add_album(new_album)  # adds current album (last one read) into artists list of albums
            artist_list.append(new_artist)  # add to global list of artists

    return artist_list


def create_checkfile(artist_list):
    """ Create a check file from the object data for comparison with the original file loaded
        Goal is to have two identical files, original and new one created from objects
    """
    with open("checkfile.txt", 'w') as checkfile:  # new file we are going to write to
        for new_artist in artist_list:
            for new_album in new_artist.albums:  # here's the problem, nothing being returned
                print("hello Kevin")
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song))
                    # print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                    #      file=checkfile)  # so new_artist.name, new_album.name, new_album.year etc.
                    # the print statement writes to the file in the format defined


if __name__ == "__main__":  # only run this if the file is run as a script
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)  # artists is what was returned from the load_data() function


"""
To do
start putting data into the classes flowing naturally from the data --
as each row is read, create a song object, then add it to the album
and when a new album is found in the data, the current album is stored in the artist's album list
and a new album object will be created with that current row's details
"""








