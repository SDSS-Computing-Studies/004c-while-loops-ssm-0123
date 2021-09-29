#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

scan = True

while scan :
    Num = input("Enter number: ")
    Num2 = Num
    Num2 = float(Num2)
    Num2 = round(Num2)
    Num = float(Num)
    if  Num == Num2 and Num%2 == 0 :
        print("That is an even integer")
        scan = False
    else :
        print("That is not an even integer")