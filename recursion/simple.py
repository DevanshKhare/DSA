def recursiveMethod(n):
    if n<1:
        print("N is less than 1")
    else:
        recursiveMethod(n-1) #these will be pushed to the stack
        print(n) #and this wont be executed instantly it will be executed when method is popped out from stack

recursiveMethod(4)