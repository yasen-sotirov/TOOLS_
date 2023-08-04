""" ЕНКАПСУЛАЦИЯ с Роси
- валидираме атрибутите
- ограничаваме достъпа до атрибутите

name = "Nora"
# обект от тип стринг
# state - състояние Nora (атрибути)
# behavior - всички операции които са свързани с обектите от типа стринг

"""

class Car:
    def __init__(self, seats: int, model: str, horse_power: int, extras: list):   # инициализираме атрибутите
        # state
        self.seats = seats          # атрибут
        self._model = model         # podqertavkata podskazva хидден atribut
        self.horse_power = horse_power
        self._extras = extras

        # behavior
        # method - работи само за класа
    def upgrade(self, new_power):
        self.horse_power = new_power
        
    @property       # getter - получава инфо за модела
    def model(self):
        return self._model      # кръстен е по различен начин от атрибута

    @model.setter   #
    def model(self, value):
        if type(value) != str:
            raise ValueError("Must be string")
        # if str(value) != value:
        #     raise  ValueError("Must be string")
        # валидация през сетъра
        # if not isinstance(value, str):
        #     raise ValueError("Must be string")
        self._model = value

    @property   # без setter
    def extras(self):
        return self._extras


# енкапсулираме с class
# za da може едно нещо да е обект то трябва да има state И бехавиор - атрибути и обекти


# обект които има state  и behavior
# hints  - само подсказка, не са реална валидация и няма да вдигне грешка ако не ги изпълним
car_1 = Car(6, "Volga", 250, ["tuning"])
car_2 = Car(6, "Zafira", 250, [])
print(f"Model: {car_1.model} with {car_1.seats} seats and {car_1.horse_power} hp")

car_1.upgrade(150)      # презаписваме state в атрибута
print(f"Model: {car_1.model} with {car_1.seats} seats and {car_1.horse_power} hp")

# print(car_1 == car_2)   # False
# print(car_1.model == car_2.model)   # True


# PROPER
# ползваме ги за да контролираме какво подаваме към външните програми
# getter - правим го за да вземем информация
# setter - правим го за да я променя. не може да го имаме самостоятелно без getter
# read - only property ?
# с подчертавката казваме че тези данни не искаме да се ползват извън класа

car_1.model = "Niva"

# атрибутите и сетърите трябва да се казват по различен начин
# изпада в рекурсия. по конвенция към атрибута слагаме "_"

# със сетъра може да правим валидация. Примерно дали винаги е стринг

# гетърите и сетърите (спрямо обикновенните методи) ?? ами не знае
# подсказва ни че не трябва да правим промени, но ако ги правим са си на наша отговорност
# май са само syntax sugar

# getter без setter e read-only вади инфо, което не може да се променя

if "Vloga" in Car.model:
    print(True)
else:
    print(False)