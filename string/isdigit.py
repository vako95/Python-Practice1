numbers = "123456 7890 1122"


if  numbers.isdigit():
    num = int(numbers)
    if num % 2 == 0:
        

        print("yes is it",num)
    else:
        print("нечетное",num)