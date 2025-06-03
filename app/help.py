from logger import Logger

class Helper:
    def __init__(self):
        self.logger = Logger()
        self.bold = self.logger.bold
        self.white = self.logger.white
        self.blue = self.logger.blue
        self.reset = self.logger.reset
    def help(self):
        
        print(f"""
{self.bold}{self.white}[{self.reset}{self.bold}{self.blue}DESCRIPTION{self.reset}{self.bold}{self.white}]{self.reset}:

    {self.bold}{self.white}CVE WebApp Backend CLI tool to manage FastAPI server setup and control behavior of  database setup and running server{self.reset}

{self.bold}{self.white}[{self.reset}{self.bold}{self.blue}USAGE{self.reset}{self.bold}{self.white}]{self.reset}:

    {self.bold}{self.white}[flags]{self.reset}

{self.bold}{self.white}[{self.reset}{self.bold}{self.blue}FLAGS{self.reset}{self.bold}{self.white}]{self.reset}:

    {self.bold}{self.white}[{self.reset}{self.bold}{self.blue}SERVER OPTIONS{self.reset}{self.bold}{self.white}]{self.reset}:
        {self.bold}{self.white}-host,   --host            :  Host address to bind FastAPI server (default: 0.0.0.0)
        -port,   --port            :  Port number for FastAPI server (default: 8000)
        -reload, --reload          :  Enable auto-reload on code changes (default: True)

    {self.bold}{self.white}[{self.reset}{self.bold}{self.blue}DATABASE OPTIONS{self.reset}{self.bold}{self.white}]{self.reset}:
        {self.bold}{self.white}-sdb,    --setup-db        :  Create database schema before starting the server

    {self.bold}{self.white}[{self.reset}{self.bold}{self.blue}MISC{self.reset}{self.bold}{self.white}]{self.reset}:
        {self.bold}{self.white}-h,      --help            :  Show this help menu{self.reset}
        """)
