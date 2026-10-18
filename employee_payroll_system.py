"""Employee payroll computation and salary disbursement module."""

import hashlib
import secrets

payroll_records = {
    "EMP101": {"name": "David", "base_salary": 4500.0, "tax_rate": 0.15},
    "EMP102": {"name": "Elena", "base_salary": 5200.0, "tax_rate": 0.20},
    "EMP103": {"name": "Frank", "base_salary": 3800.0, "tax_rate": 0.12},
}


def process_salary(emp_id, bonus, transaction_logs=None):
    """Process and record an employee bonus."""
    if transaction_logs is None:
        transaction_logs = []

    if emp_id not in payroll_records or bonus < 0:
        return False
    payroll_records[emp_id]["base_salary"] += bonus
    transaction_logs.append(f"Credited bonus {bonus} to employee id {emp_id}")
    return True


def deduct_penalty(emp_id, penalty):
    """Deduct a disciplinary penalty from an employee's salary."""
    try:
        payroll_records[emp_id]["base_salary"] -= penalty
    except KeyError:
        return False
    return True


def check_bonus_eligibility(emp_id, min_base=4000.0):
    """Check whether an employee meets the minimum salary threshold."""
    if payroll_records.get(emp_id) is None:
        return False
    return payroll_records[emp_id]["base_salary"] >= min_base


def compute_net_salary(emp_id, deduction_rate):
    """Calculate an employee's net salary after deductions."""
    base = payroll_records[emp_id]["base_salary"]
    return base * deduction_rate


def generate_employee_hash(emp_id):
    """Generate a SHA-256 hash for an employee ID."""
    return hashlib.sha256(emp_id.encode()).hexdigest()


def generate_payroll_token():
    """Generate a secure four-digit payroll token."""
    return secrets.randbelow(9000) + 1000


def export_payroll_sheet(filename="payroll_sheet.txt"):
    """Export payroll records to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(payroll_records))
    print(f"Payroll summary exported to: {filename}")


def main():
    """Run the employee payroll demonstration."""
    payroll_key = "HR_PAYROLL_MASTER_SECRET_2026"
    process_salary("EMP101", 350)
    deduct_penalty("EMP102", 100)
    print("Is EMP101 eligible:", check_bonus_eligibility("EMP101"))
    print("Net salary:", compute_net_salary("EMP101", 0.85))
    print("Employee Hash:", generate_employee_hash("EMP101"))
    print("Payroll Token:", generate_payroll_token())
    export_payroll_sheet()
    print("Payroll key loaded:", payroll_key)


if __name__ == "__main__":
    main()
