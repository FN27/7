class Car:
    def __init__(self,speed,color):
        self.speed=speed
        self.color=color
    def beep(self):
        print('beeeeeeep')
    def say_speed(self):
        print(f'Speed:{self.speed}')
    def say_color(self):
        print(f'Color:{self.color}')
porshe=Car(120,'black')
porshe.beep()
bmw=Car(100,'green')
bmw.beep()
bmw.say_speed()
porshe.say_speed()
porshe.say_color()
bmw.say_color()
