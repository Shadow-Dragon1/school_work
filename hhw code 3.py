#To calculate perimeter/circumference and area of shapes such as triangle, rectangle, square and circle
shape=input("name of shape(triangle rectangle square circle): ")

def circle():
    r=int(input("radius of circle: "))
    perimeter=2*3.14*r
    area=(r**2)*3.14
    print("area is",area)
    print("perimeter is ",perimeter)

def square():
    a=int(input("side of square: "))
    area=a**2
    perimeter=a*4
    print("area is",area)
    print("perimeter is ",perimeter)
def rectangle():
    a=int(input("side of rectangle:"))
    b=int(input("side of rectangle:"))
    area=a*b
    perimeter=2*(a*b)
    print("area is",area)
    print("perimeter is ",perimeter)
def triangle():
    a=int(input("side of triangle"))
    b=int(input("side of triangle"))
    c=int(input("side of triangle"))
    perimeter=a+b+c
    s=(a+b+c)/2
    x=s-a
    y=s-b
    z=s-c
    area=(s*x*y*z)**1/2
    print("area is",area)
    print("perimeter is ",perimeter)
if shape=="triangle":
    triangle()
elif shape=="square":
    square()
elif shape=="rectangle":
    rectangle()
elif shape=="circle":
    circle()
else:
   print("write a valid shape")