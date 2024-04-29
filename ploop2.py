import random
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
moods = ["Happy", "Sad", "Energetic", "Calm"]
tod = ["Morning","Afternoon","Evening"]


for day in days:
    print(f"Mood tracker for {day}:")
    for time in tod:
        mood = random.choice(moods)
        print(f"{time}: {mood}")
