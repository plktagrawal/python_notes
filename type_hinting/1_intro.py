from typing import List, Any, Tuple


class A:
    x: int
    y: List[Any]  # list of any data type, of any length
    z: List[int]  # list of integers, of any length
    w: Tuple[int, int, str]  # list of 3 items of specific types


a = A()

a.x = 5
a.y = [1, 2, "s"]
a.z = [1, 2, 3]
#a.w = [1, 2, "womania"]


# a.z = [1, 2, 3, "s"]
a.w = ("s", "f", "g")

print(a.x)
print(a.y)
print(a.z)
print(a.w)
