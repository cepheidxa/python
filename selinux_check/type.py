import re


type_nameformat_str = '[0-9a-zA-Z_]+'
type_nameformat = re.compile(type_nameformat_str)
type_format = re.compile('\s*type\s+({0}\s*,\s*)+{0}\s*;\s*'.format(type_nameformat_str))


class Type():
    def __init__(self, statement):
        if not re.fullmatch(type_format, statement):
            raise ValueError('type statement error: {}'.format(statement))
        name = re.findall(type_nameformat, statement)[1:]
        self.__name = name[0]
        self.__attributes = name[1:]
    def getName(self):
        return self.__name
    def getAttributes(self):
        return self.__attributes
    def dump_statement(self):
        return 'type {}, {};'.format(self.__name,', '.join(self.__attributes))
    def __eq__(self, obj):
        if isinstance(obj, Type) and self.__name == obj.getName():
            return True
        else:
            return False
    def hasAttribute(self, attribute):
        if attribute in self.__attributes:
            return True
        else:
            return False