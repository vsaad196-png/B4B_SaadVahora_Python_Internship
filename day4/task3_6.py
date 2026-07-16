def process_order(order):
    try:
        print(order['item'])
        print(order['price'])
    except KeyError:
        print('Key missing')
    else:
        print('Order OK')
    finally:
        print('Processing complete')

process_order({'item':'Book','price':100})
