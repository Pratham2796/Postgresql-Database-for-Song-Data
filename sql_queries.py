# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
                            songplay_id SERIAL PRIMARY KEY NOT NULL, 
                            start_time TIMESTAMP, 
                            user_id INT, 
                            level text, 
                            song_id text, 
                            artist_id text, 
                            session_id INT, 
                            location text, 
                            user_agent text);
                        """)

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
                        user_id INT PRIMARY KEY NOT NULL, 
                        first_name text, 
                        last_name text, 
                        gender text, 
                        level text);
                    """)

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
                        song_id text PRIMARY KEY NOT NULL, 
                        title text, 
                        artist_id text, 
                        year INT, 
                        duration DECIMAL);
                    """)

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
                          artist_id text PRIMARY KEY NOT NULL, 
                          name text, 
                          location text, 
                          latitude DECIMAL, 
                          longitude DECIMAL);
                        """)

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
                        start_time TIMESTAMP PRIMARY KEY NOT NULL, 
                        hour INT, 
                        day INT, 
                        week INT, 
                        month INT, 
                        year INT, 
                        weekday INT);
                    """)

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (
                            start_time, 
                            user_id, 
                            level, 
                            song_id, 
                            artist_id, 
                            session_id,
                            location, 
                            user_agent
                            ) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """)

user_table_insert = ("""INSERT INTO users (
                        user_id, 
                        first_name, 
                        last_name, 
                        gender, 
                        level
                        ) 
                        VALUES (%s, %s, %s, %s, %s) 
                        ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
                    """)

song_table_insert = ("""INSERT INTO songs (
                        song_id, 
                        title, 
                        artist_id, 
                        year, 
                        duration
                        ) 
                        VALUES (%s, %s, %s, %s, %s) 
                        ON CONFLICT (song_id) DO NOTHING
                    """)

artist_table_insert = ("""INSERT INTO artists (
                          artist_id, 
                          name, 
                          location, 
                          latitude, 
                          longitude
                          ) 
                        VALUES (%s, %s, %s, %s, %s) 
                        ON CONFLICT (artist_id) DO NOTHING
""")

time_table_insert = ("""INSERT INTO time (
                        start_time, 
                        hour, 
                        day, 
                        week, 
                        month, 
                        year, 
                        weekday
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s) 
                        ON CONFLICT (start_time) DO NOTHING
                    """)

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, artist_table_drop, song_table_drop, time_table_drop, songplay_table_drop]