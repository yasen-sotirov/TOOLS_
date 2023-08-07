from core.app_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine_start import Engine

# Сглабя отделните класове и подава на engine

app_data = ApplicationData()
# съсздаденият обект има методи, които могат да бъдат изпълнени
# app_data.add_package_to_system()
# app_data.view_package()

cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()



"""
CreateDeliveryPackage SYDNEY MELBOURNE 1000 Ivan Ivanov ivan@abv.bg 0888999888
CreateDeliveryPackage DARWIN MELBOURNE 1000 Peter Petrov petar@abv.bg 0888111222
CreateDeliveryPackage MELBOURNE DARWIN 1000 Steven Jones steven@gmail.com 0889222333
ViewPackages SYDNEY
ViewPackages MELBOURNE
ViewPackages ADELAIDE
ViewPackages ALICE_SPRINGS
ViewPackages BRISBANE
ViewPackages DARWIN
ViewPackages PERTH
end
"""