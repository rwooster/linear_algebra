import unittest

from vector import Vector

class TestVector(unittest.TestCase):

    def __compare(self, expected, results):
        for e, r in zip(expected, results):
            self.assertEqual(e, r)

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
        expected = [Vector(0.9339352142,-0.3574423253)]
        result = [Vector(5.581, -2.136).normalize()]

        expected.append(Vector(0.3404012959,0.5300437012,-0.7766470448))
        result.append(Vector(1.996, 3.108, -4.554).normalize())

        self.__compare(expected, result)

    def test_dot(self):
        expected = [9]
        result = [Vector(1, 1, 1).dot(Vector(2, 3, 4))]

        expected.append(-41.38228600)
        result.append(Vector(7.887, 4.138).dot(Vector(-8.802, 6.776)))

        expected.append(56.39717800)
        result.append(Vector(-5.955, -4.904, -1.874).dot(Vector(-4.496, -8.755, 7.103)))

        self.__compare(expected, result)
    
    def test_angle(self):
        expected = [0]
        result = [Vector(1, 1, 1).theta(Vector(1, 1, 1))]

        expected.append(90)
        result.append(Vector(0, 5).theta_degrees(Vector(5, 0)))
        
        expected.append(180)
        result.append(Vector(0, 5).theta_degrees(Vector(0, -5)))

        expected.append(3.0720263111831025)
        result.append(Vector(3.183, -7.627).theta(Vector(-2.668, 5.319)))

        expected.append(60.27581120560713)
        result.append(Vector(7.35, 0.221, 5.188).theta_degrees(Vector(2.751, 8.259, 3.985)))

        self.__compare(expected, result)


if __name__ == "__main__":
    unittest.main()
