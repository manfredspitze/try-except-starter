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
# Use a loop to keep asking the user to enter a price for the grocery item until
# they enter a price that is 0 or greater
while True:
    try:
        price = float(input("Enter the price of the grocery item: "))
        if price < 0:
            raise ValueError("Price cannot be negative!")
        break
    except ValueError as e:
        print(f"Invalid price: {e}")
```

```python
# Example 2
# Did the user enter an age of zero or greater?
# Was the user's input valid?  Or did they enter invalid input (such as a negative age or string input instead of a number?)
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")
```
