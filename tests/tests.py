import unittest
import regexEngine

class MyTest(unittest.TestCase):
    def test_matchOne(self):
        self.assertTrue(regexEngine.matchOne('a', 'a'))
        self.assertTrue(regexEngine.matchOne('.', 'z'))
        self.assertTrue(regexEngine.matchOne('', 'h'))
        self.assertFalse(regexEngine.matchOne('a', 'b'))
        self.assertFalse(regexEngine.matchOne('p', ''))


    def test_search(self):
        #self.assertTrue(regexEngine.search('a?b?c?', ''))
        self.assertTrue(regexEngine.search('a', 'abc'))
        self.assertTrue(regexEngine.search('ab', 'abc'))
        self.assertTrue(regexEngine.search('abc', 'abc'))
        self.assertTrue(regexEngine.search('bc', 'abc'))
        self.assertTrue(regexEngine.search('c', 'abc'))
        self.assertFalse(regexEngine.search('d', 'abc'))
        self.assertFalse(regexEngine.search('dc', 'abc'))

        self.assertTrue(regexEngine.search('c$','abc'))
        self.assertTrue(regexEngine.search('bc$','abc'))
        self.assertTrue(regexEngine.search('abc$', 'abc'))
        self.assertTrue(regexEngine.search('^abc', 'abc'))
        self.assertTrue(regexEngine.search('^ab', 'abc'))

        self.assertTrue(regexEngine.search('bc', 'abc'))
        self.assertTrue(regexEngine.search('c', 'abc'))

        self.assertTrue(regexEngine.search('ab?c', 'ac'))
        self.assertTrue(regexEngine.search('ab?c', 'abc'))
        self.assertTrue(regexEngine.search('a?b?c', 'abc'))

        self.assertTrue(regexEngine.search('a*', ''))
        self.assertTrue(regexEngine.search('a*', 'aaaaaaaaaaaaaa'))
        self.assertTrue(regexEngine.search('a*b', 'aaaaaaaaaaaaaab'))



if __name__ == '__main__':
    unittest.main()
