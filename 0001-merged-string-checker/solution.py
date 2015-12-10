import unittest

def mergedstringchecker(str, part1, part2):
    return True


class MergedStringCheckerTest(unittest.TestCase):

    def test_when_all_strings_are_empty_it_should_return_true(self):
        result = mergedstringchecker("", "", "")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
