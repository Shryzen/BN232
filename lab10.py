def harmonic(n):
  """Calculates the nth harmonic number recursively."""
  if n == 1:
    return 1
  else:
    return 1 / n + harmonic(n - 1)

def printStars(n):
  """Prints the given number of asterisks recursively."""
  if n > 0:
    print("*", end="")
    printStars(n - 1)

def sumDigits(n):
  """Calculates the sum of the digits in an integer recursively."""
  if n == 0:
    return 0
  else:
    return n % 10 + sumDigits(n // 10)

def reverseDisplay(value):
  """Displays a string reversely on the console recursively."""
  if len(value) > 0:
    reverseDisplay(value[1:])
    print(value[0], end="")

# Test the functions
n = int(input("Enter an integer for harmonic number: "))
print("Harmonic number:", harmonic(n))

n = int(input("Enter an integer for number of stars: "))
printStars(n)

n = int(input("Enter an integer for sum of digits: "))
print("Sum of digits:", sumDigits(n))

string = input("Enter a string for reverse display: ")
reverseDisplay(string)
# no 2
def printStars(n):
    if n > 0:
        print("*", end="")
        printStars(n - 1)

# Test case
printStars(5)  # Output: *****
#no 3
def sumDigits(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sumDigits(num // 10)

# Test case
number = int(input("Enter an integer: "))
print("Sum of digits:", sumDigits(number))
#no 4
def reverseDisplay(value):
    if len(value) > 0:
        print(value[-1], end="")
        reverseDisplay(value[:-1])

# Test case
string = input("Enter a string: ")
print("Reversed string:", end=" ")
reverseDisplay(string)