import unittest

from stringset import StringSet

"""
Unit tests:

Test case 1:
Points: 6
"""


class CodingRoomsUnitTests(unittest.TestCase):
    def test_constructor_and_string_representation(self):
        # Arrange
        test_input = "word1 word2 word3 word2"
        expected = "word1 word2 word3"

        # Act
        set1 = StringSet(test_input)
        actual = str(set1)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


"""
Test case 2:
Points: 6
"""


class CodingRoomsUnitTests(unittest.TestCase):
    def test_union(self):
        # Arrange
        set1 = StringSet("word1 word2 word3 word2 word1 word4")
        set2 = StringSet("word2 word5 word4 word6 word7 word3")
        expected = "word1 word2 word3 word4 word5 word6 word7"

        # Act
        set3 = set1 + set2
        actual = str(set3)

        # Assert
        message = f"\n\nInput:\n{str(set1)} ({type(set1)})\n{str(set2)} ({type(set2)})"
        message += f"\n\nExpected string representation of union ({type(expected)}):\n{expected}"
        message += (
            f"\n\nActual string representation of union ({type(actual)}):\n{actual}"
        )
        self.assertEqual(expected, actual, message)

    def test_union_preserves_input_order(self):
        # Arrange
        set1 = StringSet("word2 word5 word4 word6 word7 word3")
        set2 = StringSet("word1 word2 word3 word2 word1 word4")
        expected = "word2 word5 word4 word6 word7 word3 word1"

        # Act
        set3 = set1 + set2
        actual = str(set3)

        # Assert
        message = f"\n\nInput:\n{str(set1)} ({type(set1)})\n{str(set2)} ({type(set2)})"
        message += f"\n\nExpected string representation of union ({type(expected)}):\n{expected}"
        message += (
            f"\n\nActual string representation of union ({type(actual)}):\n{actual}"
        )
        self.assertEqual(expected, actual, message)


"""
Test case 3:
Points: 6
"""


class CodingRoomsUnitTests(unittest.TestCase):
    def test_size(self):
        # Arrange
        test_input = "word1 word2 word3 word2 word1 word4"
        expected = 4

        # Act
        set1 = StringSet(test_input)
        actual = set1.size()

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


"""
Test case 4:
Points: 6
"""


class CodingRoomsUnitTests(unittest.TestCase):
    def test_indexing(self):
        # Arrange
        test_input = "word1 word2 word1 word3 word2 word1 word4"
        expected = "word3"

        # Act
        set1 = StringSet(test_input)
        actual = set1.at(2)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


"""
Test case 5:
Points: 6
"""


class CodingRoomsUnitTests(unittest.TestCase):
    def test_find(self):
        # Arrange
        test_input = "word1 word2 word3 word2 word1 word4"
        expected = True

        # Act
        set1 = StringSet(test_input)
        actual = set1.find("word2")

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)
        self.assertTrue(actual, message)

    def test_find_not_found(self):
        # Arrange
        test_input = "word1 word2 word3 word2 word1 word4"
        expected = False

        # Act
        set1 = StringSet(test_input)
        actual = set1.find("word5")

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)
        self.assertFalse(actual, message)


if __name__ == "__main__":
    unittest.main()
