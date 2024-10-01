class Bell:
    def __init__(self, *specifications, **information):
        self.specifications = specifications
        self.information = information

    def print_info(self):
        if self.information:
            print(*[f'{i}: {self.information[i]}' for i in sorted(self.information.keys())], sep=', ', end='')
            if not self.specifications:
                print()
        if self.specifications:
            if self.information:
                print('; ', end='')
            print(*self.specifications, sep=', ')
        if not self.information and not self.specifications:
            print('-')


class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print('...')

    def print_info(self):
        for i in range(len(self.bells)):
            print(i + 1, self.bells[i].__class__.__name__, sep=' ')
            self.bells[i].print_info()
        print()


class LittleBell(Bell):
    def sound(self):
        print('ding')


class BigBell(Bell):
    def __init__(self, *specifications, **information):
        super().__init__(*specifications, **information)
        self.flag_ding = True

    def sound(self):
        if self.flag_ding:
            self.flag_ding = False
            print('ding')
        else:
            self.flag_ding = True
            print('dong')


class SizedBellTower(BellTower):
    def __init__(self, *bells, size=10):
        if len(bells) > size:
            self.bells = list(bells[len(bells) - size:])
        else:
            super().__init__(*bells)
        self.size = size

    def append(self, bell):
        if len(self.bells) == self.size:
            del self.bells[0]
            super().append(bell)
        else:
            super().append(bell)


class TypedBellTower(BellTower):
    def __init__(self, *bells, bell_type=LittleBell):
        self.bells = [bell for bell in bells if isinstance(bell, bell_type)]
        self.bell_type = bell_type

    def append(self, bell):
        if isinstance(bell, self.bell_type):
            super().append(bell)

bells = [BigBell(), BigBell("медный"), BigBell(цвет="серебристый"), BigBell("звонкий", диаметр="5 см"), BigBell("ля"),
         LittleBell("звонкий"), LittleBell(нота="до"), LittleBell(),
         LittleBell("тихий", "мелодичный", вес="100 грамм", нота="ре"), LittleBell()]
bt_default = SizedBellTower(*bells)
bt_1 = SizedBellTower(*bells, size=1)
bt_2 = SizedBellTower(*bells, size=2)
bt_10 = SizedBellTower(*bells, size=10)
bt_11 = SizedBellTower(*bells, size=11)
bt_20 = SizedBellTower(*bells, size=20)
bts = [bt_default, bt_1, bt_2, bt_10, bt_11, bt_20]

bb = BigBell("самый звонкий")
lb = LittleBell("самый маленький")
for bt in bts:
    bt.append(bb)
    bt.append(lb)
for bt in bts:
    bt.print_info()
