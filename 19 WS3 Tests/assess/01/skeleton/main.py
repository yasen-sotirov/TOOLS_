
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine
from models.test_group import TestGroup

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()

# addtestgroup TransactionTests
# addtest 1 ShouldWork_WhenToldTo
# addtestrun 1 fail 10
# addtestrun 1 pass 15
# addtestrun 1 fail 17
# addtestrun 1 fail 8
# testreport 1
# addtest 1 MustWork!_OnlyWhenCorrect
# addtestrun 2 pass 3
# addtestrun 2 pass 15
# addtestrun 2 fail 74
# addtestrun 2 pass 63
# viewgroup 1


