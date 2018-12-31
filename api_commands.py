import abc
import json
import urllib
import urllib.request


class APICommandsInvoker:

    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        data = []
        index = 1
        for command in self._commands:
            x = command.execute()
            data.append(x)
            index = index+1
        return data


class Command(metaclass=abc.ABCMeta):

    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass


class GetProduct(Command):

    def execute(self):
        return self._receiver.get_product()


class APICommandsReceiver:

    def __init__(self, url):
        self._url = url

    def get_product(self):
        api_request = urllib.request.urlopen(self._url).read()
        print(json.loads(api_request))
        json_data = json.loads(api_request)
        return json_data
