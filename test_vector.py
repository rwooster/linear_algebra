import unittest

from vector import Vector

class TestVector(unittest.TestCase):

    def test_addition(self):
        expected = Vector(4, 5, 6)
        result = Vector(1, 1, 1) + Vector(3, 4, 5)

        self.assertEqual(expected, result)
    
    def test_subtraction(self):
        expected = Vector(-4, 5, 6)
        result = Vector(1, 6, 12) - Vector(5, 1, 6)

        self.assertEqual(expected, result)

    def test_scalar_multiply(self):
        expected = Vector(-4, 4, 6)
        result = Vector(-2, 2, 3).scalar_multiply(2)

        self.assertEqual(expected, result)

    # Who can be bothered to compare floating points...
    def test_magnitude(self):
        print("Magnitudes:")
        result = Vector(-0.221, 7.437).magnitude()
        print(result)

        result = Vector(8.813, -1.331, -6.247).magnitude()
        print(result)

    def test_normalization(self):
        print("Normalizations:")
        result = Vector(5.581, -2.136).normalize()
        print(result)

        result = Vector(1.996, 3.108, -4.554).normalize()
        print(result)

    def test_dot(self):
        expected = 9
        result = Vector(1, 1, 1).dot(Vector(2, 3, 4))
        self.assertEqual(expected, result)

        print("Inner products:")
        print(Vector(7.887, 4.138).dot(Vector(-8.802, 6.776)))
        print(Vector(-5.955, -4.904, -1.874).dot(Vector(-4.496, -8.755, 7.103)))
    
    def test_angle(self):
        expected = 0
        result = Vector(1, 1, 1).theta(Vector(1, 1, 1))
        self.assertEqual(expected, result)

        expected = 90
        result = Vector(0, 5).theta_degrees(Vector(5, 0))
        self.assertEqual(expected, result)
        
        expected = 180
        result = Vector(0, 5).theta_degrees(Vector(0, -5))
        self.assertEqual(expected, result)

        print("Angles:")
        print(Vector(3.183, -7.627).theta(Vector(-2.668, 5.319)))
        print(Vector(7.35, 0.221, 5.188).theta_degrees(Vector(2.751, 8.259, 3.985)))


if __name__ == "__main__":
    unittest.main()
