## Python: Try-Except Practice

### Overview

In this project, you'll learn how to use the `try-except` block to catch and handle exceptions that might pop up when you run your code.

A `try-except` block can help keep your script from crashing when the user enters incorrect or unexpected input.

### Coding

- Complete the practice scripts below
- Use comments to label each script in your `main.py` file

#### Doing Addition
One common problem when prompting users to enter numbers occurs when people input text instead of numbers. When you try to convert the string input to an **integer**, you'll get a `ValueError`.

Write a script that prompts the user to enter two **integers** so Python can calculate the sum of the two numbers.

For this script, write two `while` loops that both use the keyword `break` to quit the loop.

Each loop will contain a `try-except` block that will prompt the user to enter an integer

- The first loop will prompt the user for the first number (convert the user's input to an **integer**)
- The second loop will prompt the user for a second number (convert the user's input to an **integer**)

### Sample Code
```python
# Loop until the user enters a valid integer
while True:
    try:
        num1 = int(input("Give me a number:\n"))
        break
    except ValueError:
        print("Sorry, I really needed a number!")
```


![Sample output](output.png)


#### Invalid List Element

- Start by creating an empty Python list named `my_scores`
- In your `try` block:
  - prompt the user to enter an **integer** to add to your empty list
  - Using the `int( )` function, tell Python to convert the user's input into an integer
  - Use the `append()` method to add the user's input to your list
  - Print the updated list
- As part of your `except` block:
  - catch a `ValueError` and then print a message that says:
    - *Invalid input! Please enter a valid integer!*
   
#### Invalid Index

- Start by creating a list named `my_nums` and filling it with the numbers 10, 20, 30, 40, 50 and 60
- In your `try` block:
  - prompt the user to enter an **integer** between 0 and 5 (since the list contains six items) and assign the user's input to a variable named `index`
  - use an f-string to print the item at the index the user enters
- As part of your first `except` block, catch an `IndexError` and print the message: *Index out of range! Enter an index between 0 and 5 only!*
- As part of your second `except` block, catch a `ValueError` and print the message: *Invalid input! Enter an integer only for your index number!*
