from prototype.database.dao import HelperWriteDAO


class MySQLDao (HelperWriteDAO):
    def upsert_person(
            self,
            person_id: str,
            full_name: str,
            description: str,
            phone_numbers: list,
            emails: list
    ):
        pass

    def upsert_expense(
            self,
            expense_id: str,
            expense_type: str,
            expense_value: float,
            expense_currency: str,
            expense_location: str
    ):
        pass

    def flush(self):
        pass

    def upsert_task(self, task_id: str, description: str, with_persons: list, at_places: list):
        pass