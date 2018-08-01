#!/usr/bin/env python3

import os
import subprocess


CmdInfoDebugEnable = False

class CmdInfo():
    def __init__(self, directory, cmd, timeout=None):
        self.__direcotry = directory
        self.__cmd = cmd
        self.__timeout = timeout
    def run(self):
        if CmdInfoDebugEnable:
            self.dump()
            return
        current_directory = os.getcwd()
        os.chdir(self.__direcotry)
        if callable(self.__cmd):
            self.__cmd()
        else:
            try:
                subprocess.run(self.__cmd, shell=True, cwd=self.__direcotry, timeout=self.__timeout)
            except AttributeError:
                subprocess.call(self.__cmd, shell=True, cwd=self.__direcotry, timeout=self.__timeout)
        os.chdir(current_directory)
    def dump(self):
        print('CmdInfo{{dir: {}\tcmd: {}}}'.format(self.__direcotry, self.__cmd))


class ProjectBuild():
    def __init__(self, updatecmdlist = None, copycmdlist = None, buildcmdlist = None):
        if updatecmdlist:
            self.UpdataCode(updatecmdlist)
        if copycmdlist:
            self.CopyCode(copycmdlist)
        if buildcmdlist:
            self.Build(buildcmdlist)
    def UpdataCode(self, cmdlist):
        self.__updatecode_cmd = cmdlist
    def CopyCode(self, cmdlist):
        self.__copycode_cmd = cmdlist
    def Build(self, cmdlist):
        self.__build_cmd = cmdlist
    def __run_cmdlist(self, cmdlist):
        if isinstance(cmdlist, list):
            for cmd in cmdlist:
                cmd.run()
        else:
            cmd = cmdlist
            cmd.run()
    def run(self):
        self.__run_cmdlist(self.__updatecode_cmd)
        self.__run_cmdlist(self.__copycode_cmd)
        self.__run_cmdlist(self.__build_cmd)

class dailybuild_P(ProjectBuild):
    def __init__(self):
        self.UpdataCode([CmdInfo('./', 'ls'), CmdInfo('./', 'ls')])
        self.CopyCode(CmdInfo('./', 'ls'))
        self.Build(CmdInfo('./', 'ls'))

if __name__ == '__main__':
    task = dailybuild_P()
    task.run()
    