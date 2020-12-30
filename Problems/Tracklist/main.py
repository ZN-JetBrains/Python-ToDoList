def tracklist(**kwargs):
    for track in kwargs:
        print(track)
        for album in kwargs[track]:
            print(f"ALBUM: {album} TRACK: {kwargs[track][album]}")


# tracklist(Woodkid={"The Golden Age": "Run Boy Run",
#                    "On the Other Side": "Samara"},
#           Cure={"Disintegration": "Lovesong",
#                 "Wish": "Friday I'm in love"})
