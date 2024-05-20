import configparser
import sys, os

def set_current_directory():
    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        application_path = os.path.abspath(sys.executable)
    elif __file__:
        application_path = os.path.abspath(__file__)
    directory = os.path.dirname(application_path)
    # set current directory
    os.chdir(directory)
    return directory

def getConfig(section: str):
    config = configparser.ConfigParser()
    config.read(set_current_directory() + '\\..\\config\\server.ini', encoding='utf-8')
    connection = config[section]
    return connection