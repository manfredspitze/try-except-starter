# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age < 0:
#             raise ValueError("Age cannot be negative.")
#         break
#     except ValueError as e:
#         print(f"Invalid input: {e}")

while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")