class Cat:
    def __init__(self, name, age, color, is_sleeping=False):
        self.name = name
        self.age = age
        self.color = color
        self.is_sleeping = is_sleeping

    def sleep(self):
        self.is_sleeping = True

    def wake_up(self):
        self.is_sleeping = False

    def make_sound(self):
        if self.is_sleeping:
            print("Zzz...")
        else:
            print("Мяу!")


kiska1 = Cat("kiska1", 10, "green")
kiska1.make_sound()
kiska1.sleep()
kiska1.make_sound()  # Выведет: Zzz...
kiska1.wake_up()
kiska1.make_sound()  # Выведет: Мяу!
