# number1=input("Eter the first number: ")
# number2=input("Enter the second number: ")
# try:
#     print(int(number1)+int(number2), "is the answer")
# except:
#     print("There is an error in what you have written.")

# print("Programm is still running")

name=input("Enter your name: ")
if name.isnumeric():
    raise Exeption("Numbers are not allowed")