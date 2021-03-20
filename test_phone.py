import pytest
import os
import subprocess

def files():
    return os.listdir('phone/')

@pytest.mark.parametrize("arg", os.listdir('phone/'))
def test_binary_in_phone_directory(arg):
    print("test ", arg)
    cmd = subprocess.run("./phone/"+arg, capture_output=True, shell=True, timeout=300)
    print(cmd.stdout.decode())
    assert cmd.returncode == 0
