import pytest

from app.employee_service import EmployeeService


service = EmployeeService()


def test_calculate_annual_salary():
    result = service.calculate_annual_salary(50000)
    assert result == 600000


def test_calculate_bonus():
    result = service.calculate_bonus(50000, 10)
    assert result == 5000


def test_invalid_salary_annual():
    with pytest.raises(ValueError, match="monthly salary must be greater than 0"):
        service.calculate_annual_salary(-1000)


def test_invalid_salary_bonus():
    with pytest.raises(ValueError, match="monthly salary must be greater than 0"):
        service.calculate_bonus(0, 5)


def test_negative_bonus_percentage():
    with pytest.raises(ValueError, match="bonus percentage cannot be negative"):
        service.calculate_bonus(50000, -1)


@pytest.mark.parametrize(
    "emp_id, expected_result",
    [
        (101, True),
        (1, True),
        (0, False),
        (-10, False),
        ("EMP101", False),
    ],
)
def test_validate_employee(emp_id, expected_result):
    assert service.validate_employee(emp_id) == expected_result
