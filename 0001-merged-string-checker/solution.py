import unittest

def are_all_empty(str, part1, part2):
    return str == "" and part1 == "" and part2 == ""

def string_empty_and_parts_non_empty(str, part1, part2):
    return str == "" and (part1 != "" or part2 != "")

def mergedstringchecker(str, part1, part2):
    if are_all_empty(str, part1, part2):
        return True  

    if string_empty_and_parts_non_empty(str, part1, part2):
        return False

class MergedStringCheckerTest(unittest.TestCase):

    def test_when_all_strings_are_empty_it_should_return_true(self):
        result = mergedstringchecker("", "", "")
        self.assertTrue(result)

    def test_string_empty_and_parts_not_empty(self):
        result = mergedstringchecker("", "something", "")
        self.assertFalse(result)
        
        result = mergedstringchecker("", "", "some text")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
