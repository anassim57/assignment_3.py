# ============================================================
# Assignment #3 - Numbers, Casting, Strings & Booleans
# Topics: W3Schools > Python Numbers, Python Casting,
#                     Python Strings, Python Booleans
#
# Instructions:
#  - Write your code under each question.
#  - For "PREDICT" questions, write your guess as a comment FIRST,
#    then run the code to check if you were right.
# ============================================================

stdCode = 34551001
stdName = 'Mohammed'
stdLastname = 'Ali'
stdMidterm = 80
stdFinal = 98.5
stdCity = '  Alexandria  '
stdEmail = 'mohammed.ali@school.edu'
stdPhone = '555-0142'
stdComment = ''


# ---------------- PART A: NUMBERS ----------------

# 1. Create these three variables and print the type of each:
#    a = 12      b = 12.0      c = 12 + 3j
a=12
b=12.0
c=12.3j

print("1.1 datatype of a is: ",type(a))
print("1.2 datatype of b is: ",type(b))
print("1.3 datatype of c is: ",type(c))


# 2. PREDICT: What is the type of x = 35e3 ? What value will print(x) show?
#    My guess: Integer. My guess was wrong. It seems taking decimal point and data type is float

x=35e3
print("2.1 type of x is: ", type(x))
print("2.2 value of x is: ", x)


# 3. Import the random module and print a random number between 1 and 10.
#    (Hint: random.randrange(1, 11))
# I need to learn more about random and related items

import random
print("3. Random number is:", random.randrange(1,11))


# ---------------- PART B: CASTING ----------------

# 4. The number "75" below is a STRING. Cast it to an int, add it to stdMidterm,
#    and print the result.
bonusPoints = "75"
bonusPointsInt = int(bonusPoints)
stdMidtermFinal=stdMidterm+bonusPointsInt

print("4. After adding bonus points, stdMidtermFinal number is:", stdMidtermFinal )


# 5. PREDICT: What will each line print?
#    print(int(9.99))
#    print(float(7))
#    print(str(3.0))
#    My guess: int = 9; float = 7.0; str = 3.0. All was correct guess

print("5.1 int value is: ", int(9.99))
print("5.2 float value is: ", float(7))
print("5.3 str value is: ", str(3.0))


# 6. Fix this line so it runs without an error (use casting):
#    print('Student code: ' + stdCode)

print("6. ", 'Student code: ',  stdCode)


# 7. PREDICT: What happens when you run print(int('12.5')) ? Try it, then
#    write a line that correctly turns '12.5' into the int 12.
#    My guess: it will print 12. My guess was wrong. Received error.
#  Need to turn into int by removing '' from the value and then it will turns into int 12

#print(int('12.5'))

print("7. Turning into int value: ",int(12.5))

# ---------------- PART C: STRINGS ----------------

# 8. Print the first letter of stdName, and the LAST letter of stdName
#    (use a negative index for the last letter). Not getting it properly

#stdName = 'Mohammed'
print("8.1 first letter of student name is: ",stdName[0:1])
print("8.2 last letter of student name using - is: ",stdName[-1])


# 9. Use slicing to print only 'Moh' from stdName.
print("3. slicing from std name :",stdName[0:3])


# 10. Print stdName in all UPPERCASE and stdLastname in all lowercase.
print("10.1 All upper case",stdName.upper())
print("10.2 All lower case",stdLastname.lower())


# 11. stdCity has extra spaces. Print it with the spaces removed using strip().
#     Then print len() of stdCity before and after strip().
print("11.1 removing space from city name: ",stdCity.strip())
print("11.2 city name length before strip: ",len(stdCity))
print("11.3 city name length after strip: ",len(stdCity.strip()))


# 12. Use replace() to change the '-' in stdPhone to a space and print it.

print("12. replacing space in place of -: ",stdPhone.replace('-', ' '))


# 13. Use split() to separate stdEmail at the '@' and print the result.
#     PREDICT: What data type does split() return?
#     My guess: String
#  stdEmail = 'mohammed.ali@school.edu'

print("13. Splitting email inplace of @: ",stdEmail.split('@'))

# 14. Use an f-string to print exactly:
#     Mohammed Ali scored 98.5 on the final.

print("14. ",f'Mohammed Ali scored {stdFinal} on the final.')



# 15. Use an f-string with a format specifier to print the average of
#     stdMidterm and stdFinal with exactly 2 decimal places.
#     Expected output: Average: 89.25. Tried for long and then learnt it

print("15. Printing upto two decimal point using function: ", f"{((stdMidterm+stdFinal)/2):.2f}")


# 16. Print this sentence using an escape character for the quotes:
#     The teacher said "Great job!" to Mohammed.

print("16. Print using escape character: ","The teacher said \"Great job!\" to Mohammed.")


# 17. Use the in keyword to check if 'school' is in stdEmail. Print the result.

print("17. using in keyword to check school word: ", 'school' in stdEmail)


# ---------------- PART D: BOOLEANS ----------------

# 18. PREDICT True or False for each, then check with bool():
#     bool(0)   bool(15)   bool("")   bool("False")   bool([])   bool(None)
#     My guesses: bool(0) = False;   bool(15)= True;  bool("") = False;   bool("False") = False: I am wrong here. It is True;  
# bool([])=False   bool(None) = False

print("18.1 Boolean value of bool(0):",bool(0))

print("18.2 Boolean value of bool(15):",bool(15))

print("18.3 Boolean value of bool(False):",bool("False"))

print("18.4 Boolean value of bool([]):",bool([]))

print("18.5 Boolean value of bool(None):",bool(None))


# 19. Print the result of bool(stdComment). Then explain in a comment
#     why it gives that answer.

print("19. As the value of stdComment is Null or Empty, it returns: ",bool(stdComment))


# 20. Use isinstance() to check if stdFinal is a float. Print the result.

print("20. Checking stdFinal data type using isinstance: ",isinstance(stdFinal, float))
# BONUS: Print stdName backwards ('demmahoM') using slicing.
#        Hint: [::-1]

print("Bonus: Printing student name backwards: ",stdName[::-1])