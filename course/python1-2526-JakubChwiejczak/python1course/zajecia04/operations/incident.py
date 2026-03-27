from datetime import datetime


class Incident:
    __max_id = 0
    # priority=["low", "medium", "high", "critical"]
    __slots__ = ["Datetime", "description", "id", "info", "priority", "status"]

    @staticmethod
    def validate_priority(priority):
        if priority in ["critical","low_danger","marginal"]:
            return True
        else:
            return False

    @classmethod
    def get_next_id(cls):
        cls.__max_id += 1
        return cls.__max_id

    @classmethod
    def reset_id_counter(cls):
        cls.__max_id = 0

    def __init__(self, description, priority, info):
        self.id = self.get_next_id()
        self.description = description
        self.priority = priority
        self.Datetime = datetime.now()
        self.info = info
        self.status = "reported" 

    def get_age_in_minutes(self):
        delta = abs(self.Datetime - datetime.now())
        delta = delta.microseconds/20
        # wiem ze zwracam wynik w mikrosekundach, ale zwracanie wyniku w minutach nie ma sensu, bo zawsze będzie zwracalo 0.
        return delta

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"description {self.description}, priority {self.priority}, time {self.Datetime}, personal info {self.info}, status {self.status}"

    def __repr__(self):
        return f"Incident(id={self.id!r}, description={self.description!r})"

    # def __str__(self):
    #   return f"Incident {self.id}: {self.description}"


if __name__ == "__main__":
    from datetime import datetime

    incident = Incident(
        "Fire in building", priority="critical", info=["John Doe", "123456789"]
    )
    print(incident.status)  # "reported" - domyślny status przy tworzeniu
    print(incident.get_age_in_minutes())  # Liczba minut od zgłoszenia

    # Aktualizacja statusu
    incident.update_status("assigned")  # Karetka została przydzielona
    incident.update_status("in_progress")  # Karetka jest w drodze/na miejscu
    incident.update_status("resolved")  # Incydent został obsłużony
    print(incident.status)
    print("\n")
    print(incident)
