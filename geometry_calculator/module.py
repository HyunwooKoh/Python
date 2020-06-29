from math import *


class Square:
    def __init__(self):
        self.len = 0.0
        self.area = 0.0

    def c_around(self, length):
        self.len = 4 * float(length)
        return self.len

    def c_area(self, length):
        self.area = float(length) * float(length)
        return self.area


class TRIANGLE:
    def __init__(self):
        self.len = 0.0
        self.area = 0.0

    def c_around(self, len1, len2, len3):
        self.len = float(len1) + float(len2) + float(len3)
        return self.len

    def c_area(self, low, height):
        self.area = float(low) * float(height) / 2
        return self.area


class PYTHAGOREAN_THEOREM:
    def __init__(self):
        self.c = 0.0

    def c_slide(self, a, b):
        self.c = sqrt(float(a) * float(a) + float(b) * float(b))
        return self.c


class TRAPEZOID:
    def __init__(self):
        self.len = 0.0
        self.area = 0.0

    def c_around(self, len1, len2, len3, len4):
        self.len = float(len1) + float(len2) + float(len3) + float(len4)
        return self.len

    def c_area(self, len1, len2, height):
        self.area = (float(len1) + float(len2)) / 2 * float(height)
        return self.area


class CUBE:
    def __init__(self):
        self.vol = 0.0
        self.area = 0.0

    def c_volume(self, len1):
        self.vol = float(len1) * float(len1) * float(len1)
        return self.vol

    def c_area(self, len1):
        self.area = 6 * float(len1) * float(len1)
        return self.area


class RECTANGLE:
    def __init__(self):
        self.len = 0.0
        self.area = 0.0

    def c_around(self, len1, len2):
        self.len = 2 * (float(len1) + float(len2))
        return self.len

    def c_area(self, len1, len2):
        self.area = float(len1) * float(len2)
        return self.area


class PARALLELOGRAM:
    def __init__(self):
        self.len = 0.0
        self.area = 0.0

    def c_around(self, len1, len2):
        self.len = 2 * (float(len1) + float(len2))
        return self.len

    def c_area(self, len1, len2):
        self.area = float(len1) * float(len2)
        return self.area


class CIRCULAR_RING:
    def __init__(self):
        self.area = 0.0

    def c_area(self, sr, rr):
        self.area = pi * (float(rr) * float(rr) - float(sr) * float(sr))
        return self.area


class RECTANGULAR_BOX:
    def __init__(self):
        self.vol = 0.0
        self.area = 0.0

    def c_volume(self, len1, len2, len3):
        self.vol = float(len1) * float(len2) * float(len3)
        return self.vol

    def c_area(self, len1, len2, len3):
        self.area = 2 * float(len1) * float(len2) + 2 * float(len1) * float(len3) + 2 * float(len2) * float(len3)
        return self.area


class CYLINDER:
    def __init__(self):
        self.vol = 0.0
        self.area = 0.0

    def c_volume(self, r, height):
        self.vol = pi * float(r) * float(r) * float(height)
        return self.vol

    def c_area(self, r, height):
        self.area = 2 * pi * float(r) * (float(r) + float(height))
        return self.area


class CIRCLE:
    def __init__(self):
        self.len = 0.0
        self.area = 0.0

    def c_around(self, r):
        self.len = 2 * pi * float(r)
        return self.len

    def c_area(self, r):
        self.area = pi * float(r) * float(r)
        return self.area


class CIRCULAR_SECTION:
    def __init__(self):
        self.len = 0.0
        self.area = 0.0

    def c_around(self, ag, r):
        self.len = l = pi * float(r) * float(ag) / 180
        return self.len

    def c_area(self, ag, r):
        self.area = pi * float(r) * float(r) * float(ag) / 360
        return self.area


class SPHERE:
    def __init__(self):
        self.vol = 0.0
        self.area = 0.0

    def c_volume(self, r):
        self.vol = pi * float(r) * float(r) * float(r) * 4 / 3
        return self.vol

    def c_area(self, r):
        self.area = 4 * pi * float(r) * float(r)
        return self.area


class RIGHT_CIRCULAR_CONE:
    def __init__(self):
        self.vol = 0.0
        self.area = 0.0

    def c_volume(self, r, height):
        self.vol = pi * float(r) * float(r) * float(height) / 3
        return self.vol

    def c_area(self, r, height):
        self.area = pi * float(r) * float(r) + pi * float(r) * sqrt(float(r) * float(r) + float(height) * float(height))
        return self.area


class FRUSTUM_CONE:
    def __init__(self):
        self.vol = 0.0

    def c_volume(self, sr, rr, height):
        self.vol = pi * float(height) * (float(sr) * float(sr) + float(sr) * float(rr) + float(rr) * float(rr)) / 3
        return self.vol
