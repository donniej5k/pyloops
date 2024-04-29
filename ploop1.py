# Task 1
import random
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
moods = ["Happy", "Sad", "Energetic", "Calm"]

for day in days:
	mood = random.choice(moods)
	print(f"On {day}, I am feeling {mood}.")
