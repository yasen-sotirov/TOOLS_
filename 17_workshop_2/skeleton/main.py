
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()


# CreateShampoo MyMan Trashy 10.99 Men 1000 Every_Day
# CreateToothpaste White Expensive 10.99 Men calcium,fluorid
# CreateCategory Shampoos
# CreateCategory Toothpastes
# AddToCategory Shampoos MyMan
# AddToCategory Toothpastes White
# AddToShoppingCart MyMan
# AddToShoppingCart White
# ShowCategory Shampoos
# ShowCategory Toothpastes
# TotalPrice
# RemoveFromCategory Shampoos MyMan
# ShowCategory Shampoos
# RemoveFromShoppingCart MyMan
# TotalPrice
# End