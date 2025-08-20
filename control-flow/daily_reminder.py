task = input("Enter your task for today: ")
priority = input("Enter the priority (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        reminder = f"{task} is a high priority task."
    case "medium":
        reminder = f"{task} is a medium priority task."
    case "low":
        reminder = f"{task} is a low priority task."
    case _:
        reminder = f"Task: {task} (priority not recognized)"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"

print(reminder)