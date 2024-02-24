from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

# Subject interface
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Concrete Observer
class WeatherDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure} hPa")

# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()

# Usage
weather_station = WeatherStation()

display1 = WeatherDisplay()
display2 = WeatherDisplay()

weather_station.register_observer(display1)
weather_station.register_observer(display2)

weather_station.set_measurements(25, 60, 1010)




