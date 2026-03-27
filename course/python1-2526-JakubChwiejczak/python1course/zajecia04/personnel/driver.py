from .employee import Employee


class Driver(Employee):
    __max_id = 0

    @classmethod
    def get_next_id(cls):
        cls.__max_id += 1
        return cls.__max_id

    @classmethod
    def reset_id_counter(cls):
        cls.__max_id = 0

    def __init__(self, first_name, last_name, salary, license_number, qualifications):
        super().__init__(first_name, last_name, salary)
        self.license_number = license_number
        self.qualifications = qualifications

    def display_info(self):
        qualifications_joined = ", ".join(self.qualifications)
        return super().display_info() + " Qualifications:" + qualifications_joined

    def __str__(self):
        return f"Driver({self.first_name} {self.last_name}, ID: {self.employee_id}, License: {self.license_number})"

    def __repr__(self):
        return f" Driver( '{self.first_name}', '{self.last_name}', '{self.employee_id}', '{self.salary}', '{self.license_number}', '{self.qualifications}')"


# Uruchomienie tego kodu: python -m python1course.zajecia04.personnel.driver
if __name__ == "__main__":
    driver1 = Driver("Jane", "Smith", 12000.00, "LIC1001", ["BLS"])
    print(driver1.display_info())
