import configparser
import os

cwd = os.getcwd()
config = configparser.ConfigParser()
config.read(cwd + '/configurations/config-real.ini')
database = config['DATABASE']['DATABASE']
host = config['DATABASE']['HOST']
user = config['DATABASE']['USER']
password = config['DATABASE']['PASSWORD']
port = config['DATABASE']['PORT']

database_type = config['DATABASE']['DATABASE_TYPE']
database_url = os.environ['DATABASE_URL']


