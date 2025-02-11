## Python: Try-Except Practice

### Overview

In this project, you'll learn how to use the `try-except` block to catch and handle exceptions that might pop up when you run your code.

A `try-except` block can help keep your script from crashing when the user enters incorrect or unexpected input.

### Coding

- Complete the practice scripts below
- Use comments to label each part in your `main.py` file

#### Part 1: Doing Addition
One common problem when prompting users to enter numbers occurs when people input text instead of numbers. When you try to convert the text input to an **integer**, Python will **throw** (generate) a `ValueError`.

Write a script that prompts the user to enter two **integers** so Python can calculate the sum of the two numbers.

For this script, write two `while` loops that both use the keyword `break` to quit the loop.
- The first loop will prompt the user to enter the first number or -999 to quit
- The second loop will prompt the user to enter another number or -999 to quit

### Sample Code
```python
# Loop prompts the user to enter a valid integer or -999 to quit the loop
while True:
    try:
        num1 = int(input(f"Enter a number or -999 to quit:\n"))
        break
    except ValueError:
        print("Sorry, I really needed a number.")
```

- Outside your loops (at the bottom of your script), print a message that displays both numbers and the sum.


#### Part 2: Invalid List Element

- Start by creating an empty Python list named `my_scores`
- Define a CONSTANT named `EXIT_CODE` and assign it the value -999

- Write a `while` loop that contains a `try-except` block
 
```python
while True:
    try:
        # Replace the placeholder value pass with actual code
        pass
    except ValueError:
        # Replace the placeholder value pass with actual code
        pass
```

- In the `try` block:
  - Prompt the user to enter an integer OR to enter -999 to quit the loop
  - `if` the user's input matches the `EXIT_CODE`, `break` out of the loop
  - Append the user's input to the list
  - Tell the user what input was just added to the list
  - Print the current version of the list
  - HINT: You can combine both outputs in one f-string!
 
- Write an `except` block that handles a `ValueError`
  - In the `except` block, print a message informing the user they entered invalid input and need to enter an integer
 
- Outside the `while` loop, use an f-string to print the final list of scores 
   
#### Part 3: Invalid Index

- Start by creating a list named `my_nums` and filling it with the numbers 10, 20, 30, 40, 50 and 60
- Similar to the second script above, write a `while` loop that contains a `try-except` block

- In your `try` block:
  - prompt the user to enter an integer between 0 and 5
  - How could you use the `len()` function to help Python display **5** (the index number of the last list item)?
  - write an `if-else` statement that:
    - checks if the index number the user entered is greater than or equal to zero **AND** less than the length of the list
    - Reminder: If the `if` statement is true:
      - print the item at that index
      - `break` out of the `while` loop
    - Otherwise, tell the user to enter an index number between 0 and 5 only
      - Again, how could you use the `len()` function to help Python display **5** (the index number of the last list item)?
- Write an `except` block that handles a `ValueError`
    - In the `except` block, print a message that tells the user they entered invalid input and should only enter an integer
