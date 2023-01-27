# Write a function that takes in a string of lowercase letters and an integer list of the same length. The function should shift all the letters in the string along the alphabet x number of times based on each integer in the list. If you shift 'a' once it will become 'b' and so forth. If you shift 'z' once it must wrap around to become 'a'.

# Two important points:
# 1. You must use ASCII values in some way to solve this challenge
# 2. Every letter in the string must be shifted by it's corresponding index value in the list and every integer that follows it. This is a bit tricky so I'll give an example.

# Example 1:
# Input: s = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.

# Example2:
# Input: s = "aaa", shifts = [1,2,3]
# Output: "gfd"

import string

def shifting_letters(s, shifts):
    # Initialize a variable to keep track of the total shift for each letter
    total_shift = [0] * len(s)
    total_shift[-1] = shifts[-1]
    # Loop through the shifts list in reverse order and keep track of the total shift
    for i in range(len(shifts)-2, -1, -1):
        total_shift[i] = total_shift[i+1] + shifts[i]
    # Convert the string to a list so that each letter can be shifted individually
    s = list(s)
    # Loop through the string and shift each letter by its corresponding total shift
    for i in range(len(s)):
        # Get the ASCII value of the letter
        ascii_val = ord(s[i])
        # Shift the ASCII value by the total shift and get the new letter
        shifted_ascii_val = (ascii_val - ord('a') + total_shift[i]) % 26 + ord('a')
        s[i] = chr(shifted_ascii_val)
    # Convert the list back to a string and return it
    return "".join(s)
# The function takes in a string s and a list of integers shifts.
# First, we initialize a variable total_shift that is a list of the same length as the string s. We set the last element of this list to be the last element of the shifts list.
# Next, we use a for loop to iterate through the list shifts in reverse order. Starting from the second last element, we add the value of the current element to the value of the next element and store it in the current element. This way, we get the total shift that has to be applied to each letter of the string.
# After that, we convert the string s to a list of characters so that we can shift the letters individually.
# Then, we use another for loop to iterate through the list of characters. For each character, we get its ASCII value, shift it by the corresponding total shift, and get the new letter.
# Next, we convert the list of characters back to a string and return it.