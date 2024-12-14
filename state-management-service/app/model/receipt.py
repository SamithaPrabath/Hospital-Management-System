from datetime import datetime


class Receipt:
    """
    Receipt model class

    receipt_id: int
    patient_id: int
    doctor_id: int
    issued_by: int
    issued_date: datetime
    total_amount: float
    """

    def __init__(
            self,
            patient_id: int,
            doctor_id: int,
            issued_by: int,
            issued_date: datetime,
            total_amount: float,
            status: str = 'pending',
            receipt_id: int | None = None,
    ) -> None:
        """
        Constructor for Receipt class

        :param receipt_id: int
        :param patient_id: int
        :param doctor_id: int
        :param issued_by: int
        :param issued_date: datetime
        :param total_amount: float
        :param status: str
        """
        self.__id = receipt_id
        self.__patient_id = patient_id
        self.__doctor_id = doctor_id
        self.__issued_by = issued_by
        self.__issued_date = issued_date
        self.__total_amount = total_amount
        self.__status = status

    def get_receipt_id(self) -> int:
        """
        Get the receipt id

        :return: int
        """
        return self.__id

    def get_patient_id(self) -> int:
        """
        Get the patient id

        :return: int
        """
        return self.__patient_id

    def get_doctor_id(self) -> int:
        """
        Get the patient id

        :return: int
        """
        return self.__doctor_id

    def issued_by(self) -> int:
        """
        Get the patient id

        :return: int
        """
        return self.__issued_by

    def issued_date(self) -> datetime:
        """
        Get the patient id

        :return: int
        """
        return self.__issued_date

    def total_amount(self) -> float:
        """
        Get the patient id

        :return: int
        """
        return self.__total_amount

    def get_status(self) -> str:
        """
        Get the status of the receipt

        :return: str
        """
        return self.__status

    # setter methods for all the attributes
    def set_patient_id(self, patient_id: int) -> None:
        """
        Set the patient id

        :param patient_id: int
        """
        self.__patient_id = patient_id

    def set_doctor_id(self, doctor_id: int) -> None:
        """
        Set the doctor id

        :param doctor_id: int
        """
        self.__doctor_id = doctor_id

    def set_issued_by(self, issued_by: int) -> None:
        """
        Set the issued by

        :param issued_by: int
        """
        self.__issued_by = issued_by

    def set_issued_date(self, issued_date: datetime) -> None:
        """
        Set the issued date

        :param issued_date: datetime
        """
        self.__issued_date = issued_date

    def set_total_amount(self, total_amount: float) -> None:
        """
        Set the total amount

        :param total_amount: float
        """
        self.__total_amount = total_amount

    def set_status(self, status: str) -> None:
        """
        Set the status

        :param status: str
        """
        self.__status = status
