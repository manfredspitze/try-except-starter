### What is an Exception in Python?

**An exception in Python is an error that occurs during the execution of a program.** When an exception happens, it can disrupt the normal flow of the program.

**Think of it like this:** You're following a recipe to bake a cake. If you don't have enough flour, that's an exception. You can't continue following the recipe until you do something about the exception (such as borrow three cups of flour from your neighbor).

In Python, exceptions are handled using `try-except` blocks. 

`try-except` blocks help you write code that can gracefully handle errors and continue running even if something unexpected happens.

### `try-except` Block in Python

- A `try-except` block in Python helps you manage errors that pop up when you run your code

- You write the code you want to test inside the `try` block, and if an error occurs, Python jumps to the `except` block to handle the error instead of crashing your script
- This allows you to catch mistakes and provide the user with helpful feedback, which makes your code safer and more user-friendly
- Using a `try-except` block is a way to anticipate problems and keep your script running smoothly


### `try-except` Block Examples

```python
# Example 1
# Using try-except block to handle attempting to divide a number by zero
try:
    print(2/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

```python
# Example 2
def get_validated_input(min_length=1, max_length=10):
  """
  Prompts the user for a string input and validates its length.

  Arguments used in the function call:
    min_length: The minimum allowed length of the string.
    max_length: The maximum allowed length of the string.

  Returns:
    The validated string if valid, otherwise raises a ValueError.
  """
  while True:
    try:
      user_input = input("Enter a string: ")
      if len(user_input) < min_length:
        raise ValueError(f"Input string must be at least {min_length} characters long.")
      if len(user_input) > max_length:
        raise ValueError(f"Input string cannot exceed {max_length} characters.")
      return user_input
    except ValueError as e:
      print(f"Error: {e}")

# Calling the function that validates the input string
validated_string = get_validated_input(min_length=3, max_length=8)

if validated_string:
  print(f"Validated string: {validated_string}")
```
