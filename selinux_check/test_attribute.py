import unittest
from attribute import Attribute


class TestType(unittest.TestCase):
    def setUp(self):
        self.__statement = [
            'attribute name;',
            ' attribute name ;',
            'attribute name; ',
            ' attribute name ; ',
            ]
        self.__err_statements = [
            'attribute name',
            'attribute name,',
            'attribute name;;',
            'attribute, name;',
            'attribute , name;',
            'attribute name1 name2;',
            'attribute name1, name2;',
            ]
    def test_statement_error(self):
        for statement in self.__err_statements:
            self.assertRaises(ValueError, Attribute, statement)
    def test_attribute(self):
        for statement in self.__statement:
            t = Attribute(statement)
            self.assertEqual(t.getName(), 'name')
    def test_dump_statement(self):
        for statement in self.__statement:
            t = Attribute(statement)
            self.assertEqual(t.dump_statement(), 'attribute name;')
    def test_eq(self):
        t1 = Attribute(self.__statement[0])
        for statement in self.__statement:
            t = Attribute(statement)
            self.assertEqual(t, t1)
        
        self.assertFalse(t1 == 'name')
           
        t2 = Attribute('attribute name2;')
        for statement in self.__statement:
            t = Attribute(statement)
            self.assertTrue(t != t2)
        
            
if __name__ == '__main__':
    unittest.main()