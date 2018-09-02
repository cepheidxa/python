import unittest
from rule import AllowRule, NerverAllowRule


class TestAllowRule(unittest.TestCase):
    def setUp(self):
        self.__exact__statement = [
            'allow statsd adbd:fd use;',
            'allow statsd shell:fifo_file { getattr read };',
            'allow hal_camera { appdomain -isolated_app }:fd use;',
            'allow { hal_camera_client hal_camera_server } hal_graphics_allocator:fd use;',
            ]
        self.__err_statements = [
            'allow statsd adbd:fd use',
            'allow statsd, adbd:fd use;',
            'allow statsd adbd fd use;',
            'allow statsd adbd,fd use;',
            'allow statsd adbd fd use;',
            ]
    def test_statement_error(self):
        for statement in self.__err_statements:
            try:
                self.assertRaises(ValueError, AllowRule, statement)
            except AssertionError as e:
                print('parse statement error:{}'.format(statement))
                raise e
    def test_dump_statement(self):
        for statement in self.__exact__statement:
            r = AllowRule(statement)
            self.assertEqual(r.dump_statement(), statement)
    def test_getSourceType(self):
        rule = AllowRule('allow statsd adbd:fd use;')
        self.assertEqual(rule.getSourceType(), ['statsd'])
        rule = AllowRule('allow statsd shell:fifo_file { getattr read };')
        self.assertEqual(rule.getSourceType(), ['statsd'])
        rule = AllowRule('allow hal_camera { appdomain -isolated_app }:fd use;')
        self.assertEqual(rule.getSourceType(), ['hal_camera'])
        rule = AllowRule('allow { hal_camera_client hal_camera_server } hal_graphics_allocator:fd use;')
        self.assertEqual(rule.getSourceType(), ['hal_camera_client', 'hal_camera_server'])
    def test_getTargetType(self):
        rule = AllowRule('allow statsd adbd:fd use;')
        self.assertEqual(rule.getTargetType(), ['adbd'])
        rule = AllowRule('allow statsd shell:fifo_file { getattr read };')
        self.assertEqual(rule.getTargetType(), ['shell'])
        rule = AllowRule('allow hal_camera { appdomain -isolated_app }:fd use;')
        self.assertEqual(rule.getTargetType(), ['appdomain', '-isolated_app'])
        rule = AllowRule('allow { hal_camera_client hal_camera_server } hal_graphics_allocator:fd use;')
        self.assertEqual(rule.getTargetType(), ['hal_graphics_allocator'])
    def test_getClass(self):
        rule = AllowRule('allow statsd adbd:fd use;')
        self.assertEqual(rule.getClass(), ['fd'])
        rule = AllowRule('allow statsd shell:fifo_file { getattr read };')
        self.assertEqual(rule.getClass(), ['fifo_file'])
        rule = AllowRule('allow hal_camera { appdomain -isolated_app }:fd use;')
        self.assertEqual(rule.getClass(), ['fd'])
        rule = AllowRule('allow { hal_camera_client hal_camera_server } hal_graphics_allocator:fd use;')
        self.assertEqual(rule.getClass(), ['fd'])
    def test_getPerm(self):
        rule = AllowRule('allow statsd adbd:fd use;')
        self.assertEqual(rule.getPerm(), ['use'])
        rule = AllowRule('allow statsd shell:fifo_file { getattr read };')
        self.assertEqual(rule.getPerm(), ['getattr', 'read'])
        rule = AllowRule('allow hal_camera { appdomain -isolated_app }:fd use;')
        self.assertEqual(rule.getPerm(), ['use'])
        rule = AllowRule('allow { hal_camera_client hal_camera_server } hal_graphics_allocator:fd use;')
        self.assertEqual(rule.getPerm(), ['use'])
    
    
if __name__ == '__main__':
    unittest.main()