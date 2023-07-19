class Wheel:
    def rotate(self):
        print('Wheel rotating.')


class V8Engine:
    def start(self):
        print('Engine starting with a bang.')


class SteeringWheel:
    def turn(self):
        print('Steering wheel turning.')


class Engine:
    def start(self):
        print('Engine starting.')


class Car:
    def __init__(self):
        self.engine = Engine()
        self.steering_wheel = SteeringWheel()
        self.wheels = [
            Wheel(),
            Wheel(),
            Wheel(),
            Wheel()
        ]

    def drive(self):
        self.engine.start()
        for wheel in self.wheels:
            wheel.rotate()
        self.steering_wheel.turn()


car = Car()
car.drive()
