#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    limit_checking = int(number / 2) + 1
    if number > 0:
        if int(number / 2) == 1 or int(number / 1) == 1:
            is_prime = True
        for i in range(2, limit_checking):
            if number % i == 0:
                is_prime = False
    else:
        print("It's not a prime number.")
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
