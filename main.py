import os

#all code is written by D1aMonDNL

def return_home():
    os.system('cls')
    prime_app()


def num_input_prime():
    starter = 0
    is_prime = False
    while True:
        while True:
            num = float(input("Enter number to check if it's a prime number. Enter 0 to return to the home screen. "))
            half_num = num / 2
            if num == 0:
                return_home()
            while half_num > starter:
                starter += 1
                half_num = num / 2
                out = float(num / starter)
                if out.is_integer():
                    if not num == 1.0:
                        if 1 < out < num:
                            is_prime = False
                        else:
                            is_prime = True

            if is_prime:
                print("Inputted number is a prime number.")
            else:
                print("Inputted number isn't a prime number.")
            starter = 0


def num_range_prime():
    num = float(1)
    half_num = num / 2
    starter = 0
    is_prime = False
    num_range = int(input('enter range, enter 0 to return to the home screen: '))
    range_level = 0
    while num_range > 0:
        while num_range >= num:
            while half_num > starter:
                starter += 1
                half_num = num / 2
                out = float(num / starter)
                if out.is_integer():
                    if not num == 1.0:
                        if 1 < out < num:
                            is_prime = False
                        else:
                            is_prime = True

            if is_prime:
                print(num)
                range_level += 1
            starter = 0
            num += 1
            half_num = num / 2
        num_range = int(input("enter range, enter 0 to return to the home screen: "))

    if num_range == 0:
        os.system('cls')
        return_home()


def prime_app():
    os.system('cls')
    proceed = False
    print("Source code written and designed by - D1aMonD_NL")
    print("\n")
    print("Choose the function of choice.")
    print("1. Print all the prime numbers within a range.")
    print("2. Check if number is a prime number.")
    print("3. Exit the program.")
    while not proceed:
        try:
            choice = int(input())
            if choice == 1:
                num_range_prime()
                proceed = True
            elif choice == 2:
                num_input_prime()
                proceed = True
            elif choice == 3:
                exit()
            elif choice > 3:
                print("Inputted number is invalid, try again.")
                proceed = False
        except ValueError:
            print("Inputted character is not a number, try again.")
            proceed = False


prime_app()
