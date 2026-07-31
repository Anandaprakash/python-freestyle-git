class EmployeeService:
    def calculate_annual_salary(self, monthly_salary):
        """Return annual salary given a monthly salary.

        Raises ValueError if `monthly_salary` is not greater than 0.
        """
        if monthly_salary <= 0:
            raise ValueError("monthly salary must be greater than 0")
        return monthly_salary * 12

    def calculate_bonus(self, monthly_salary, bonus_percentage):
        """Return bonus amount given monthly salary and percentage.

        Raises ValueError if `monthly_salary` is not greater than 0 or
        if `bonus_percentage` is negative.
        """
        if monthly_salary <= 0:
            raise ValueError("monthly salary must be greater than 0")
        if bonus_percentage < 0:
            raise ValueError("bonus percentage cannot be negative")
        return monthly_salary * bonus_percentage / 100

    def validate_employee(self, emp_id):
        """Return True if `emp_id` is a positive integer."""
        return isinstance(emp_id, int) and emp_id > 0
