def rectangle(width, height):
    print("|" + "-"*(width-2) + "|")

    for i in range(height-2):
        print("|" + " "*(width-2) + "|")

    print("|" + "-"*(width-2) + "|")

rectangle(20, 4)

