

from core.command_factory import CommandFactory
from core.engine import Engine

cmd_factory = CommandFactory()
engine = Engine(cmd_factory)

engine.start()


"""
CreateDirectory newdir
CreateFile newdir myfile.txt
AppendText text
ReadFile myfile.txt
DeleteFile myfile.txt
ListFiles newdir
CountFiles
CountLines
exit

"""