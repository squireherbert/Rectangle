# Herbert Squire
# CIS 261
# Week 8, Lab 1 Rectangle

print("Rectangle Calculator")
pole = False
while not pole:
    height = int(input("Write length side height: "))
    width = int(input("Write length side width: "))
    area = height * width
    perimeter = 2 * (height + width)
    if area >= 0:
        print("Area of the rectangle:", area)
        print("Perimeter of the rectangle:", perimeter)
        pole = True
    else:
        print("Write correct data!")