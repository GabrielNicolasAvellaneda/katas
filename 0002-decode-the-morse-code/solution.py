import unittest

def decode_char(coded_char):
    MORSE_CODE = {
        ".-" : "A",
        "." : "E"
            }
    return MORSE_CODE[coded_char]

""" https://en.wikipedia.org/wiki/Morse_code """
def decode_morse(morseCode):
    char = decode_char(morseCode)
    return char 

class DecodeMorseCodeTest(unittest.TestCase):

    def test_morse_code_decoding(self):
        result = decode_morse(".-")
        self.assertEqual("A", result) 
        result = decode_morse(".")
        self.assertEqual("E", result)
        #result = decode_morse(".... . -.--   .--- ..- -.. .")
        #self.assertEqual("HEY JUDE", result) 

if __name__ == "__main__":
    unittest.main()
