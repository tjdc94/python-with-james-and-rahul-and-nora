import numbers


def process_number(number: int) -> list:
    # numbers_list = [range(1, number + 1)]
    fizzbuzz = [
        n
        if n % 3 != 0
        else "fizz"
        if n % 5 != 0
        else "buzz"
        if n % 3 != 0 and n % 5 != 0
        else "fizzbuzz"
        for n in range(1, number + 1)
    ]
    return fizzbuzz


print(process_number(15))







# for f in range(1, number + 1)
# for b in range(n, number + 1)
# for f in range(b, number + 1)
# for fb in range(f, number + 1)
#  if f % 3 == 0
#  if b % 5 == 0
#  if fb % 3 == 0 and fb % 5 == 0
#         if number % 3 == 0
#         if number % 5 == 0
#         return "fizz"
#         return "buzz"
#         return number


# def process_number(number: int):
#         if number % 3 == 0 & number % 5 == 0:
#             return "fizzbuzz"
#         if number % 3 == 0:
#             return "fizz"
#         if number % 5 == 0:
#             return "buzz"
#         else:
#             return number
