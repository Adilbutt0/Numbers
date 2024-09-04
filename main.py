def prime_number(sum):
    if sum == 1 or sum ==0:
        return
    elif sum > 1:
        for i in range(2,sum):
            if sum % 2 == 0:
                print(f"{sum} is not a prime number")
                break
        else:
            print(f"{sum} is a prime number")
    else:
        print(f"{sum} is not a prime number")
name = input("Enter your name: ")
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
my_list = [num1,num2,num3]
even_odd = []
sqauree = []
for num in my_list:
    if num % 2 == 0:
        even_odd.append((num,"even"))
        print(f"the number {num} is even")
    else:
        even_odd.append((num,"odd"))
        print(f"the number {num} is odd")
for num in my_list:
    sqauree = ((num,num**2))
    print(f"the number is {num} and it's square is {sqauree}")
print(f'Hello {name},Lets explore your favorite numbers:')
sum = num1 + num2 + num3
print(f"Amazing! the sum of your favourite number is {sum}")
prime_number(sum)
