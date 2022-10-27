import unittest

from complex_number import ComplexNumber

"""
Test case 1 (1. String conversion):
Points: 7
"""


class ComplexNumberStringUnitTests(unittest.TestCase):
    def test_string_conversion(self):
        # Arrange
        expected = "5 + 7i"

        # Act
        z = ComplexNumber(5, 7)
        actual = str(z)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_string_conversion_negative_imaginary_part(self):
        # Arrange
        expected = "5 - 7i"

        # Act
        z = ComplexNumber(5, -7)
        actual = str(z)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_string_conversion_no_imaginary_part(self):
        # Arrange
        expected = "5"

        # Act
        z = ComplexNumber(5, 0)
        actual = str(z)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_string_conversion_negative_real_part_no_imaginary_part(self):
        # Arrange
        expected = "-5"

        # Act
        z = ComplexNumber(-5, 0)
        actual = str(z)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_string_conversion_no_real_part(self):
        # Arrange
        expected = "7i"

        # Act
        z = ComplexNumber(0, 7)
        actual = str(z)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_string_conversion_no_real_part_negative_imaginary_part(self):
        # Arrange
        expected = "-7i"

        # Act
        z = ComplexNumber(0, -7)
        actual = str(z)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_string_conversion_zero(self):
        # Arrange
        expected = "0"

        # Act
        z = ComplexNumber(0, 0)
        actual = str(z)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


"""
Test case 2 (1.0. Constructor default arguments):
Points: 2
"""


class ComplexNumberConstructorUnitTests(unittest.TestCase):
    def test_constructor_all_defaults(self):
        # Arrange
        expected = "0"

        # Act
        z = ComplexNumber()
        actual = str(z)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_constructor_1_default(self):
        # Arrange
        expected = "5"

        # Act
        z = ComplexNumber(5)
        actual = str(z)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


"""
Test case 3 (2. Representation):
Points: 2
"""


class ComplexNumberRepresentationUnitTests(unittest.TestCase):
    def test_representation(self):
        # Arrange
        z = ComplexNumber(5, 7)
        expected = "ComplexNumber(5, 7)"

        # Act
        actual = repr(z)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


"""
Test case 4 (3. Re and Im):
Points: 2
"""


class ComplexNumberReImUnitTests(unittest.TestCase):
    def test_re(self):
        # Arrange
        z = ComplexNumber(3, 4)
        expected = 3

        # Act
        actual = z.re()

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_im(self):
        # Arrange
        z = ComplexNumber(3, 4)
        expected = 4

        # Act
        actual = z.im()

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


"""
Test case 5 (4. Equality):
Points: 1
"""


class ComplexNumberEqualityUnitTests(unittest.TestCase):
    def test_equality(self):
        # Arrange
        z = ComplexNumber(3, 4)
        w = ComplexNumber(3, 4)

        # Act
        actual = z == w

        # Assert
        self.assertTrue(actual)
        self.assertEqual(z, w)

    def test_identity(self):
        # Arrange
        z = ComplexNumber(3, 4)
        w = z

        # Act
        actual = z == w

        # Assert
        self.assertTrue(actual)
        self.assertEqual(z, w)

    def test_not_equal(self):
        # Arrange
        z = ComplexNumber(3, 4)
        w = ComplexNumber(5, 4)

        # Act
        actual = z == w

        # Assert
        self.assertFalse(actual)
        self.assertNotEqual(z, w)

    def test_another_unequal_pair(self):
        # Arrange
        z = ComplexNumber(3, 4)
        w = ComplexNumber(4, 3)

        # Act
        actual = z == w

        # Assert
        self.assertFalse(actual)
        self.assertNotEqual(z, w)

    def test_another_unequal_pair_with_negatives(self):
        # Arrange
        z = ComplexNumber(3, 4)
        w = ComplexNumber(-3, -4)

        # Act
        actual = z == w

        # Assert
        self.assertFalse(actual)
        self.assertNotEqual(z, w)

    def test_evaluation_of_representation(self):
        # Arrange
        z = ComplexNumber(5, 7)
        expected = ComplexNumber(5, 7)

        # Act
        actual = eval(repr(z))

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)
        self.assertEqual(ComplexNumber, type(actual))


"""
Test case 6 (5. Conjugation):
Points: 2
"""


class ComplexNumberConjugationUnitTests(unittest.TestCase):
    def test_conjugate(self):
        # Arrange
        z = ComplexNumber(3, 4)
        expected = ComplexNumber(3, -4)

        # Act
        actual = z.conjugate()

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)
        self.assertEqual(ComplexNumber, type(actual))

    def test_double_conjugation(self):
        # Arrange
        z = ComplexNumber(3, 4)
        expected = z

        # Act
        actual = z.conjugate().conjugate()

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_original_not_modified(self):
        # Arrange
        z = ComplexNumber(3, 4)
        expected = ComplexNumber(3, 4)

        # Act
        z.conjugate()
        actual = z

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when adding the two."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


"""
Test case 7 (6. Negation):
Points: 2
"""


