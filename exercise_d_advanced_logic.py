
# Online Python - IDE, Editor, Compiler, Interpreter

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
for number in numbers: 
    if number % 2 == 0:
        print(number)
# MY OWN QUESTION - Do things in Python call automatically? My understanding of the above line of code would be that I've defined a loop but I haven't called it, yet when I run (on online-python.com) it seems to call automatically?
# MY OWN QUESTION - I would expect this to exist in the background until called by whatever means. It would seem that there would be many scenarios where it would be preferable not to have code run right away.

# 2. Print the difference between the largest and smallest value:
min_qtwo = min(numbers)
max_qtwo = max(numbers)
print(max_qtwo - min_qtwo)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
if numbers[3] == numbers[2]:
    print("Nice")
else:
    print("Bad")

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

del numbers[1:4:6:9]

print(numbers)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
