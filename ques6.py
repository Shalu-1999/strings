'''
Write a Python Program to form a new string made of the first 2 characters and last 2 characters from a given string.
Problem Description:
The program takes a string and forms a new string made of the first 2 characters and last 2 characters from a given string.
Problem Solution:
1. Take a string from the user and store it in a variable.
2. Initialize a count variable to 0.
3. Use a for loop to traverse through the characters in the string and increment the count variable each time.
4. Form the new string using string slicing.
5. Print the newly formed string.
6. Exit.
Sample Input:
Hello World
Sample Output:
Held
'''
def form_new_string(s):
    if len(s) < 2:
        return "The string is too short!"
    else:
        new_string = s[:2] + s[-2:]
        return new_string
input_string = input("Enter a string: ")
result = form_new_string(input_string)
print(result)
