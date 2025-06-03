from logger import Logger
import argparse

class CLI:
    def __init__(self) -> None:
        self.logger = Logger()
        self.parser = argparse.ArgumentParser(add_help=False, usage=argparse.SUPPRESS,exit_on_error=False)
        self.parsed = None
        
    def cli(self):
        self.parser.add_argument("-host", "--host", type=str, default="0.0.0.0")
        self.parser.add_argument("-port", "--port", type=int, default=8000)
        self.parser.add_argument("-reload", "--reload", action="store_true", default=True)
        self.parser.add_argument("-sdb", "--setup-db", action="store_true", default=False)
        self.parser.add_argument("-h", "--help", action="store_true", default=False)
        self.parsed = self.parser.parse_args()
        return self.parser.parse_args()