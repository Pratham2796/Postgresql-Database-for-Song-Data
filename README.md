Sparkify Postgres ETL
-Data modeling with Postgres
-Database star schema created
-ETL pipeline using Python

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

The role is to create a database schema and ETL pipeline for this analysis.

Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong

-songplay_id (INT) PRIMARY KEY: ID of each user song play
-start_time (DATE) NOT NULL: Timestamp of beggining of user activity
-user_id (INT) NOT NULL: ID of user
-level (TEXT): User level {free | paid}
-song_id (TEXT) NOT NULL: ID of Song played
-artist_id (TEXT) NOT NULL: ID of Artist of the song played
-session_id (INT): ID of the user Session
-location (TEXT): User location
-user_agent (TEXT): Agent used by user to access Sparkify platform

Dimension Tables
1.
users - users in the app
-user_id (INT) PRIMARY KEY: ID of user
-first_name (TEXT) NOT NULL: Name of user
-last_name (TEXT) NOT NULL: Last Name of user
-gender (TEXT): Gender of user {M | F}
-level (TEXT): User level {free | paid}

2.
songs - songs in music database
-song_id (TEXT) PRIMARY KEY: ID of Song
-title (TEXT) NOT NULL: Title of Song
-artist_id (TEXT) NOT NULL: ID of song Artist
-year (INT): Year of song release
-duration (FLOAT) NOT NULL: Song duration in milliseconds

3.artists - artists in music database

-artist_id (TEXT) PRIMARY KEY: ID of Artist
-name (TEXT) NOT NULL: Name of Artist
-location (TEXT): Name of Artist city
-lattitude (FLOAT): Lattitude location of artist
-longitude (FLOAT): Longitude location of artist

4.
time - timestamps of records in songplays broken down into specific units
-start_time (DATE) PRIMARY KEY: Timestamp of row
-hour (INT): Hour associated to start_time
-day (INT): Day associated to start_time
-week (INT): Week of year associated to start_time
-month (INT): Month associated to start_time
-year (INT): Year associated to start_time
-weekday (TEXT): Name of week day associated to start_time


ETL pipeline
-On the etl.py the program was start by connecting to the sparkify database, and begin by processing all songs related data.

-the tree files under /data/song_data, and for each json file encountered we send the file to a function called process_song_file.

-Here load the file as a dataframe using a pandas function called read_json().

-For each row in the dataframe we select the fields we are interested in:

song_data = [song_id, title, artist_id, year, duration]
 artist_data = [artist_id, artist_name, artist_location, artist_longitude, artist_latitude]
And finally we insert this data into their respective databases.

-Once all files from song_data are read and processed, we move on processing log_data.

- repeat step 2, but this time we send our files to function process_log_file.

- load our data as a dataframe same way as with songs data.

- select rows where page = 'NextSong' only

- convert ts column where we have our start_time as timestamp in millisencs to datetime format. We obtain the parameters we need from this date (day, hour, week, etc), and insert everythin into our time dimentional table.

- load user data into our user table

-Finally  lookup song and artist id from their tables by song name, artist name and song duration that we have on our song play data. The query used is the following:
song_select = ("""
    SELECT song_id, artists.artist_id
    FROM songs JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.duration = %s
""")
-The last step is inserting everything we need into our songplay fact table.
