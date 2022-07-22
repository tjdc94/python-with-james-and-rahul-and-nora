# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120


# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1

# f(x) -> y




def factorial(x):
    # basecase
    if x == 0 or x == 1:
        return 1
    elif x < 0:
        return "🤯"
    return x * factorial(x - 1)
    

if __name__ == "__main__": #Ask about this line
    print(factorial(-1))
    print(factorial(0))
    print(factorial(1))
    print(factorial(3))
    print(factorial(5))