arr = list()
tests = input()
for test in range(int(tests)):
    test = input()
    instruction = test.split(" ")
    if instruction[0] in dir(arr) and callable(getattr(arr, instruction[0])):
        args = instruction[1:]
        args = list(map(int, args))  # str -> int
        f = getattr(arr, instruction[0])  # get the callable method
        f(*args)  # and send it *whatever* argument you have
    else:
        if instruction[0] == "print":
            print(arr)