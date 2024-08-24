def addition(ftnum, scnum):
    result = ftnum + scnum
    return result

def subtraction(ftnum, scnum):
    result = ftnum - scnum
    return result

def multiplication(ftnum, scnum):
    result = ftnum * scnum
    return result

def division(ftnum, scnum):
    result = ftnum // scnum
    return result

def remainder(ftnum, scnum):
    result = ftnum % scnum
    return result

print("This is calculation program\n")
print("Enter 1: to addition")
print("Enter 2: to subtraction")
print("Enter 3: to multiplication")
print("Enter 4: to division")
print("Enter 5: to remainder")
print("Enter 6: to exit")

ls = [1,2,3,4,5]

while True:

    ch_num = int(input("Choose a number:> "))

    if ch_num > 6:
        print("Try Again")

    if ch_num in ls:

        try:
            print("You chose method number of {0} to calculation".format(ch_num))
            ftnum = int(input("Enter first number:>"))
            scnum = int(input("Enter second number:>"))
            print("First number is",ftnum)
            print("Second number is", scnum)

        except ValueError:
            print("Invalid Value Error")

        if ch_num == 1:
            print("The addition numbers of {0} and {1} is".format(ftnum, scnum), addition(ftnum, scnum))
    
        elif ch_num == 2:
            print("The subtraction numbers of {0} and {1} is".format(ftnum, scnum), subtraction(ftnum, scnum))

        elif ch_num == 3:
            print("The multiplication numbers of {0} and {1} is".format(ftnum, scnum), multiplication(ftnum, scnum))

        elif ch_num == 4:
            print("The division numbers of {0} and {1} is".format(ftnum, scnum), division(ftnum, scnum))

        elif ch_num == 5:
            print("The remainder numbers of {0} and {1} is".format(ftnum, scnum), remainder(ftnum, scnum))
    
        ply_again = str(input("Do you want to more calculation? (yes or no) :>"))
        if ply_again == 'yes':
            continue
        else:
            print("Quit calcuation")
            quit()
    
    elif ch_num == 6:
        print("Exit Program")
        exit(0)

else:
    print("something is wrong")



