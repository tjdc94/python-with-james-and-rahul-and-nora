# 0 1 1 2 3 5 8 13 21

def fibonacci(x):
    if x <= 1:
        return x
    return fibonacci(x-1) + fibonacci(x-2) 

if __name__ == "__main__": #Ask about this line
    print([fibonacci(x) for x in range (5)])
    print([fibonacci(x) for x in range (10)])
    print([fibonacci(x) for x in range (15)])
