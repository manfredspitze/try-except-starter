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
def get_user_input():
  """Prompts the user for string input and handles an empty string and a ValueError.

  Returns:
    The string entered by the user.
  """
  while True:
    try:
      user_input = input("Enter a string:\n")
      if len(user_input) == 0:  # Check for empty string using len() function
        raise ValueError("Empty input is not allowed!")
      return user_input
    except ValueError:
      print("Please do not just press the ENTER key!  Enter an actual string instead!")

if __name__ == "__main__":
  user_string = get_user_input()
  if user_string: # If the user did enter a string...
    print(f"You entered: {user_string}")
```
