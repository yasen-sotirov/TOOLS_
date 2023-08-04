
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

# създава обект, инстанция на APP Data
app_data = ApplicationData()

# създава обект инстанция на Command factory с параметрите на обекта инст. на App Data
cmd_factory = CommandFactory(app_data)

# създава обект, който носи атрибутите на cmd_factory  и app_data
engine = Engine(cmd_factory)

# използва метода start на обекта engine
# engine.start()      # препраща към engine.py


print(type(app_data))
# CreateCategory Shampoos