#BG 1st recursion notes

#What type of code does recursion replace?
    #Recursion replaces iteration.
    #Instead of using loops (for / while),
    #recursion repeats actions by calling itself.


#What is a base case?
    #A base case is the stopping condition of a recursive function.
    #It is the simplest case where the function does NOT call itself again.


    #How do you set up a recursive function?
        #A recursive function must have:
            #A base case
            #A recursive case (function calls itself with smaller input)

def example(n):
    #Base case
    if n == 0:
        return "Done"
    
    #Recursive case
    return example(n - 1)


# Why do we use recursion?
    # We use recursion when:
        #A problem can be broken into smaller versions of itself
        #The structure is naturally recursive (like trees)
        #Divide-and-conquer algorithms are needed
        #It makes the code simpler and clearer
even = []

num = 3
sum = 1
for x in range(1,num +1):
    sum *= x
print(f"loop: {sum}")

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)
print(f"recurtion: {factorial(num)}")


fib = [1,1]
for i in range(1,11):
    fib.append(fib[i-1] + fib[i])
print(f'loop: {fib}')


numbers = []
def fibonacci(n):
    numbers.append(n)
    if n == 2: 
        return 1
    elif n ==1:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(f"recturtions: {fibonacci(11)}")