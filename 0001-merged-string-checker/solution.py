import unittest

def are_all_empty(str, part1, part2):
    return str == "" and part1 == "" and part2 == ""

def string_empty_and_parts_non_empty(str, part1, part2):
    return str == "" and (part1 != "" or part2 != "")

def parts_does_not_sum_up_to_string_size(str, part1, part2):
    return (len(part1) + len(part2) - len(str)) != 0

def mergedstringchecker(str, part1, part2):
    if parts_does_not_sum_up_to_string_size(str, part1, part2):
        return False

    return mergedstringchecker2(str, part1, part2)

def mergedstringchecker2(str, part1, part2):
    if are_all_empty(str, part1, part2):
        return True

    if string_empty_and_parts_non_empty(str, part1, part2):
        return False

    target_char = str[0]
    target_substring = str[1:]

    if len(part1) > 0 and target_char == part1[0]:
        return mergedstringchecker2(target_substring, part1[1:], part2)
    elif len(part2) > 0 and target_char == part2[0]:
        return mergedstringchecker2(target_substring, part1, part2[1:])
        
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

    def test_with_string_bigger_than_sum_of_parts(self):
        result = mergedstringchecker("abc", "a", "b")
        self.assertFalse(result)

    def test_with_string_smaller_than_sum_of_parts(self):
        result = mergedstringchecker("a","abc", "b")
        self.assertFalse(result)

    def test_with_string_and_part_equals(self):
        result = mergedstringchecker("a", "a", "")
        self.assertTrue(result)
        result = mergedstringchecker("some string", "", "some string")
        self.assertTrue(result)

    def test_with_string_and_parts_not_matching(self):
        result = mergedstringchecker("x", "y", "z")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
