from models_nai_malkite_elementi_na_programata.pakage import Package
from map_info.locations import Locations
from errors.invalid_location_error import InvalidLocationError

"""
съдържа информация кой пакет в кой град се намира
метод за добавяне на пакетите към конкретните градове
метод за преглед на пакетите в отделните градове
"""

class ApplicationData:
    # този клас няма атрибути, ползваме го само заради методите му
    # тъй като класа няма конструктор, ако направим инстанция от него,
    # тя ще подкара долните редове

    _not_assigned_packages_SYD: list[Package] = []
    _not_assigned_packages_MEL: list[Package] = []
    _not_assigned_packages_ADL: list[Package] = []
    _not_assigned_packages_ASP: list[Package] = []
    _not_assigned_packages_BRI: list[Package] = []
    _not_assigned_packages_DAR: list[Package] = []
    _not_assigned_packages_PER: list[Package] = []

    _all_packages: list[Package] = []

    def add_package_to_system(self, package: Package):
        # поема новосъздаденият пакет обект и го слага в лист хранилище
        if package.start_location == "SYDNEY":
            self._not_assigned_packages_SYD.append(package)
            self._all_packages.append(package)

        elif package.start_location == "MELBOURNE":
            self._not_assigned_packages_MEL.append(package)
            self._all_packages.append(package)

        elif package.start_location == "ADELAIDE":
            self._not_assigned_packages_ADL.append(package)
            self._all_packages.append(package)

        elif package.start_location == "ALICE_SPRING":
            self._not_assigned_packages_SYD.append(package)
            self._all_packages.append(package)

        elif package.start_location == "BRISBANE":
            self._not_assigned_packages_BRI.append(package)
            self._all_packages.append(package)

        elif package.start_location == "DARWIN":
            self._not_assigned_packages_DAR.append(package)
            self._all_packages.append(package)

        elif package.start_location == "PERTH":
            self._not_assigned_packages_PER.append(package)
            self._all_packages.append(package)

        return (f"New package has been created successfully. The Package ID is {package.package_id}. "
                f"The package is located in {package.start_location.capitalize()} department")



    def view_package(self, location: str):
        try:
            # проверява дали зададеният аргумент го има в списъка с градове по Enum
            _ = Locations(location.upper())
        except:
            raise InvalidLocationError(f"This location is not supported")


        if location.upper() == "SYDNEY":
            spacer = "\n"
            if len(self.not_assigned_packages_SYD) == 0:
                # връщаме грешката, за да се върне до engine
                return f"There is no packages in {location.capitalize()} department."
            else:
                return spacer.join([f"Department: [{location}]\n"
                                   f" - total amount of packages: {len(self.not_assigned_packages_SYD)}"])


        if location.upper() == "MELBOURNE":
            spacer = "\n"
            if len(self.not_assigned_packages_MEL) == 0:
                # връщаме грешката, за да се върне до engine
                return f"There is no packages in {location.capitalize()} department."
            else:
                return spacer.join([f"Department: [{location}]\n"
                                   f" - total amount of packages: {len(self.not_assigned_packages_SYD)}"])


        if location.upper() == "ADELAIDE":
            spacer = "\n"
            if len(self.not_assigned_packages_ADL) == 0:
                # връщаме грешката, за да се върне до engine
                return f"There is no packages in {location.capitalize()} department."
            else:
                return spacer.join([f"Department: [{location}]\n"
                                   f" - total amount of packages: {len(self.not_assigned_packages_SYD)}"])


        if location.upper() == "ALICE_SPRINGS":
            spacer = "\n"
            if len(self.not_assigned_packages_ASP) == 0:
                # връщаме грешката, за да се върне до engine
                return f"There is no packages in {location.capitalize()} department."
            else:
                return spacer.join([f"Department: [{location}]\n"
                                   f" - total amount of packages: {len(self.not_assigned_packages_SYD)}"])


        if location.upper() == "BRISBANE":
            spacer = "\n"
            if len(self.not_assigned_packages_BRI) == 0:
                # връщаме грешката, за да се върне до engine
                return f"There is no packages in {location.capitalize()} department."
            else:
                return spacer.join([f"Department: [{location}]\n"
                                   f" - total amount of packages: {len(self.not_assigned_packages_SYD)}"])


        if location.upper() == "DARWIN":
            spacer = "\n"
            if len(self.not_assigned_packages_DAR) == 0:
                # връщаме грешката, за да се върне до engine
                return f"There is no packages in {location.capitalize()} department."
            else:
                return spacer.join([f"Department: [{location}]\n"
                                   f" - total amount of packages: {len(self.not_assigned_packages_SYD)}"])


        if location.upper() == "PERTH":
            spacer = "\n"
            if len(self.not_assigned_packages_PER) == 0:
                # връщаме грешката, за да се върне до engine
                return f"There is no packages in {location.capitalize()} department."
            else:
                return spacer.join([f"Department: [{location}]\n"
                                   f" - total amount of packages: {len(self.not_assigned_packages_SYD)}"])











