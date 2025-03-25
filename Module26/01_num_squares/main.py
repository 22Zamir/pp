####### Итератор #########
class SquareIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise SquareIterator
        result = self.current ** 2
        self.current += 1
        return result


########## ГЕНЕРАТОР ##############
def square_generator(n):
    current = 1
    while current <= n:
        yield current ** 2
        current += 1


############# Генераторное выржаение ###############

def square_generator_expression(n):
    return (coorent ** 2 for coorent in range(1, n + 1))
