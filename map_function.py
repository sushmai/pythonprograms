temps = [("Berlin", 29), ('cario', 34), ("Newyork", 33), ("london",22), ("Los Angeles", 25) ]


# to convert it tio forenheat

c_to_f = lambda data : (data[0], (9/5)*data[1] + 32)

print(list(map(c_to_f, temps)))

s = "maps the data and do required changes in stead of re writing entire list"
print(list(map(s.count, s)))
# finding area
import math
def area(r):
    """area of circle with raius r."""
    return math.pi*(r**2)
radii = [2,3,4,5,6]
areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)
# using map
#gives iterator over the results:
print(map(area, radii))
print(list(map(area, radii)))
