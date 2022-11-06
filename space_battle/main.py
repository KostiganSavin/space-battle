import sys
from collections import defaultdict
from curses.ascii import SO
from typing import Callable
from abc import ABC, abstractmethod
from queue import Queue
import logging

commands_queue = Queue()


class AbstractCommand(ABC):
                 
    @abstractmethod
    def execute(self):
        ...


class ExceptionHandler:
    _handlers: dict[AbstractCommand, dict[Exception, Callable]] = defaultdict()

    def setup(self, cmd: AbstractCommand, exc: Exception, func: Callable) -> None:
        self._handlers[cmd] = {exc: func}
        print(f"HANDLERS: {self._handlers} ")

    def handle(self, cmd: AbstractCommand, exc: Exception, q: Queue):
        # print(f"Got: cmd: {cmd}, exc: {exc}, queue: {q}")
        # print(f"CMD: {cmd.__class__}")
        func = self._handlers[cmd.__class__][exc.__class__]
        func(cmd, exc, q)


exception_handler = ExceptionHandler()


class Log(AbstractCommand):

    def __init__(self, cmd: AbstractCommand, exc: Exception) -> None:
        self.cmd = cmd
        self.exc = exc

    def execute(self):
        print(f"Executing comand with {self.__class__}")
        print(f"Exception: {self.exc} happend while executing: {self.cmd} command")


def log_cmd(cmd: AbstractCommand, exc: Exception, q: Queue):
    q.put(Log(cmd=cmd, exc=exc))


class PreRetryComand(AbstractCommand):

    def __init__(self, cmd: AbstractCommand, exc: Exception) -> None:
        self.cmd = cmd

    def execute(self):
        print(f"Executing comand with {self.__class__}")
        self.cmd.execute()


def pre_retry_cmd(cmd: AbstractCommand, exc: Exception, q: Queue):
    q.put(PreRetryComand(cmd=cmd, exc=exc))


class RetryComand(AbstractCommand):

    def __init__(self, cmd: AbstractCommand, exc: Exception) -> None:
        self.cmd = cmd

    def execute(self):
        print(f"Executing comand with {self.__class__}")
        self.cmd.execute()


def retry_cmd(cmd: AbstractCommand, exc: Exception, q: Queue):
    q.put(RetryComand(cmd=cmd, exc=exc))


class SomeCommand(AbstractCommand):

    def execute(self):
        print(f"Executing comand with {self.__class__}")
        raise ValueError


def main():
    print("Start...")

    exception_handler.setup(cmd=SomeCommand, exc=ValueError, func=pre_retry_cmd)

    exception_handler.setup(cmd=PreRetryComand, exc=ValueError, func=retry_cmd)
    
    exception_handler.setup(cmd=RetryComand, exc=ValueError, func=log_cmd)

    commands_queue.put(SomeCommand())


    while not commands_queue.empty():
        cmd = commands_queue.get()
        try:
            cmd.execute()
        except Exception as exc:
            exception_handler.handle(cmd=cmd, exc=exc, q=commands_queue)


if  __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stop executing")
        sys.exit()