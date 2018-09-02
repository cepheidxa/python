import re

type_or_perm_format_str = '(([0-9a-zA-Z_]+)|({(\s*[0-9a-zA-Z_-]+\s*)+}))'

allow_rule_format = re.compile('\s*allow\s+{0}\s+{0}\s*:\s*{0}\s+{0}\s*;\s*'.format(type_or_perm_format_str))
neverallow_rule_format = re.compile('\s*neverallow\s+{0}\s+{0}\s*:\s*{0}\s+{0}\s*;\s*'.format(type_or_perm_format_str))

class _Rule():
    def __init__(self, statement, allow_rule = False, neverallow_rule = False):
        if allow_rule:
            rule_format = allow_rule_format
        elif neverallow_rule:
            rule_format = neverallow_rule_format
        else:
            raise ValueError('Either allow_rule or neverallow_rule should be set')
        
        if not re.fullmatch(rule_format, statement):
            raise ValueError('attribute statement error: {}'.format(statement))
        index = re.search(re.compile('allow'), statement).span()[1]
        #get source type
        tmp = re.search(re.compile(type_or_perm_format_str), statement[index:])
        index += tmp.span()[1]
        self.__source_statement = tmp.group(0)
        #get target type
        tmp = re.search(re.compile(type_or_perm_format_str), statement[index:])
        index += tmp.span()[1]
        self.__target_statement = tmp.group(0)
        #get class
        tmp = re.search(re.compile(type_or_perm_format_str), statement[index:])
        index += tmp.span()[1]
        self.__class_statement = tmp.group(0)
        #get perm
        tmp = re.search(re.compile(type_or_perm_format_str), statement[index:])
        index += tmp.span()[1]
        self.__perm_statement = tmp.group(0)

        self.__source_type = [x for x in re.split(re.compile('[\s{},;:]+'), self.__source_statement) if x]
        self.__target_type = [x for x in re.split(re.compile('[\s{},;:]+'), self.__target_statement) if x]
        self.__class = [x for x in re.split(re.compile('[\s{},;:]+'), self.__class_statement) if x]
        self.__perm = [x for x in re.split(re.compile('[\s{},;:]+'), self.__perm_statement) if x]
    def getSourceType(self):
        return self.__source_type
    def getTargetType(self):
        return self.__target_type
    def getClass(self):
        return self.__class
    def getPerm(self):
        return self.__perm
    def dump_statement(self):
        return 'allow {} {}:{} {};'.format(self.__source_statement, self.__target_statement, self.__class_statement, self.__perm_statement)
    
class AllowRule(_Rule):
    def __init__(self, statement):
        _Rule.__init__(self, statement, allow_rule = True)
class NerverAllowRule(_Rule):
    def __init__(self, statement):
        _Rule.__init__(self, statement, neverallow_rule = True)
