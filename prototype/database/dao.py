from abc import ABC, abstractmethod


class HelperWriteDAO (ABC):
    """
    This is an interface for the DAO used to write data into the system, following the OWL ontology. The implementations
    of this interface are supposed to validate the object, convert them to triples, and store them somewhere.
    """
    @abstractmethod
    def upsert_task(
            self,
            user: str,
            task_id: str,
            description: str,
            with_persons: list,
            at_places: list
    ):
        """
        Upsert a task
        :param user: The user for the entries. This can be used for partitioning data for different users.
        :param task_id:  A unique ID to use to store the task as.
        :param description: Description of the task. (Optional).
        :param with_persons: A list of `Person` objects associated with this task. (Optional).
        :param at_places: A list of locations associated with this task. (Optional).
        :return:
        """
        pass

    @abstractmethod
    def upsert_person(
            self,
            user: str,
            person_id: str,
            full_name: str,
            description: str,
            phone_numbers: list,
            emails: list
    ):
        """
        Upsert a task
        :param user: The user for the entries. This can be used for partitioning data for different users.
        :param person_id:  A unique ID to use to store the person as.
        :param full_name: Name of the person.
        :param description: Description of the person, like "plumber", etc. (Optional).
        :param phone_numbers: A list of phone numbers of this person. (Optional).
        :param emails: A list of emails of the person. (Optional).
        :return:
        """
        pass

    @abstractmethod
    def upsert_expense(
            self,
            user: str,
            expense_id: str,
            expense_type: str,
            expense_value: float,
            expense_currency: str,
            expense_location: str
    ):
        """
        Upsert a task
        :param user: The user for the entries. This can be used for partitioning data for different users.
        :param expense_id:  A unique ID to use to store the expense data.
        :param expense_type: The type of expense. Look at the ontology to determine types.
        :param expense_value: The amount of money spent.
        :param expense_currency: Currency used.
        :param expense_location: Where the expense was made. (Optional).
        :return:
        """
        pass

    @abstractmethod
    def flush(self):
        """
        Write the graph back to the persistence layer.
        """
        pass


