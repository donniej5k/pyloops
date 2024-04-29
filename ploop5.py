# Task 1
print("Task 1 output:")
genres = ["Jazz","Rock","Hip-hop","Classical"]
for index, genre in enumerate(genres, start=1):
    print(f"Track {index}: We are playing {genre} !")

# Task 2
print("Task 2 output:")
index = 1
stopg = "Hip-hop"

while index <= len(genres):
    genre = genres[index - 1]
    print(f"Track {index}: Is now playing {genre}")
    if genre == stopg:
        print("Hip-hop detected stopping!!")
        break
    index += 1


#Task 3
print("Task 3 output:")

genres = ["Jazz","Rock","Hip-hop","Classical"]
for index in range(len(genres)):
    genre = genres[index]
    if genre == "Classical":
        continue
    print(f"Track {index + 1}: Light show is ready for {genre}!!!")
