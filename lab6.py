# 1. Assume that the variable data refers to the string "myprogram.exe". Write the values of the following expressions:

data = "myprogram.exe"

# a) data[2]
print(data[2])  # Output: 'y'

# b) data[-1]
print(data[-1])  # Output: 'e'

# c) len(data)
print(len(data))  # Output: 12

# d) data[0:8]
print(data[0:8])  # Output: 'myprogram'

# 2. Assume that the variable data refers to the string "myprogram.exe". Write the expressions that perform the following tasks:

# a) Extract the substring "gram" from data.
print(data[3:7])  # Output: 'gram'

# b) Truncate the extension ".exe" from data.
print(data[:-4])  # Output: 'myprogram'

# c) Extract the character at the middle position from data.
middle_index = len(data) // 2
print(data[middle_index])  # Output: 'o'

# 3. Assume that the variable myString refers to a string. Write a code segment that uses a loop to print the characters of the string in reverse order.

myString = "hello"

for i in range(len(myString) - 1, -1, -1):
    print(myString[i])

# 4. Assume that the variable myString refers to a string, and the variable reversedString refers to an empty string. Write a loop that adds the characters from myString to reversedString in reverse order.

myString = "hello"
reversedString = ""

for i in range(len(myString) - 1, -1, -1):
    reversedString += myString[i]

print(reversedString)  # Output: 'olleh'

# 5. Write a program that prompts the user to enter a letter grade A/a, B/b, C/c, D/d, or F/f and displays its corresponding numeric value 4, 3, 2, 1, or 0.

grade = input("Enter a letter grade (A, B, C, D, or F): ")

if grade.lower() == 'a':
    numeric_grade = 4
elif grade.lower() == 'b':
    numeric_grade = 3
elif grade.lower() == 'c':
    numeric_grade = 2
elif grade.lower() == 'd':
    numeric_grade = 1
else:
    numeric_grade = 0

print("Numeric grade:", numeric_grade)

# 6. A string is a palindrome if it reads the same forward and backward. The words "mom," "dad," and "noon," for instance, are all palindromes. Write a script that prompts the user to enter a string and reports whether the string is a palindrome or not (without reversing the string).

string = input("Enter a string: ")

is_palindrome = True
for i in range(len(string) // 2):
    if string[i] != string[len(string) - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# 7. Write a script that converts a string of bits to a decimal integer, e.g. when the user enters 101, the program should print 5.

bits = input("Enter a string of bits: ")

decimal_value = 0
for i in range(len(bits)):
    decimal_value += int(bits[i]) * (2 ** (len(bits) - i - 1))

print("Decimal value:", decimal_value)

# 8. Write a script that inputs a string (in lowercase letters) and a distance value and outputs an encrypted string using a Caesar cipher.

string = input("Enter a string: ")
distance = int(input("Enter the distance value: "))

encrypted_string = ""
for char in string:
    encrypted_char = chr((ord(char) - 97 + distance) % 26 + 97)
    encrypted_string += encrypted_char

print("Encrypted string:", encrypted_string)

# 9. Write a script that inputs encrypted string of lowercase letters and a distance value and outputs the decrypted string using a Caesar cipher.

encrypted_string = input("Enter the encrypted string: ")
distance = int(input("Enter the distance value: "))

decrypted_string = ""
for char in encrypted_string:
    decrypted_char = chr((ord(char) - 97 - distance) % 26 + 97)
    decrypted_string += decrypted_char

print("Decrypted string:", decrypted_string)