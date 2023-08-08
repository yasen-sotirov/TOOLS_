welcome_screen = """
    ___              __             ___            __                _      __  _
   /   | __  _______/ /__________ _/ (_)___ _     / /   ____  ____ _(_)____/ /_(_)____
  / /| |/ / / / ___/ __/ ___/ __ `/ / / __ `/    / /   / __ \/ __ `/ / ___/ __/ / ___/
 / ___ / /_/ (__  ) /_/ /  / /_/ / / / /_/ /    / /___/ /_/ / /_/ / (__  ) /_/ / /__
/_/  |_\__,_/____/\__/_/   \__,_/_/_/\__,_/    /_____/\____/\__, /_/____/\__/_/\___/
                                                           /____/
                    WELCOME


    Please, type a command and parameters:

CreateDeliveryPackage start_location, end_location, weight, customer_first_name, customer_last_name, customer_email, customer_phone_number
ViewPackages location
CreateDeliveryRoute
SearchRoute
AssignTruckToDeliveryRoute
AssignPackageToDeliveryRoute
ViewRoutes
ViewTrucks
"""

print(welcome_screen)