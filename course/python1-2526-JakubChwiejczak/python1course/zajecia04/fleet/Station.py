from abc import ABC, abstractmethod
from math import sqrt

from ..personnel import *
from .ambulance import Ambulance


class BaseStation(ABC):
    @abstractmethod
    def is_ambulance_available():
        pass

    @abstractmethod
    def get_station_info():
        pass


class Station(BaseStation):
    __max_id = 0

    @classmethod
    def get_next_id(cls):
        cls.__max_id += 1
        return cls.__max_id

    def __init__(self, location, ambulance, driver, employee):
        self.location = location
        self.id = self.get_next_id()
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee

    def is_ambulance_available(self):
        return self.ambulance.status == "available"

    def get_station_info(self):
        return f"info : location={self.location}, id={self.id}, ambulance={self.ambulance!s}, driver={self.driver!s},employee={self.employee!s} "

    def is_ambulance_at_station(self):
        if self.location == self.ambulance.location: 
            return f" ambulance at station\n" 
        else: 
            return f"ambulance is oustide the station\n" 
        

    def calculate_distance(loc1, loc2):
        distance = sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)
        return distance


if __name__ == "__main__":
    print("=== Test klas Employee i Driver ===")

    # Tworzymy pracownika
    emp1 = Employee("Jan", "Kowalski", 5000)  # employee_id nadawany automatycznie
    # Tworzymy kierowcę
    driver1 = Driver("Jane", "Smith", 12000.0, "LIC1001", ["BLS", "ACLS"])

    # Tworzymy karetki
    ambulance1 = Ambulance(
        vehicle_type="AZ124",
        status="available",
        location=(50.095340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"],
    )

    station = Station((50.095340, 19.920282), ambulance1, driver1, emp1) 
    print(station.get_station_info())
    print (station.is_ambulance_at_station())