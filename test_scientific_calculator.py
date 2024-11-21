import unittest
from scientific_calculator import sin_function, cos_function, tan_function, sqrt_function, log_function, exp_function
import math

class TestScientificCalculator(unittest.TestCase):
    
    def test_sin(self):
        self.assertAlmostEqual(sin_function(30), math.sin(math.radians(30)))
        self.assertAlmostEqual(sin_function(-30), math.sin(math.radians(-30)))
        with self.assertRaises(TypeError):
            sin_function("invalid")
    
    def test_cos(self):
        self.assertAlmostEqual(cos_function(60), math.cos(math.radians(60)))
        self.assertAlmostEqual(cos_function(-60), math.cos(math.radians(-60)))
        with self.assertRaises(TypeError):
            cos_function("invalid")

    def test_tan(self):
        self.assertAlmostEqual(tan_function(45), math.tan(math.radians(45)))
        self.assertAlmostEqual(tan_function(-45), math.tan(math.radians(-45)))
        with self.assertRaises(TypeError):
            tan_function("invalid")

    def test_sqrt(self):
        self.assertAlmostEqual(sqrt_function(16), math.sqrt(16))
        self.assertAlmostEqual(sqrt_function(0), math.sqrt(0))
        with self.assertRaises(ValueError):
            sqrt_function(-16)
        with self.assertRaises(TypeError):
            sqrt_function("invalid")

    def test_log(self):
        self.assertAlmostEqual(log_function(10), math.log(10))
        with self.assertRaises(ValueError):
            log_function(0)
        with self.assertRaises(ValueError):
            log_function(-10)
        with self.assertRaises(TypeError):
            log_function("invalid")

    def test_exp(self):
        self.assertAlmostEqual(exp_function(2), math.exp(2))
        self.assertAlmostEqual(exp_function(0), math.exp(0))
        self.assertAlmostEqual(exp_function(-2), math.exp(-2))
        with self.assertRaises(TypeError):
            exp_function("invalid")

if __name__ == "__main__":
    unittest.main()
