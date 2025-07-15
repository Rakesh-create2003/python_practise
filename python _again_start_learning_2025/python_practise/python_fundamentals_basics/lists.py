#creating lists for different apps

# playlist = ["shape of you "," Naa ready" ,"Beliver","Tum Hi ho"] #spofity playlist
# movies = ["Inception", "The Dark Knight", "Interstellar", "Parasite"] # Netflix movies
# Favorite_foods=["pizza","burger","pasta","biryani"]        # Favorite foods
# recent_location=["New York","Los Angeles","Chicago","Houston"] # Recent locations


# # print("Spotify Playlist:", playlist)
# # print("Netflix Movies:", movies)
# # print("Favorite Foods:", Favorite_foods)
# # print("Recent Locations:", recent_location)


# #list methods

# # playlist.append("Blinding Lights")  # Adding a song to the playlist
# # print("Updated Spotify Playlist:", playlist)



# # playlist.insert(1,"song_rakesh")  # Inserting a song at index 1
# # print("Spotify Playlist after insertion:", playlist)  

# # playlist.remove("Beliver")  # Removing a song from the playlist
# # print("Spotify Playlist after removal:", playlist )

# # playlist.pop() # Removing the last song from the playlist
# # print("Spotify Playlist after popping last song:", playlist)

# playlist.reverse()  # Reversing the playlist    
# print("Reversed Spotify Playlist:", playlist)

# print("count:",playlist.count("shape of you"))  # Counting occurrences of a song    

#list slicing
playlist = ["shape of you "," Naa ready" ,"Beliver","Tum Hi ho"] #spofity playlist
movies = ["Inception", "The Dark Knight", "Interstellar", "Parasite"] # Netflix movies
Favorite_foods=["pizza","burger","pasta","biryani"]        # Favorite foods
recent_location=["New York","Los Angeles","Chicago","Houston"] # Recent locations

# print("top 2 songs from playlist:", playlist[0:2])  # Slicing the first two songs    

# print("last 2 movies from Netflix:", movies[-2:])  # Slicing the last two movies

#list iteration 

# for song in playlist:
#     print("Song:", song)  # Iterating through the playlist and printing each song
# for movie in movies:
#     print("Movie:", movie.upper())  # Iterating through the movies and printing each movie

# for songs in playlist :
#     print("Song:", songs.title())  # Iterating through the playlist and printing each song in title case
# for songs in playlist:
#     print("song:"+" "+"by Rakesh")


#ckecking membership in list
# print("playlist:", playlist)
# if "Beliver" in playlist:
#     print("yes, 'Beliver' is in the playlist.")
# else:
#     print("No, 'Beliver' is not in the playlist.")


    # Favorite_foods[2]="noodles"  # Changing the third favorite food to "noodles"
    # print("Updated Favorite Foods:", Favorite_foods)

# mixed_list = ["apple", 42, 3.14, True, "banana"]  # A mixed list with different data types  
# for item in mixed_list:
#     print("Item:", item)  # Iterating through the mixed list and printing each item 

recent_location= ["New York", "Los Angeles", "Chicago", "Houston"]  # Recent locations
for i,location in enumerate(recent_location):
    print(f"Location {i}: {location}")  # Iterating through the recent locations and printing each location with its index



    