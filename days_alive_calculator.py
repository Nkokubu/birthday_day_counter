from datetime import datetime

def birthday_info():
    # Get birthday input from user
    birth_input = input("Enter your birthday (YYYY-MM-DD): ")
    
    try:
        birth_date = datetime.strptime(birth_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Get today's date
    today = datetime.today()

    # Calculate the day of the week
    day_of_week = birth_date.strftime("%A")

    # Calculate how many days you've been alive
    days_alive = (today - birth_date).days

    print(f"\nYou were born on a {day_of_week}.")
    print(f"You have been alive for {days_alive:,} days.")

if __name__ == "__main__":
    birthday_info()
