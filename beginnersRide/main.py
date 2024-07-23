'''Syntax'''
print("Hello Ride")
print()

'''Variables'''
num = 5
print(num)
print()

'''Strings'''
'''Ex1'''
name = "Gerald"
print('My name is', name)
'''Ex2'''
print('My name is Gerald')
print()


'''Number - Arithmetic Symbols'''
print(1 + 1)
print(2 - 1)
print( 2 / 2)
print(3 // 2)
print(3 % 2)
print(2 * 2)
print()

'''Booleans'''
print(True)
print(False)
print(3 > 2)
print(4 < 2)
print(1 + 1 == 4)
print()

'''Immutable'''
num = (2)
print(num)
print()

'''List'''
colors = ['Red', 'Green', 'Blue', 'Yellow', 'Violet']
print(colors)
print()

'''Comments'''
#This Is A Comment. I will be using this for the rest of this basic python project 👌

#Types Coversion
num = 3
print(type(num))
print(float(num))
print(int(num))
print(str(num))
print(bool(3))
print()

# Comparison Operations and Logical Operators
print(1 > 2)
print(3 > 1)
print(1 == 1)
print(2 != 1)
print(1 & 1 == 2)
print(3 | 2 > 1)
print()

# Control FLow and while loop
# active = True
# while active:
#     age = int(input('Enter a number: '))
#     if age == 0:
#         break
#     elif age <= 5 or age >= 80:
#         print('This Ticket Is Free')
#     elif age < 18:
#         print('Ticket is $5')
#     elif age < 80:
#         print('This Ticket is $10')

print()

x = [x for x in range(10) if x % 2 == 0]
print(x)
print()


#Functions
def myName(name):
    print('Hello my name is', name)

if __name__ == '__main__':
    myName('Stephanie')
print()

def adding(num1, num2):
    final = num1 + num2
    print("Your answer is", final)

if __name__ == '__main__':
    print(adding(2,3))


##Python 101
##This is to show my clear knowledge of basic python language
