from struct import iter_unpack

from homework.hw2.decrypt import decrypt
import unittest


class TestDecrypt(unittest.TestCase):
    def test_decrypt(self):
        self.assertTrue(decrypt('абрау...-кадабра') == 'абра-кадабра')
        self.assertTrue(decrypt('абра-кадабра.') == 'абра-кадабра')
        self.assertTrue(decrypt('абраа..-кадабра') == 'абра-кадабра')
        self.assertTrue(decrypt('абра--..кадабра') == 'абра-кадабра')
        self.assertTrue(decrypt('абраа..-.кадабра') == 'абра-кадабра')
        self.assertTrue(decrypt('1..4.5') == '45')
        self.assertTrue(decrypt('3.................') == '')
