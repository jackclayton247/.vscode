#subroutine to ^2 digits of numbers and add them
def HappyNumber(TheInput):
    number = TheInput
    Happy = 0
    while Happy != 1:
        Happy = 0
        for counter in range(0, len(str(number)), 1):
            digit = int(str(number)[counter])
            square = digit * digit
            if counter == 0:
                number = number
            else:
                number = number + square
            Happy = Happy + int(str(number)[counter])
    if Happy == 1:
        print("{} is a happy number.".format(TheInput))
        
#main
HappyNumber(19)