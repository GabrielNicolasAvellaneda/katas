import unittest
import string

""" https://en.wikipedia.org/wiki/Morse_code """
def decode_morse_char(coded_char):
    MORSE_CODE_TABLE = {
        ".-"    : "A",
        "-..."  : "B",
        "-.-."  : "C",
        "."     : "E",
        "-.."   : "D",
        "..-."  : "F",
        "--."   : "G",
        "...."  : "H",
        ".."    : "I",
        ".----" : "J",
        "-.-"   : "K",
        ".-.."  : "L",
        "--"    : "M",
        "-."    : "N",
        "---"   : "O",
        ".--."  : "P",
        "--.-"  : "Q",
        ".-."   : "R",
        "..."   : "S",
        "-"     : "T",
        "..-"   : "U",
        "...-"  : "V",
        ".--"   : "W",
        "-..-"   : "X",
        "-.--"  : "Y",
        "--.."  : "Z",
        ".----" : "1",
        "..---" : "2",
        "...--" : "3",
        "....-" : "4",
        "....." : "5",
        "-...." : "6",
        "--..." : "7",
        "---.." : "8",
        "----." : "9",
        "-----" : "0"
        }
    return MORSE_CODE_TABLE[coded_char]

def abstract_decode(coded_string, separator_str, translator, join_str):
    parts = coded_string.split(separator_str)
    translated = map(translator, parts)
    return string.join(translated, join_str)

def decode_morse_word(morse_word):
    return abstract_decode(morse_word, " ", decode_morse_char, "")

def decode_morse(morse_code):
    return abstract_decode(morse_code, "   ", decode_morse_word, " ")

class DecodeMorseCodeTest(unittest.TestCase):

    def test_morse_code_decoding_a_single_char(self):
        result = decode_morse(".-")
        self.assertEqual("A", result) 
        result = decode_morse(".")
        self.assertEqual("E", result)

    def test_morse_code_decoding_a_word(self):
        result = decode_morse(".... . -.--")
        self.assertEqual("HEY", result) 
        result = decode_morse("... --- ...")
        self.assertEqual("SOS", result)

    def test_morse_code_decoding_multiple_words(self):
        result = decode_morse(".... . -.--   -.. ..- -.. .")
        self.assertEqual("HEY DUDE", result) 

    def test_morse_code_decoding_numbers(self):
        result = decode_morse(".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----")
        self.assertEqual("1234567890", result)

if __name__ == "__main__":
    unittest.main()
