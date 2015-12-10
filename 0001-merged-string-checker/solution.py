import unittest

def are_all_empty(str, part1, part2):
    return str == "" and part1 == "" and part2 == ""

def parts_does_not_sum_up_to_string_size(str, part1, part2):
    return (len(part1) + len(part2) - len(str)) != 0

def mergedstringchecker(str, part1, part2):
    if parts_does_not_sum_up_to_string_size(str, part1, part2):
        return False

    return mergedstringchecker2(str, part1, part2)

def mergedstringchecker2(str, part1, part2):
    if are_all_empty(str, part1, part2):
        return True

    target_char = str[0]
    target_substring = str[1:]

    if len(part1) > 0 and len(part2) > 0 and part1[0] == target_char and part2[0] == target_char:
        # This is the special case
        return mergedstringchecker2(target_substring, part1[1:], part2) or mergedstringchecker2(target_substring, part1, part2[1:])

    if len(part1) > 0 and target_char == part1[0]:
        return mergedstringchecker2(target_substring, part1[1:], part2)
    elif len(part2) > 0 and target_char == part2[0]:
        return mergedstringchecker2(target_substring, part1, part2[1:])
        
    return False
   
class MergedStringCheckerTest(unittest.TestCase):

    def test_when_all_strings_are_empty_it_should_return_true(self):
        result = mergedstringchecker("", "", "")
        self.assertTrue(result)

    def test_with_string_bigger_than_sum_of_parts(self):
        result = mergedstringchecker("abc", "a", "b")
        self.assertFalse(result)

    def test_with_string_smaller_than_sum_of_parts(self):
        result = mergedstringchecker("a","abc", "b")
        self.assertFalse(result)

    def test_with_string_and_parts_matching(self):
        result = mergedstringchecker("a", "a", "")
        self.assertTrue(result)
        result = mergedstringchecker("some string", "", "some string")
        self.assertTrue(result)
        result = mergedstringchecker("code peace", "cd pc", "oeeae")
        self.assertTrue(result)

    def test_with_string_and_parts_not_matching(self):
        result = mergedstringchecker("x", "y", "z")
        self.assertFalse(result)

    def test_with_parts_with_ambiguous_characters(self):
        result = mergedstringchecker("oaob","ob", "oa")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
