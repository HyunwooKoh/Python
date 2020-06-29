from HW2 import problem4 as geometry


while 1:
    print("What is the kind of Geometry?")
    print("1: SQUARE, 2: TRIANGLE, 3: PYTHAGOREAN THEOREM, 4: TRAPEZOID, 5: CUBE")
    print("6: RECTANGLE, 7: PARALLELOGRAM, 8 : CIRCULAR RING, 9: RECTANGULAR BOX, 10: CYLINDER")
    print("11: CIRCLE, 12: CIRCULAR SECTION, 13: SPHERE, 14: RIGHT CIRCULAR CONE 15: FRUSTUM OF A CONE")
    print("press 0 to finish")
    kind = input()
    kind = int(kind)
    if kind == 0:
        break
    if kind == 1:
        g = geometry.Square()
        print("round of the SQUARE : press 1, area of the SQUARE : press 2")
        t = int(input())
        print("insert the length of side : ")
        s = input()
        if t == 1:
            print("round of the SQUARE is ", g.c_around(s))
        else:
            print("area if the SQUARE is ", g.c_area(s))

    if kind == 2:
        g = geometry.TRIANGLE()
        print("round of the TRIANGLE : press 1, area of the TRIANGLE : press 2")
        t = int(input())
        if t == 1:
            a, b, c = input("insert the length of the three side (a,b,c)").split()
            print("round of the TRIANGLE is ", g.c_around(a, b, c))
        else:
            b, h = input("insert the length of one side and its height : ").split()
            print("area of the TRIANGLE is ", g.c_area(b, h))

    if kind == 3:
        a, b = input("input the length of under side and height : ").split()
        g = geometry.PYTHAGOREAN_THEOREM()
        print("the result is ", g.c_slide(a, b))

    if kind == 4:
        g = geometry.TRAPEZOID()
        print("round of the TRAPEZOID : press 1, area of the TRAPEZOID : press 2")
        t = int(input())
        if t == 1:
            a, b, c, d = input("insert the length of the four side : ").split()
            print("round of the TRAPEZOID is ", g.c_around(a, b, c, d))
        else:
            a, b, h = input("insert length of upper and under side and height (a,b,h) : ").split()
            print("area of TRAPEZOID is ", g.c_area(a, b, h))

    if kind == 5:
        g = geometry.CUBE()
        print("volume of the CUBE : press 1, area of the CUBE : press 2")
        t = int(input())
        print("insert the length of the side : ")
        l = input()
        if t == 1:
            print("Volume of the CUBE is ", g.c_volume(l))
        if t == 2:
            print("Area of the CUBE is ", g.c_area(l))

    if kind == 6:
        g = geometry.RECTANGLE()
        print("round of the RECTANGLE : press 1, area of the RECTANGLE : press 2")
        t = int(input())
        a, b = input("insert the length of two side : ").split()
        if t == 1:
            print("round of the RECTANGLE is ", g.c_around(a, b))
        else:
            print("area if the RECTANGLE is ", g.c_area(a, b))

    if kind == 7:
        g = geometry.PARALLELOGRAM()
        print("round of the PARALLELOGRAM : press 1, area of the PARALLELOGRAM : press 2")
        t = int(input())
        if t == 1:
            a, b = input("insert the length of two side : ").split()
            print("round of the PARALLELOGRAM is ", g.c_around(a, b))
        else:
            b, h = input("insert the length of under side and height : ").split()
            print("area if the PARALLELOGRAM is", g.c_area(b, h))

    if kind == 8:
        g = geometry.CIRCULAR_RING()
        rr, sr = input("insert the large radius and small radius : ").split()
        print("area of the CIRCULAR RING is ", g.c_area(sr, rr))

    if kind == 9:
        g = geometry.RECTANGULAR_BOX()
        print("volume of the RECTANGULAR_BOX : press 1, area of the RECTANGULAR_BOX : press 2")
        t = int(input())
        a, b, c = input("insert height and the length of two side : ").split()
        if t == 1:
            print("Volume of the RECTANGULAR_BOX is ", g.c_volume(a, b, c))
        if t == 2:
            print("Area of the RECTANGULAR_BOX is ", g.c_area(a, b, c))

    if kind == 10:
        g = geometry.CYLINDER()
        print("volume of the CYLINDER : press 1, area of the CYLINDER : press 2")
        t = int(input())
        r, h = input("insert radius and height : ").split()
        if t == 1:
            print("Volume of the CYLINDER is ", g.c_volume(r, h))
        if t == 2:
            print("Area of the CYLINDER is ", g.c_area(r, h))

    if kind == 11:
        g = geometry.CIRCLE()
        print("round of the CIRCLE : press 1, area of the CIRCLE : press 2")
        t = int(input())
        r = input("insert radius : ")
        if t == 1:
            print("round of the CIRCLE is ", g.c_around(r))
        else:
            print("area of the CIRCLE is ", g.c_area(r))

    if kind == 12:
        g = geometry.CIRCULAR_SECTION()
        print("L of the CIRCULAR  SECTION : press 1, area of the CIRCULAR SECTION : press 2")
        t = int(input())
        ag, r = input("insert the central angel and radius : ").split()
        if t == 1:
            print("L of the CIRCULAR SECTION is ", g.c_around(ag, r))
        else:
            print("area of the CIRCULAR SECTION is ", g.c_area(ag, r))

    if kind == 13:
        g = geometry.SPHERE()
        print("volume of the SPHERE : press 1, area of the SPHERE : press 2")
        t = int(input())
        r = input("insert the radius : ")
        if t == 1:
            print("Volume of the SPHERE is ", g.c_volume(r))
        if t == 2:
            print("Area of the SPHERE is ", g.c_area(r))

    if kind == 14:
        g = geometry.RIGHT_CIRCULAR_CONE()
        print("volume of the RIGHT_CIRCULAR_CONE : press 1, area of the RIGHT_CIRCULAR_CONE : press 2")
        t = input()
        t = int(t)
        h, r = input("insert the height and radius : ").split()

        if t == 1:
            print("Volume of the SPHERE is ", g.c_volume(r, h))
        if t == 2:
            print("Area of the SPHERE is ", g.c_area(r, h))

    if kind == 15:
        g = geometry.FRUSTUM_CONE()
        h, rr, sr = input("insert the height, upper Circle's radius and under Circle's radius : ").split()
        print("Volume of the SPHERE is ", g.c_volume(sr, rr, h))



