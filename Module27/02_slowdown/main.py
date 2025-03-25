import time


def waiting(func):
    def timing():
        print('WAIT...')
        time.sleep(3)
        func()

    return timing


@waiting
def test():
    print('Done!')


test()
