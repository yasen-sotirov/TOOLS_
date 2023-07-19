
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()


# CreateCream MyWoman OhGood 9.99 Women vanilla
# CreateCategory Creams
# AddToCategory Cream MyWoman
# AddToShoppingCart MyWoman
# ShowCategory Cream
# TotalPrice
# RemoveFromCategory Cream MyWoman
# ShowCategory MyWoman
# RemoveFromShoppingCart MyWoman
# TotalPrice
# End

