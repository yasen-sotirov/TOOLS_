class First:
    def __init__(self, param_1:int, param_2:int):
        self.param_1 = param_1
        self.param_2 = param_2

    def sum_param(self):
        return f"{self.param_1} +++ {self.param_2}"

    def __str__(self) -> str:
        return f"param_1= {self.param_1}, param_2= {self.param_2}"


class Second:
    def __init__(self, pa_3, pa_4):
        self.param_3 = pa_3
        self.param_4 = pa_4

    def substract_num(self):
        return self.param_4 - 1

    def __str__(self) -> str:
        return f"param_3= {self.param_3}, param_4= {self.param_4}"

a = 5
object_1 = First(1, 2)
object_2 = Second(object_1, 4)

# print(object_2)
print(object_2.param_3.sum_param)
        


