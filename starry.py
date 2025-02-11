"""
Part 2: Star Drawings with Nested Loops

Take a look at starry.py posted on our course website. Take some time looking through the
code, explaining how it works.
Add your explanation as in-line comments if needed.
Once you feel completely confident in your understanding of starry.py, comment out the
given loop and add in other loops which draw at least three of the following drawings (n
should be the # of rows for each of them). If you choose any of the last three, decide what
you want to do it if n is even.

References used: https://pynative.com/print-pattern-python-examples/#h-inverted-pyramid-pattern-of-numbers
Hint:
n = int(input("# rows: "))

# You are only allowed to use the following 3 print functions.
# print()
# print(" ", end="")
# print("*", end="")

# nested loops example
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

"""


# pattern 1

def print_pattern1(n):
    # Print piramid
    for i in range(n):
        # print space
        for _ in range(n - i - 1):
           print(' ', end='')
           # print piramid
        for i in range(2 * i + 1):
            print('*', end='')
        print()

#rows = int(input("Enter the number of rows for pattern 1: "))
#print_pattern1(rows)

# pattern 2
def print_pattern2(n):
    print(n)
    """ One inverted triangle """
    for i in range(n, 0, -1):
        for j in range(i):
            print( '*', end='')  # Add space
        print()


#rows = int(input("Enter the number of rows pattern 2: "))
#print_pattern2(rows)

# pattern 3

def print_pattern3(n):
    for i in range(1, n + 1):
        for j in range(i):
            print('*', end='')
        print()
    for i in range(n, 0, -1):
        for j in range(0, i - 1):
            print('*', end='')
        print()

#rows = int(input("Enter the number of rows - pattern 3: "))
#print_pattern3(rows)

# pattern 4
def print_pattern4(n):
    # inverted pyramid
    i = 0
    while i <= n - 1:
        j = 0
        while j < i:
            # display space
            print('', end=' ')
            j += 1
        k = i
        while k <= n - 1:
            print('*', end=' ')
            k += 1
        print()
        i += 1

    i = n - 2
    while i >= 0:
        j = 0
        while j < i:
            print('', end=' ')
            j += 1
        k = i
        while k <= n - 1:
            print('*', end=' ')
            k += 1
        print('')
        i -= 1
#rows = int(input("Enter the number of rows - patterns 4: "))
#print_pattern4(rows)

# pattern 5

def print_pattern5(n):
    for i in range(n):
        # Creates spaces to center the stars
        #print("I", i)
        spaces = ' ' * (n - i - 1)
        # Print starts the pyramid pattern
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

    for i in range(n - 1, 0, -1):
        # Spaces increase as rows decrease
        spaces = ' ' * (n - i)
        # print starts
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

rows = int(input("Enter the number of rows pattern 5: "))
print_pattern5(rows)
