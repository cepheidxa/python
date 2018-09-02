import re

attribute_format_str = '[0-9a-zA-Z_]+'
attribute_nameformat = re.compile(attribute_format_str)
attribute_format = re.compile('\s*attribute\s+{}\s*;\s*'.format(attribute_format_str))


class Attribute():
    def __init__(self, statement):
        if not re.fullmatch(attribute_format, statement):
            raise ValueError('attribute statement error: {}'.format(statement))
        self.__name = re.findall(attribute_nameformat, statement)[1]
    def getName(self):
        return self.__name
    def dump_statement(self):
        return 'attribute {};'.format(self.__name)
    def __eq__(self, obj):
        if isinstance(obj, Attribute) and self.__name == obj.getName():
            return True
        else:
            return False