
import subprocess
import os

def get_git_revision_hash():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD'])

def get_git_branch():
    return subprocess.check_output(['git', 'branch', '--show-current'])

def get_git_remote():
    return subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'])

def get_pip_freeze():
    return subprocess.check_output(['pip', 'freeze']).splitlines()

new_line = bytes("\n", "UTF-8")

def record_libraries(mlflow):
    """
    This method run the pip freeze command record the output as a file
    :param mlflow:
    :return:
    """
    with open("pip_freeze.txt", "wb") as file:
        for line in get_pip_freeze():
            file.write(line)
            file.write(new_line)
    file.close()
    mlflow.log_artifact("pip_freeze.txt")
    os.remove("pip_freeze.txt")