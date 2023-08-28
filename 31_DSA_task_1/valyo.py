from collections import defaultdict


class Item():
    def __init__(self, item_name, price, child_name) -> None:
        self._item_name = item_name
        self._price = price
        self._child_name = child_name

    @property
    def item_name(self):
        return self._item_name

    @property
    def price(self):
        return self._price

    @property
    def child_name(self):
        return self._child_name

    def __str__(self) -> str:
        return '{' + f'{self.item_name};{self.child_name};{self.price:.2f}' + '}'


class SantaBag():
    def __init__(self) -> None:
        self.items = defaultdict(list)

    def add_item(self, item: Item):
        self.items[item.child_name].append(item)

    def remove_items(self, child_name):
        return len(self.items.pop(child_name))


def name(item):
    return item.item_name


N = int(input())

bag = SantaBag()
output = []
for i in range(N):
    cmd, params = input().split(' ', 1)
    if cmd == 'AddWish':
        item_name, price, child_name = params.split(';')
        item = Item(item_name, float(price), child_name)
        bag.add_item(item)
        output.append('Wish added')

    if cmd == 'DeleteWishes':
        child_name = params
        if child_name in bag.items.keys():
            deleted_wishes = bag.remove_items(child_name)
            output.append(f'{deleted_wishes} Wishes deleted')
        else:
            output.append('No Wishes found')

    if cmd == 'FindWishesByPriceRange':
        from_price, to_price = params.split(';')
        wishes = []
        for value in bag.items.values():
            for item in value:
                if item.price >= float(from_price) and item.price <= float(to_price):
                    wishes.append(item)
        wishes.sort(key=name)
        for wish in wishes:
            output.append(str(wish))
        if len(wishes) == 0:
            output.append('No Wishes found')

    if cmd == 'FindWishesByChild':
        child_name = params
        wishes = []
        if child_name in bag.items.keys():
            for item in bag.items.get(child_name):
                wishes.append(item)
            wishes.sort(key=name)
            for wish in wishes:
                output.append(str(wish))
        else:
            output.append('No Wishes found')

print('\n'.join(output))