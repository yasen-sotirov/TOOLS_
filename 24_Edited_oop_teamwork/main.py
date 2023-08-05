from core.app_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine_start import Engine

"""
Сглабя отделните класове и подава на engine
"""


app_data = ApplicationData()
# съсздаденият обект има методи, които могат да бъдат изпълнени
# app_data.add_package_to_system()
# app_data.view_package()

cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()