class ComplexNumberNegationUnitTests(unittest.TestCase):
    def test_negation(self):
        # Arrange
        z = ComplexNumber(5, -3)
        expected = ComplexNumber(-5, 3)

        # Act
        actual = -z

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)
        self.assertEqual(ComplexNumber, type(actual))

    def test_double_negation(self):
        # Arrange
        z = ComplexNumber(5, -3)
        expected = z

        # Act
        actual = -(-z)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_original_not_modified(self):
        # Arrange
        z = ComplexNumber(3, 4)
        expected = ComplexNumber(3, 4)

        # Act
        -z
        actual = z

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when adding the two."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


"""
Test case 8 (7a. Sum):
Points: 2
"""


class ComplexNumberSumUnitTests(unittest.TestCase):
    def test_sum(self):
        # Arrange
        z = ComplexNumber(300, 800)
        w = ComplexNumber(1, -2)
        expected = ComplexNumber(301, 798)

        # Act
        actual = z + w

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)
        self.assertEqual(ComplexNumber, type(actual))

    def test_left_operand_not_modified(self):
        # Arrange
        z = ComplexNumber(300, 800)
        w = ComplexNumber(1, -2)
        expected = ComplexNumber(300, 800)

        # Act
        z + w
        actual = z

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when adding the two."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)

    def test_right_operand_not_modified(self):
        # Arrange
        z = ComplexNumber(300, 800)
        w = ComplexNumber(1, -2)
        expected = ComplexNumber(1, -2)

        # Act
        z + w
        actual = w

        # Assert
        message = f"\n\nSecond vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when adding the two."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


"""
Test case 9 (7b. Difference):
Points: 2
"""


class ComplexNumberDifferenceUnitTests(unittest.TestCase):
    def test_difference(self):
        # Arrange
        z = ComplexNumber(300, 800)
        w = ComplexNumber(1, -2)
        expected = ComplexNumber(299, 802)

        # Act
        actual = z - w

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)
        self.assertEqual(ComplexNumber, type(actual))

    def test_left_operand_not_modified(self):
        # Arrange
        z = ComplexNumber(300, 800)
        w = ComplexNumber(1, -2)
        expected = ComplexNumber(300, 800)

        # Act
        z - w
        actual = z

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when adding the two."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)

    def test_right_operand_not_modified(self):
        # Arrange
        z = ComplexNumber(300, 800)
        w = ComplexNumber(1, -2)
        expected = ComplexNumber(1, -2)

        # Act
        z - w
        actual = w

        # Assert
        message = f"\n\nSecond vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when adding the two."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


"""
Test case 10 (7c. Product):
Points: 3
"""


class ComplexNumberProductUnitTests(unittest.TestCase):
    def test_product(self):
        # Arrange
        z = ComplexNumber(300, 800)
        w = ComplexNumber(1, -2)
        expected = ComplexNumber(1900, 200)

        # Act
        actual = z * w

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)
        self.assertEqual(ComplexNumber, type(actual))

    def test_left_operand_not_modified(self):
        # Arrange
        z = ComplexNumber(300, 800)
        w = ComplexNumber(1, -2)
        expected = ComplexNumber(300, 800)

        # Act
        z * w
        actual = z

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when adding the two."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)

    def test_right_operand_not_modified(self):
        # Arrange
        z = ComplexNumber(300, 800)
        w = ComplexNumber(1, -2)
        expected = ComplexNumber(1, -2)

        # Act
        z * w
        actual = w

        # Assert
        message = f"\n\nSecond vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when adding the two."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


"""
Test case 11 (8a. Inverse):
Points: 3
"""


class ComplexNumberInverseUnitTests(unittest.TestCase):
    def test_inverse(self):
        # Arrange
        z = ComplexNumber(4, 3)
        expected = ComplexNumber(0.16, -0.12)

        # Act
        actual = z.inverse()

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)
        self.assertEqual(ComplexNumber, type(actual))

    def test_double_inverse(self):
        # Arrange
        z = ComplexNumber(4, 3)
        expected = z

        # Act
        actual = z.inverse().inverse()

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_original_not_modified(self):
        # Arrange
        z = ComplexNumber(3, 4)
        expected = ComplexNumber(3, 4)

        # Act
        z.inverse()
        actual = z

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when adding the two."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


"""
Test case 12 (8b. Division):
Points: 2
"""


class ComplexNumberDivisionUnitTests(unittest.TestCase):
    def test_division(self):
        # Arrange
        z = ComplexNumber(4, 3)
        ONE = ComplexNumber(1)
        expected = ComplexNumber(0.16, -0.12)

        # Act
        actual = ONE / z

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)
        self.assertEqual(ComplexNumber, type(actual))

    def test_left_operand_not_modified(self):
        # Arrange
        z = ComplexNumber(300, 800)
        w = ComplexNumber(1, -2)
        expected = ComplexNumber(300, 800)

        # Act
        z / w
        actual = z

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when adding the two."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)

    def test_right_operand_not_modified(self):
        # Arrange
        z = ComplexNumber(300, 800)
        w = ComplexNumber(1, -2)
        expected = ComplexNumber(1, -2)

        # Act
        z / w
        actual = w

        # Assert
        message = f"\n\nSecond vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when adding the two."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


if __name__ == "__main__":
    unittest.main()
