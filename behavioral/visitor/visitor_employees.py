from datetime import date


class Employee:
    def __init__(self, id, name, date_of_employment):
        self.id = id
        self.name = name
        self.date_of_employment = date_of_employment


class SalaryEmployee(Employee):
    def __init__(self, id, name, date_of_employment, base_salary):
        super().__init__(id, name, date_of_employment)
        self.base_salary = base_salary

    def tenure(self):
        return date.today().year - self.date_of_employment.year

    def salary(self):
        return self.base_salary * (1.0 + 0.05 * self.tenure())


class HourlyEmployee(Employee):
    regular_hours = 160

    def __init__(self, id, name, date_of_employment, hours_worked_last_month, hourly_wage):
        super().__init__(id, name, date_of_employment)
        self.hours_worked_last_month = hours_worked_last_month
        self.hourly_wage = hourly_wage

    def overtime_hours(self):
        diff = self.hours_worked_last_month - regular_hours
        return diff if diff >= 0 else 0

    def salary(self):
        return self.hours_worked_last_month * self.hourly_wage


class TempEmployee(Employee):
    def __init__(self, id, name, date_of_employment, end_of_contract, wage):
        super().__init__(id, name, date_of_employment)
        self.end_of_contract = end_of_contract
        self.wage = wage

    def salary(self):
        return self.wage


class Visitor:
    def visit(self, node, *args, **kwargs):
        visiting_method = None
        
        for cls in node.__class__.__mro__:
            method_name = 'visit_' + cls.__name__
            visiting_method = getattr(self, method_name, None)
            if visiting_method:
                break

        if not visiting_method:
            visiting_method = self.generic_visit
        return visiting_method(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        raise TypeError()


class AvailableDaysOffVisitor(Visitor):
    def __init__(self):
        self.available_days_off = 0

    def visit_SalaryEmployee(self, employee):
        print('visiting_SalaryEmployee: ' + employee.name)
        self.available_days_off += (21 + employee.tenure())

    def visit_HourlyEmployee(self, employee):
        print('visiting_HourlyEmployee: ' + employee.name)
        if employee.hours_worked_last_month > 60:
            self.available_days_off += 5
        else:
            self.available_days_off += 1

    def visit_TempEmployee(self, employee):
        print('visiting_TempEmployee: ' + employee.name)
        self.available_days_off += 1


def main():
    employees = [SalaryEmployee(1, "Jan Kowalski", date(2010, 1, 1), 5500),
                 HourlyEmployee(2, "Ewa Nowak", date(2015, 1, 1), 120, 15),
                 TempEmployee(3, "Zenon Nowak", date(2015, 6, 1), date(2016, 6, 1), 2500)]

    visitor = AvailableDaysOffVisitor()

    for e in employees:
        visitor.visit(e)

    print('available days off: {}'.format(visitor.available_days_off))


if __name__ == '__main__':
    main()
