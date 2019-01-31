import line

line1 = line.Line([4.046, 2.836], 1.21)
line2 = line.Line([10.115, 7.09], 3.025)
print(line.are_parallel(line1, line2))
print(bool(line1 == line2))
try:
    print(line.get_intersection(line1, line2))
except Exception as e:
    print("No interestion")

line1 = line.Line([7.204, 3.128], 8.68)
line2 = line.Line([8.172, 4.114], 9.883)
print(line.are_parallel(line1, line2))
print(bool(line1 == line2))
try:
    print(line.get_intersection(line1, line2))
except Exception as e:
    print("No interestion: {}".format(e))

line1 = line.Line([1.182, 5.562], 6.744)
line2 = line.Line([1.773, 8.343], 9.525)
print(line.are_parallel(line1, line2))
print(bool(line1 == line2))
try:
    print(line.get_intersection(line1, line2))
except Exception as e:
    print("No interestion")
