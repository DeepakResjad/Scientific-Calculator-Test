import unittest
from scientific_calculator import sin_function,cos_function,log_function,exp_function,sqrt_function,tan_function,asin_function,acos_function,atan_function,sinh_function,cosh_function,tanh_function
import math

class TestScientificCalculator(unittest.TestCase):

    def test_sin_with_positive_angle(self):
        self.assertAlmostEqual(sin_function(90), math.sin(math.radians(90)))

    def test_sin_with_negative_angle(self):
        self.assertAlmostEqual(sin_function(-90), math.sin(math.radians(-90)))

    def test_sin_with_zero_angle(self):
        self.assertAlmostEqual(sin_function(0), math.sin(math.radians(0)))

    def test_sin_with_invalid_input(self):
        with self.assertRaises(TypeError):
            sin_function("hello")

    def test_cos_with_positive_angle(self):
        self.assertAlmostEqual(cos_function(90), math.cos(math.radians(90)))

    def test_cos_with_negative_angle(self):
        self.assertAlmostEqual(cos_function(-90), math.cos(math.radians(-90)))

    def test_cos_with_invalid_input(self):
        with self.assertRaises(TypeError):
            cos_function("hello")

    def test_logarithm_with_positive_input(self):
        self.assertAlmostEqual(log_function(10), math.log(10))

    def test_logarithm_with_zero(self):
        with self.assertRaises(ValueError):
            log_function(0)

    def test_logarithm_with_negative_input(self):
        with self.assertRaises(ValueError):
            log_function(-1)

    def test_logarithm_with_invalid_input(self):
        with self.assertRaises(TypeError):
            log_function("hello")

    def test_exponential_with_positive_input(self):
        self.assertAlmostEqual(exp_function(1), math.exp(1))

    def test_exponential_with_zero(self):
        self.assertAlmostEqual(exp_function(0), math.exp(0))

    def test_exponential_with_negative_input(self):
        self.assertAlmostEqual(exp_function(-1), math.exp(-1))

    def test_exponential_with_invalid_input(self):
        with self.assertRaises(TypeError):
            exp_function("hello")

    def test_tan_with_positive_angle(self):
        self.assertAlmostEqual(tan_function(45), math.tan(math.radians(45)))

    def test_tan_with_negative_angle(self):
        self.assertAlmostEqual(tan_function(-45), math.tan(math.radians(-45)))

    def test_tan_with_zero_angle(self):
        self.assertAlmostEqual(tan_function(0), math.tan(math.radians(0)))

    def test_tan_with_invalid_input(self):
        with self.assertRaises(TypeError):
            tan_function("hello")

    def test_square_root_of_positive_number(self):
        self.assertAlmostEqual(sqrt_function(16), math.sqrt(16))

    def test_square_root_of_zero(self):
        self.assertAlmostEqual(sqrt_function(0), math.sqrt(0))

    def test_square_root_of_negative_number(self):
        with self.assertRaises(ValueError):
            sqrt_function(-1)

    def test_square_root_with_invalid_input(self):
        with self.assertRaises(TypeError):
            sqrt_function("hello")

    def test_arcsin_with_valid_positive_input(self):
        self.assertAlmostEqual(asin_function(0.5), math.degrees(math.asin(0.5)))

    def test_arcsin_with_valid_negative_input(self):
        self.assertAlmostEqual(asin_function(-0.5), math.degrees(math.asin(-0.5)))

    def test_arcsin_with_out_of_domain_value(self):
        with self.assertRaises(ValueError):
            asin_function(2)

    def test_arcsin_with_invalid_input(self):
        with self.assertRaises(TypeError):
            asin_function("hello")

    def test_arccos_with_valid_positive_input(self):
        self.assertAlmostEqual(acos_function(0.5), math.degrees(math.acos(0.5)))

    def test_arccos_with_valid_negative_input(self):
        self.assertAlmostEqual(acos_function(-0.5), math.degrees(math.acos(-0.5)))

    def test_arccos_with_out_of_domain_value(self):
        with self.assertRaises(ValueError):
            acos_function(2)

    def test_arccos_with_invalid_input(self):
        with self.assertRaises(TypeError):
            acos_function("hello")

    def test_arctan_with_positive_value(self):
        self.assertAlmostEqual(atan_function(1), math.degrees(math.atan(1)))

    def test_arctan_with_negative_value(self):
        self.assertAlmostEqual(atan_function(-1), math.degrees(math.atan(-1)))

    def test_arctan_with_zero(self):
        self.assertAlmostEqual(atan_function(0), math.degrees(math.atan(0)))

    def test_arctan_with_invalid_input(self):
        with self.assertRaises(TypeError):
            atan_function("hello")

    def test_sinh_with_positive_value(self):
        self.assertAlmostEqual(sinh_function(1), math.sinh(1))

    def test_sinh_with_negative_value(self):
        self.assertAlmostEqual(sinh_function(-1), math.sinh(-1))

    def test_sinh_with_zero(self):
        self.assertAlmostEqual(sinh_function(0), math.sinh(0))

    def test_sinh_with_invalid_input(self):
        with self.assertRaises(TypeError):
            sinh_function("hello")

    def test_cosh_with_positive_value(self):
        self.assertAlmostEqual(cosh_function(1), math.cosh(1))

    def test_cosh_with_negative_value(self):
        self.assertAlmostEqual(cosh_function(-1), math.cosh(-1))

    def test_cosh_with_zero(self):
        self.assertAlmostEqual(cosh_function(0), math.cosh(0))

    def test_cosh_with_invalid_input(self):
        with self.assertRaises(TypeError):
            cosh_function("hello")

    def test_tanh_with_positive_value(self):
        self.assertAlmostEqual(tanh_function(1), math.tanh(1))

    def test_tanh_with_negative_value(self):
        self.assertAlmostEqual(tanh_function(-1), math.tanh(-1))

    def test_tanh_with_zero(self):
        self.assertAlmostEqual(tanh_function(0), math.tanh(0))

    def test_tanh_with_invalid_input(self):
        with self.assertRaises(TypeError):
            tanh_function("hello")

if __name__ == "__main__":
    unittest.main()
