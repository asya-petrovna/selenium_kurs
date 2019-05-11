# -*- coding: utf-8 -*-
from googletrans import Translator
import unittest
from parameterized import parameterized

class TranslatorTest(unittest.TestCase):

    @parameterized.expand([
        ['to exude', 'de', 'ausstrahlen', 'en-de translation'],
        ['a women', 'de', 'eine Frau', 'en-de indef articles'],
        ['the woman', 'de', 'die Frau', 'en-de def articles'],
        ['the women', 'de', 'die Frauen', 'en-de  plural'],
        ['женщина', 'de', 'eine Frau', 'ru-de indef article']
    ])
    def test_is_google_translate_ok(self, word, dest_language, expected_translation, name):
        translator = Translator()
        translation = translator.translate(word, dest=dest_language)
        print(translation)
        self.assertEqual(expected_translation, translation.text, msg=name)


if __name__ == '__main__':
    unittest.main()
