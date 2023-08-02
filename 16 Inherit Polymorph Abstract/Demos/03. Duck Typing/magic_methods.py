class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        output = f'{self.amount} {self.currency}'

        if self.amount != 1:
            output += 's'

        return output

    def __add__(self, other):
        if other.currency != self.currency:
            raise ValueError('Cant convert between currencies')

        return Money(self.amount + other.amount, self.currency)


some_euro = Money(10, 'euro')
more_euro = Money(20, 'euro')
dollar = Money(1, 'dollar')

# print calls the "__str__"
print(some_euro)
print(dollar)

# + operator calls the "__add__"
added = some_euro + more_euro
print(added)


# ----------------------------------

class Team:
    def __init__(self):
        self._members = []

    def add(self, new_member):
        if new_member not in self:  # 'in self' works because the __contains__ method is defined
            self._members.append(new_member)

    def __contains__(self, value):
        return value in self._members

    def __len__(self):
        return len(self._members)


team = Team()
team.add('Steven')

# len function uses __len__
print(len(team))  # instead of len(team._members)

# operator 'in' uses __contains__
if 'Steven' in team:  # instead of ('Steven' in team._members)
    print('Steven is in the team!')
