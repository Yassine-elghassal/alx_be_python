# daily_reminder.py

# Prompt the user to input the task description, priority, and time sensitivity
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to process the task based on priority
match priority:
    case "high":
        # If it's high priority, add urgency if time-bound
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Please ensure it is completed today.")
    case "medium":
        # If it's medium priority, handle time-bound and non-time-bound
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task. Ensure it is done soon.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Consider completing it soon.")
    case "low":
        # For low priority tasks, handle time-bound and non-time-bound scenarios
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        # If an invalid priority is entered
        print("Invalid priority level entered. Please enter 'high', 'medium', or 'low'.")
