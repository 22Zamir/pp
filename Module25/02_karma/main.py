import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    day = 0
    total_karma = 0

    while total_karma < 500:
        day += 1

        if random.randint(1, 10) == 1:
            dice = random.choice([DrunkError, KillError, GluttonyError, DepressionError, CarCrashError])
            with open('karma.log', 'a', encoding='utf-8') as file:
                file.write(f'День: {day} Исключение: {dice}\n')
                try:
                    if dice == DrunkError:
                        raise DrunkError
                    elif dice == KillError:
                        raise KillError
                    elif dice == GluttonyError:
                        raise GluttonyError
                    elif dice == DepressionError:
                        raise DepressionError
                    else:
                        raise CarCrashError
                except DrunkError:
                    print(f'День: {day} Исключение: {dice}')
                except KillError:
                    print(f'День: {day} Исключение: {dice}')
                except GluttonyError:
                    print(f'День: {day} Исключение: {dice}')
                except DepressionError:
                    print(f'День: {day} Исключение: {dice}')
                except CarCrashError:
                    print(f'День: {day} Исключение: {dice}')
        else:
            carma = random.randint(1, 7)
            total_karma += carma
            print(f'День: {day}\nВыпало кармы:{carma}\nВсего кармы:{total_karma}')


one_day()
