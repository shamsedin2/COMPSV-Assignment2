"""
Practice Problems
Each solution includes a short justification explaining:
1. Why this data structure fits the task
2. What operations are performed and their expected runtime
"""

# Problem 1: Track unique user IDs from logins
def unique_user_ids(logins):
    # Using a set to automatically remove duplicates
    return set(logins)

"""
Justification:
A set is best because we only care about uniqueness, not order.
Insertion and membership checks in a set are O(1) on average.
"""

# Problem 2: Store student grades and look them up quickly
def store_grades(pairs):
    # pairs is a list of (student, grade)
    gradebook = {student: grade for student, grade in pairs}
    return gradebook

"""
Justification:
A dictionary allows constant-time lookups by key (student name).
Insertion and access operations are O(1) on average.
"""

# Problem 3: Process customer service tickets in the order they arrive
from collections import deque

def ticket_queue(tickets):
    q = deque()
    for t in tickets:
        q.append(t)
    # process tickets in FIFO order
    processed = []
    while q:
        processed.append(q.popleft())
    return processed

"""
Justification:
A queue (deque) is ideal for first-in, first-out processing.
Appending and popping from the left are both O(1).
"""
"""
Timed Challenge

Question:
Given a list of integers and a target value, return the indices of the two numbers that add up to the target.
Assume exactly one solution exists and the same element cannot be used twice.
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None


# Example Tests
print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
print(two_sum([3, 2, 4], 6))        # [1, 2]
print(two_sum([3, 3], 6))           # [0, 1]


"""
Reflection (Approx. 230 words)

For this timed challenge, I chose to use a dictionary (hash map) as my main data structure.
The dictionary stores numbers as keys and their indices as values, which allows me to check
in constant time whether the complement of the current number has already been seen. This
approach gives an overall runtime of O(n), which is much more efficient than a naive
double loop approach that would take O(n^2).

The 30-minute time limit definitely shaped how I approached the solution. Instead of
experimenting with multiple possible strategies, I focused quickly on the hash map method
because I knew from practice and class examples that it was the most direct and efficient
way to solve this kind of problem. I did spend a couple minutes thinking about edge cases,
like duplicate values and lists with small lengths, but I didn’t overcomplicate the solution.
The time pressure pushed me to stick with a clean and proven approach rather than exploring
alternatives.

One trade-off I made was in code readability. While the final solution is short and efficient,
I didn’t include extra comments or input validation beyond what was necessary for the task.
If I had more time, I would add more descriptive variable names and checks for invalid input.
Overall, this challenge gave me confidence that I can perform under pressure by relying on
core data structure knowledge.
"""
