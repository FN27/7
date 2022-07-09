number = int(input('Enter number lower then 1000000000: '))


def number_in_list(number):
    numbers = []

    if int(number) < 1000000000:
        number = int(numbers)
        for i in str(number):
            numbers.append(i)

    return numbers



def calculate(numbers, number):
    if int(numbers[0]) == 1 or number > 1000000000:
        while int(numbers[0]) == 1 or number > 1000000000:
            number = int(input("Please enter new number: "))
            number_in_list(number)
            if number <= 1000000000 and int(numbers[0]) != 1:
                continue
            while True:
                number = int(number) * int(numbers[0])
                numbers = number_in_list(number)
                print(number)
                if int(numbers[0]) == 1:
                    break
            if int(numbers[0]) == 1:
                break

    else:
        while True:
            number = int(number) * int(numbers[0])
            numbers = number_in_list(number)
            print(number)
            if int(numbers[0]) == 1:
                break


calculate(number_in_list(number), int(number))
