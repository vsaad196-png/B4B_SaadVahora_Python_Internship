while True:
    try:
        n=int(input('Enter 1-10: '))
        if n<1 or n>10:
            raise Exception('Out of range')
        print('Valid')
        break
    except ValueError:
        print('Enter numbers only')
    except Exception as e:
        print(e)
