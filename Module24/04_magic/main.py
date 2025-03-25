class ElemWater:

    def __add__(self, other):
        if isinstance(other, ElemAir):
            return ElemStorm()
        elif isinstance(other, ElemFire):
            return ElemSteam()
        elif isinstance(other, ElemEarth):
            return ElemMud()
        else:
            return None


class ElemAir:

    def __add__(self, other):
        if isinstance(other, ElemWater):
            return ElemStorm()
        elif isinstance(other, ElemEarth):
            return ElemDust()
        elif isinstance(other, ElemFire):
            return ElemLightning()
        else:
            return None


class ElemFire:

    def __add__(self, other):
        if isinstance(other, ElemWater):
            return ElemSteam()
        elif isinstance(other, ElemEarth):
            return ElemLava()
        elif isinstance(other, ElemAir):
            return ElemLightning()
        else:
            return None


class ElemEarth:

    def __add__(self, other):
        if isinstance(other, ElemWater):
            return ElemMud()
        elif isinstance(other, ElemAir):
            return ElemDust()
        elif isinstance(other, ElemFire):
            return ElemLava()
        else:
            return None


class ElemStorm:

    def __str__(self):
        return 'Шторм'


class ElemSteam:

    def __str__(self):
        return 'Пар'


class ElemMud:
    def __str__(self):
        return 'Грязь'


class ElemLightning:

    def __str__(self):
        return 'Молния'


class ElemDust:
    def __str__(self):
        return 'Пыль'


class ElemLava:

    def __str__(self):
        return 'Лава'


water = ElemWater()
air = ElemAir()
fire = ElemFire()
earth = ElemEarth()

print(earth + water)
print(fire + water)
