import math
import decimal

decimal.getcontext().prec = 10

class Vector:

    def __init__(self, *coordinates):
        self.coordinates = tuple(decimal.Decimal(x) for x in coordinates)

    def __str__(self):
        coordinate_str = ",".join(str(x) for x in self.coordinates)
        return "Vector: [{}]".format(coordinate_str)

    def __eq__(self, rhs):
       return self.coordinates == rhs.coordinates 

    def __add__(self, rhs):
        return Vector(*(a + b for a, b in zip(self.coordinates, rhs.coordinates)))

    def __sub__(self, rhs):
        return Vector(*(a - b for a, b in zip(self.coordinates, rhs.coordinates)))

    def scalar_multiply(self, scalar):
        return Vector(*(scalar * decimal.Decimal(a) for a in self.coordinates))

    def magnitude(self):
        return decimal.Decimal(math.sqrt(sum(a*a for a in self.coordinates)))

    def normalize(self):
        mag = self.magnitude()
        if (mag == 0):
            raise ValueError("Can't normalize the 0 vector")

        return self.scalar_multiply(decimal.Decimal('1.0') / mag)

    def dot(self, rhs):
        return sum(a*b for a, b in zip(self.coordinates, rhs.coordinates))

    def theta(self, rhs):
        x = self.dot(rhs) / (self.magnitude() * rhs.magnitude())
        return math.acos(x)

    def theta_degrees(self, rhs):
        return self.theta(rhs) * (180 / math.pi)
