import unittest
from type import Type


class TestType(unittest.TestCase):
    def setUp(self):
        self.__statement1 = [
            'type name, attri1;',
            ' type name,attri1 ;',
            'type name , attri1; ',
            ' type name ,attri1 ; ',
            ]
        self.__statement2 = [
            'type name, attri1, attri2;',
            ' type name,attri1,attri2 ;',
            'type name, attri1 ,attri2; ',
            ' type name ,attri1, attri2 ; ',
            ]
        self.__statement3 = [
            'type name, attri1, attri2, attri3;',
            ' type name,attri1,attri2,attri3 ;',
            'type name ,attri1, attri2 ,attri3; ',
            ' type name, attri1 ,attri2, attri3 ; ',
            ]
        self.__err_statements = [
            'type name, attri1',
            'type name,, attri1;',
            'name, attri1',
            'type name attri1;',
            'type, name attri1;',
            'type name, attri1, attri2',
            'type name, attri1 attri2;',
            'type name,, attri1, attri2;',
            'type, name, attri1 attri2;',
            'name, attri1, attri2',
            'type name, attri1, attri2, attri3',
            'name, attri1, attri2, attri3',
            'type name, attri1, attri2 attri3;',
            'type, name, attri1, attri2 attri3;',
            'type name, attri1, attri2,, attri3;',
            ]
    def test_statement_error(self):
        for statement in self.__err_statements:
            self.assertRaises(ValueError, Type, statement)
    def test_type(self):
        for statement in self.__statement1:
            t = Type(statement)
            self.assertEqual(t.getName(), 'name')
            self.assertEqual(t.getAttributes(), ['attri1'])
        for statement in self.__statement2:
            t = Type(statement)
            self.assertEqual(t.getName(), 'name')
            self.assertEqual(t.getAttributes(), ['attri1', 'attri2'])
        for statement in self.__statement3:
            t = Type(statement)
            self.assertEqual(t.getName(), 'name')
            self.assertEqual(t.getAttributes(), ['attri1', 'attri2', 'attri3'])
    def test_dump_statement(self):
        for statement in self.__statement1:
            t = Type(statement)
            self.assertEqual(t.dump_statement(), 'type name, attri1;')
        for statement in self.__statement2:
            t = Type(statement)
            self.assertEqual(t.dump_statement(), 'type name, attri1, attri2;')
        for statement in self.__statement3:
            t = Type(statement)
            self.assertEqual(t.dump_statement(), 'type name, attri1, attri2, attri3;')
    def test_eq(self):
        t1 = Type(self.__statement1[0])
        for statement in self.__statement1:
            t = Type(statement)
            self.assertEqual(t, t1)
        for statement in self.__statement2:
            t = Type(statement)
            self.assertEqual(t, t1)
        for statement in self.__statement3:
            t = Type(statement)
            self.assertEqual(t, t1)
        
        self.assertFalse(t1 == 'name')
           
        t2 = Type('type name2, attri1, attri2;')
        for statement in self.__statement1:
            t = Type(statement)
            self.assertTrue(t != t2)
        for statement in self.__statement2:
            t = Type(statement)
            self.assertTrue(t != t2)
        for statement in self.__statement3:
            t = Type(statement)
            self.assertTrue(t != t2)
    def test_hasAttribute(self):
        for statement in self.__statement1:
            t = Type(statement)
            self.assertTrue(t.hasAttribute('attri1'))
            self.assertFalse(t.hasAttribute('attri2'))
            self.assertFalse(t.hasAttribute('attri3'))
        for statement in self.__statement2:
            t = Type(statement)
            self.assertTrue(t.hasAttribute('attri1'))
            self.assertTrue(t.hasAttribute('attri2'))
            self.assertFalse(t.hasAttribute('attri3'))
        for statement in self.__statement3:
            t = Type(statement)
            self.assertTrue(t.hasAttribute('attri1'))
            self.assertTrue(t.hasAttribute('attri2'))
            self.assertTrue(t.hasAttribute('attri3'))
            self.assertFalse(t.hasAttribute('attri4'))
        
            
if __name__ == '__main__':
    unittest.main()
                
            