def user_view(data: dict):
    name = data['username']
    id = data['id']

    return f'{name}, id: {id}'


def order_view(data):
    order_id = data['id']
    product_ids = data['product_ids']
    delivery_date = data['delivery_date']
    delivery_address = data['delivery_address'] or 'Unknown'

    return '\n'.join([
        f'Order id={order_id}; {len(product_ids)} products',
        f'To be delivered on: {delivery_date}',
        f'Address: {delivery_address}'
    ])


def product_view(data):
    id = data['id']
    name = data['name']
    desc = data['description']
    price = data['price']

    return f'{id}. {name}, {desc}, {price}$'


def order_response_view(data):
    order_id = data['id']
    user = data['customer']
    products = data['products']
    delivery_date = data['delivery_date']
    delivery_address = data['delivery_address'] or 'Unknown'
    order_total = data['order_total']

    return '\n'.join([
        '===================',
        f'OrderID = {order_id} by {user_view(user)}',
        f'To be delivered on: {delivery_date}',
        f'Address: {delivery_address}',
        f'Total: {order_total}$',
        f'Products:',
        *(product_view(p) for p in products)
    ])
