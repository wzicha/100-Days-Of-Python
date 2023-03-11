def add(*args):
    # Takes an unlimited number of arguments
    total = 0
    for num in args:
        total += num
    print(total)
# Add an unlimited number of numbers defined as an argument in the function
add(1,1,2,4)
