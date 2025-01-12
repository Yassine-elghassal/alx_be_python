from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()  # Get the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """Calculates a future date based on user input."""
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()  # Get the current date
        future_date = current_date + timedelta(days=days_to_add)  # Add days to the current date
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    display_current_datetime()  # Display the current date and time
    calculate_future_date()     # Calculate and display the future date
