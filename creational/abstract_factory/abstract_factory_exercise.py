
import abc
from typing import Tuple


class DbConnection(abc.ABC):
    @abc.abstractmethod
    def connect(self, address: Tuple[str, int], user: str, password: str):
        pass

    @abc.abstractmethod
    def close(self):
        pass


class DbCommand(abc.ABC):
    @abc.abstractmethod
    def execute(self, connection: DbConnection):
        pass


class SqlServerConnection(DbConnection):
    def __init__(self) -> None:
        self.address = None

    def connect(self, address: Tuple[str, int], user: str, password: str):
        self.address = address
        self._credentials = (user, password)
        print(
            f'Connecting to SQLServer {address} - user {user}; password {password}... ')

    def close(self):
        print(f'Closing connection with SQLServer {self.address}')


class SqlServerCommand(DbCommand):
    def __init__(self, cmd: str) -> None:
        super().__init__()
        self._cmd = cmd

    def execute(self, connection: DbConnection):
        print(
            f'Executing SQLServer command: "{self._cmd}" using the connection to {connection.address}')


class OracleServerConnection(DbConnection):
    def __init__(self) -> None:
        self.address = None

    def connect(self, address: Tuple[str, int], user: str, password: str):
        self.address = address
        self._credentials = (user, password)
        print(
            f'Connecting to Oracle {address} - user {user}; password {password}... ')

    def close(self):
        print(f'Closing connection with Oracle {self.address}')


class OracleCommand(DbCommand):
    def __init__(self, cmd: str) -> None:
        super().__init__()
        self._cmd = cmd

    def execute(self, connection: DbConnection):
        print(
            f'Executing Oracle command: "{self._cmd}" using the connection to {connection.address}')


def main():
    conn = SqlServerConnection()
    conn.connect(('localhost', 8080), 'dev', 'pwd')

    cmd = SqlServerCommand("SELECT * FROM Products")
    cmd.execute(conn)

    conn.close()

    ###########################
    print('*' * 40)

    conn = OracleServerConnection()
    conn.connect(('localhost', 8080), 'dev', 'pwd')

    cmd = OracleCommand("SELECT * FROM Products")
    cmd.execute(conn)

    conn.close()


if __name__ == "__main__":
    main()

# TODO: Implement AbstractFactory pattern