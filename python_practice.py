# ============================================
# Python Practice Questions
# Solve each question below the comment block
# Run: python3 python_practice.py
# ============================================


# ------------------------------------------
# Q1: Reverse a String
# Write a function reverse_string(s) that
# returns the reversed string WITHOUT using [::-1]
#
# Example:
#   Input:  "hello"
#   Output: "olleh"
# ------------------------------------------

def reverse_string(s):
    # Write your code here
    pass

# Test Q1
print("Q1:", reverse_string("hello"))        # Expected: olleh
print("Q1:", reverse_string("python"))       # Expected: nohtyp


# ------------------------------------------
# Q2: FizzBuzz
# Print numbers from 1 to 50:
#   - Multiples of 3 -> print "Fizz"
#   - Multiples of 5 -> print "Buzz"
#   - Multiples of both 3 and 5 -> print "FizzBuzz"
#   - Otherwise -> print the number
# ------------------------------------------

def fizzbuzz():
    # Write your code here
    pass

# Test Q2
print("\nQ2 FizzBuzz:")
fizzbuzz()


# ------------------------------------------
# Q3: Find Duplicates
# Write a function that takes a list and returns
# a list of elements that appear more than once.
#
# Example:
#   Input:  [1, 2, 3, 2, 4, 5, 3, 6]
#   Output: [2, 3]
# ------------------------------------------

def find_duplicates(lst):
    # Write your code here
    pass

# Test Q3
print("\nQ3:", find_duplicates([1, 2, 3, 2, 4, 5, 3, 6]))   # Expected: [2, 3]
print("Q3:", find_duplicates([10, 20, 30]))                   # Expected: []


# ------------------------------------------
# Q4: Count Vowels and Consonants
# Write a function that takes a string and returns
# a dictionary with vowel and consonant counts.
# Ignore spaces and special characters.
#
# Example:
#   Input:  "Hello World"
#   Output: {"vowels": 3, "consonants": 7}
# ------------------------------------------

def count_vowels_consonants(s):
    # Write your code here
    pass

# Test Q4
print("\nQ4:", count_vowels_consonants("Hello World"))     # Expected: {'vowels': 3, 'consonants': 7}
print("Q4:", count_vowels_consonants("Python"))            # Expected: {'vowels': 1, 'consonants': 5}


# ------------------------------------------
# Q5: Second Largest Number
# Write a function that returns the second largest
# number from a list. Do NOT use sort() or sorted().
#
# Example:
#   Input:  [10, 20, 4, 45, 99]
#   Output: 45
# ------------------------------------------

def second_largest(nums):
    # Write your code here
    pass

# Test Q5
print("\nQ5:", second_largest([10, 20, 4, 45, 99]))    # Expected: 45
print("Q5:", second_largest([1, 2, 3]))                 # Expected: 2
