while True:
    try:
        age = input("Enter your age:\n")  # Get input from user
        # Try to convert user's input to an integer
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative.")
        else:
            print('Thank you for entering your age as a positive number.')
            break  # Exit the loop after valid input
    except ValueError as e:
        print(f"Invalid input: {e}! Please enter a valid number!")
