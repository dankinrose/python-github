import datetime
import random

def get_rand_number():
    return random.randint(1, 5)

if __name__ == '__main__':

    first_number = get_rand_number()
    second_number = get_rand_number()

    print(first_number)
    print(second_number)

    if first_number == second_number:
        print("The numbers are equal with value " + str(first_number))
    else:
        print("The numbers are not equal first number value is: " +
              str(first_number) + " and second number value is: " + str(second_number))

    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime('%m-%d-%Y %H:%M:%S')

    print(formatted_date)