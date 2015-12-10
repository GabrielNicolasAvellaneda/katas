import unittest
import string

def decode_char(coded_char):
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
        "--.."  : "Z"
        }
    return MORSE_CODE_TABLE[coded_char]

def decode_morse_word(morse_word):
    output = []
    char_separator = " "
    for c in morse_word.split(char_separator):
        char = decode_char(c)
        output.append(char)
    return string.join(output, "")

""" https://en.wikipedia.org/wiki/Morse_code """
def decode_morse(morse_code):
    output = []
    word_separator = "   "
    for w in morse_code.split(word_separator):
        decoded_word = decode_morse_word(w)
        output.append(decoded_word)
    return string.join(output, " ") 

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

if __name__ == "__main__":
    unittest.main()
