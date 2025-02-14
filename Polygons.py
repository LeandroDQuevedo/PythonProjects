i = 1
while i == 1:

    shape = input("Which polygon do you want to calculate? (s)Square (c)Circle (r)Rectangle (t)Triangle ")
    if shape == "s":
        edge_length = int(input("What is the edge length?"))
        print("The area of the square is", edge_length * 2)
    else:
        if shape == "c":
            diameter = int(input("What is the diameter?"))
            print("The area of the circle is", diameter ** 2 * 3.14)
        else:
            if shape == "r":
                length = int(input("What is the length?"))
                height = int(input("What is the height?"))
                print("The area of the rectangle is", length * height)
            else:
                base = int(input("What is the base length?"))
                height = int(input("What is the height?"))
                print("The area of the triangle is", base * height / 2)
    i = int(input("Do you want to perform another operation? (1)Yes (2)No")) 
exit
