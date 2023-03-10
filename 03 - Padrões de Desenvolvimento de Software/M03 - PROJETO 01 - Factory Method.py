from abc import ABC, abstractmethod

class Computer(ABC):
    @property
    @abstractmethod
    def ram(self):
        pass

    @property
    @abstractmethod
    def hdd(self):
        pass

    @property
    @abstractmethod
    def cpu(self):
        pass

    @property
    @abstractmethod
    def type(self):
        pass

    def __str__(self):
        return f"{self.type} - RAM: {self.ram}GB, HD: {self.hdd}GB, CPU: {self.cpu}GHz"


class PC(Computer):
    def __init__(self, ram, hdd, cpu):
        self._ram = ram
        self._hdd = hdd
        self._cpu = cpu

    @property
    def ram(self):
        return self._ram

    @property
    def hdd(self):
        return self._hdd

    @property
    def cpu(self):
        return self._cpu

    @property
    def type(self):
        return "PC"


class Server(Computer):
    def __init__(self, ram, hdd, cpu):
        self._ram = ram
        self._hdd = hdd
        self._cpu = cpu

    @property
    def ram(self):
        return self._ram

    @property
    def hdd(self):
        return self._hdd

    @property
    def cpu(self):
        return self._cpu

    @property
    def type(self):
        return "Server"


class ComputerFactory(ABC):
    @abstractmethod
    def create_computer(self, ram, hdd, cpu):
        pass


class PCFactory(ComputerFactory):
    def create_computer(self, ram, hdd, cpu):
        return PC(ram, hdd, cpu)


class ServerFactory(ComputerFactory):
    def create_computer(self, ram, hdd, cpu):
        return Server(ram, hdd, cpu)


class Client:
    def __init__(self, factory):
        self._factory = factory

    def create_computer(self, ram, hdd, cpu):
        computer = self._factory.create_computer(ram, hdd, cpu)
        return computer


pc_factory = PCFactory()
server_factory = ServerFactory()

client = Client(pc_factory)
pc = client.create_computer(8, 500, 2.5)
print(pc)  # output: PC - RAM: 8GB, HD: 500GB, CPU: 2.5GHz

client = Client(server_factory)
server = client.create_computer

