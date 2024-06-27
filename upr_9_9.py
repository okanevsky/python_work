class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("Пробег автомобиля " + str(self.odometer_reading) + " км.")

    def update_odometer(self, mileage):
        """
        Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки изменение отклоняется.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("вне можете скрутить счетчик пробега")
    
    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        self.gas_tank = 120
        print("бензобак" + str(self.gas_tank))

class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("у данного автомобиля " + str(self.battery_size) + "-kWh батарея.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "автомобиль проедет " + str(range)
        message += " км на полной зарядке."
        print(message)
    
    def upgrade_battery(self):
        if self.battery_size !=85:
            self.battery_size = 85

class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        print("этому автомобилю не нужен бензобак!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

    
#my_used_car = Car('subaru', 'outback', 2013)
#print(my_used_car.get_descriptive_name())
#my_used_car.fill_gas_tank()
#my_used_car.update_odometer(23500)
#my_used_car.read_odometer()
#my_used_car.increment_odometer(100)
#my_used_car.read_odometer()