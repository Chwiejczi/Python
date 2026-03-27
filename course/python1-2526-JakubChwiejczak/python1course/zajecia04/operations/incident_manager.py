from ..fleet import *
from ..personnel import *
from .incident_queue import IncidentQueue 
from .incident import *


class IncidentManager:
    def __init__(self, stations):
        self.stations = stations
        self.incidentQueue = IncidentQueue

    def add_incident(self, incident):
        self.incidentQueue += incident 

    def get_available_ambulances(self): 
        amb=self.stations.ambulance 
        amb_available=[]
        for a in amb: 
            if a.status=="Available": 
                amb_available.append(a) 
        return amb_available

    @staticmethod
    def calculate_priority_score(incident): 
        #critical-6 , low_danger-3 , marginal-1 
        #we are adding also time  
        danger={"critical":6,"low_danger":3,"marginal":1} 
        emergency_score=danger[incident.priority] + incident.get_age_in_minutes() 
        return emergency_score   
        
        
        

    

    #def assign_ambulance(self,incident): 
    #"critical,low_danger,marginal" - priorities


if __name__ == "__main__":
    from datetime import datetime

    incident = Incident(
        "Fire in building", priority="critical", info=["John Doe", "123456789"]
    ) 
    print(incident.__str__()) 

    #im=IncidentManager(incident) 
    #print(im.calculate_priority_score(incident)) 
    
    a1 = Ambulance(
        # id=0,
        vehicle_type="AZ124",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"],
    )
    a2 = Ambulance(
        # id=1,
        vehicle_type="AZ2000",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"],
    ) 
    emp1 = Employee("Jan", "Kowalski", 5000)  # employee_id nadawany automatycznie
    # Tworzymy kierowcę
    driver1 = Driver("Jane", "Smith", 12000.0, "LIC1001", ["BLS", "ACLS"]) 

    station = Station((50.095340, 19.920282), [a1,a2], driver1, emp1) 

    im=IncidentManager(stations=station)
    print(im.get_available_ambulances()) 
    im.add_incident(incident) 
    print(im.calculate_priority_score(im.incidentQueue))
