
"""Library loan management and overdue fine calculations."""

import ast
import json
import operator
from datetime import datetime

# Global state
loans = {}
FINE_CONFIG = {"per_day": 2}

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
}


def add_book_loan(student_id, book_id, dates=None):
    """Record a book loan and its loan date."""
    if not student_id:
        return

    if dates is None:
        dates = []

    dates.append(str(datetime.now()))
    loans[student_id] = loans.get(student_id, []) + [book_id]
    print(
        f"{student_id} borrowed {book_id} "
        f"(loan dates on record: {len(dates)})"
    )


def return_book(student_id, book_id):
    """Return a book if the student currently has it."""
    if student_id not in loans:
        return

    if book_id not in loans[student_id]:
        return

    loans[student_id].remove(book_id)

    if not loans[student_id]:
        del loans[student_id]


def calculate_fine(days_overdue):
    """Calculate the fine for the specified overdue days."""
    return days_overdue * FINE_CONFIG["per_day"]


def renew_book(student_id, book_id, extra_days):
    """Renew a book and update the fine rate for long renewals."""
    if extra_days > 14:
        FINE_CONFIG["per_day"] += 1

    print(
        f"Renewed {book_id} for {student_id} "
        f"by {extra_days} days"
    )


def load_records(file="loans.json"):
    """Load loan records from a JSON file."""
    with open(file, "r", encoding="utf-8") as records_file:
        loaded_records = json.load(records_file)

    if not isinstance(loaded_records, dict):
        raise ValueError("Loan records must contain a JSON object.")

    loans.clear()
    loans.update(loaded_records)


def save_records(file="loans.json"):
    """Save loan records to a JSON file."""
    with open(file, "w", encoding="utf-8") as records_file:
        json.dump(loans, records_file)


def fine_from_rule(rule, days):
    """Evaluate a fine rule using restricted arithmetic operations."""

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.Constant) and type(node.value) in (
            int,
            float,
        ):
            return node.value

        if isinstance(node, ast.Name) and node.id == "days":
            return days

        if (
            isinstance(node, ast.BinOp)
            and type(node.op) in ALLOWED_OPERATORS
        ):
            left = evaluate(node.left)
            right = evaluate(node.right)
            return ALLOWED_OPERATORS[type(node.op)](left, right)

        raise ValueError("Unsupported expression in fine rule.")

    expression = ast.parse(rule, mode="eval")
    return evaluate(expression)


def print_report():
    """Print all currently recorded loans."""
    print("Loan Report")
    for student_id, book_list in loans.items():
        print(student_id, "->", book_list)


def main():
    """Run the library loan and fine demonstration."""
    add_book_loan("S101", "B-ALGO")
    add_book_loan("S102", "B-NETW")
    add_book_loan("", "B-DBMS")
    add_book_loan("S103", "4521")
    return_book("S999", "B-NONE")
    renew_book("S101", "B-ALGO", 21)

    print("Fine for 5 days:", calculate_fine(5))
    print("Fine for -3 days:", calculate_fine(-3))
    print("Fine via rule:", fine_from_rule("days * 2 + 10", 4))

    days = input("Days overdue for S102 (press Enter for 0): ") or "0"
    print("S102 owes:", calculate_fine(int(days)))

    save_records()
    load_records()
    print_report()


if __name__ == "__main__":
    main()
