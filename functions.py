import math

class Area:
    def area_rect(self):
        return nums[0] * nums[1]

    def area_circle(self):
        return (math.pi * (num ** 2))

    def area_sqr(self):
        return num ** 2

    def area_tri(self):
        return (nums[0] * nums[1] * 0.5)


class Perimeter:
    def perim_rect(self):
        return ((2 * nums[0]) + (2 * nums[1]))

    def perim_sqr(self):
        return (num * 4)

    def perim_tri(self):
        return sum(nums)

    def perim_circle(self):
        return ((2 * num) * math.pi)