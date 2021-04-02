import argparse
import string
from base64 import b64decode, b64encode


class Cipher:

    def __init__(self, text, shift):
        for key in shift:
            self.text = text
            self.key = key

    def encode_message(self):
        result_text = ""

        for i in range(len(self.text)):
            char = self.text[i]
            if (char.isupper()):
                result_text += chr((ord(char) + int(self.key) - 65) % 26 + 65)
            elif char == ' ':
                result_text += ' '
            else:
                result_text += chr((ord(char) + int(self.key) - 97) % 26 + 97)

        print(b64encode(result_text.encode('utf-8')).decode('utf-8'))


class Decoder:

    def __init__(self, text):
        for message in text:
            self.message = b64decode(message.encode('utf-8')).decode('utf-8')

    def decode_message(self):
        for key in range(len(string.ascii_letters)):
            translated = ''
            for symbol in self.message:
                if (symbol in string.ascii_letters):
                    num = string.ascii_letters.find(symbol)
                    num -= key
                    if (num < 0):
                        num += len(string.ascii_letters)
                    translated += string.ascii_letters[num]
                else:
                    translated += symbol

            print('Hacking key #%s: %s' % (key, translated))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description='Encodes and Decodes.')

    parser.add_argument('-m', '--message',
                        nargs=1, action='store',
                        help='Encodes input text. Required Argument is key shift. (e.g. -m 3)')

    parser.add_argument('-d', '--decode',
                        nargs=1, metavar='DECODE',
                        action='store',
                        help="Brute Forces to decode a Caesar Cipher Text. (e.g. -d 'TnJza25zamM=')")
    
    args = parser.parse_args()

    if args.message:
        try:
            while True:
                message = input("Message: ")
                Cipher(message, [key for key in args.message]).encode_message()
        except KeyboardInterrupt as c:
            print('\n\nStopped!')

    if args.decode:
        Decoder([x for x in args.decode]).decode_message()