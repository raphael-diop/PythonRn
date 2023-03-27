def triangle(height):
    for i in range(height):
        print(" "*(height-i-1), end="")
        
        print("/", end="")
        
        if i == height-1:
            print("_"*(2*i+1))
        elif i > 0:
            print(" "*(2*i-1) + "\\")
        else:
            print("")

triangle(10)

