"""
Author: Brent Joshua Samson
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Brent Samson"
preferred_weight_kg = 20.5
highest_reps= 20
membership_active = True


# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Brent": (30, 45, 20),
    "Joshua": (60, 45, 40),
    "Noe": (45, 35, 55),
}

# Step d: Calculate total workout minutes using a loop and add to dictionary

friends = list(workout_stats.keys())

for friend in friends:
    total = sum(workout_stats[friend])
    workout_stats[friend + "_Total"] = total


# Step e: Create a 2D nested list called workout_list

workout_list = [list(workout_stats[friend]) for friend in friends]


# Step f: Slice the workout_list

print("===Yoga & Running minutes for all friends ===")
for i, friend in enumerate(friends):
    yoga_running = workout_list[i][:2]
    print(f"    {friend}: {yoga_running}")

# Step g: Check if any friend's total >= 120
print("\n=== Activity Check ===")
for friend in friends:
    total = workout_stats[friend + "_Total"]
    if total >= 120:
        print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend

print("\n=== Friend Lookup ===")
name_input = input("Enter a friend's name to look up: ").strip()

if name_input in friends:
    yoga, running, weightlifting = workout_stats[name_input]
    total = workout_stats[name_input + "_Total"]
    print(f"\n  {name_input}'s workout breakdown:")
    print(f"    Yoga:          {yoga} min")
    print(f"    Running:       {running} min")
    print(f"    Weightlifting: {weightlifting} min")
    print(f"    Total:         {total} min")
else:
    print(f"Friend {name_input} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes

print("\n=== Workout Summary ===")
totals = {friend: workout_stats[friend + "_Total"] for friend in friends}

best_friend  = max(totals, key=totals.get)
worst_friend = min(totals, key=totals.get)

print(f"  Highest total workout minutes: {best_friend} ({totals[best_friend]} min)")
print(f"  Lowest total workout minutes:  {worst_friend} ({totals[worst_friend]} min)")
