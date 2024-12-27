from datetime import datetime


class Payment:
    """
    Payment model class
    """

    def __init__(
            self,
            payment_id: int,
            receipt_id: int,
            collected_by: int,
            collected_date: datetime
    ) -> None:
        """
        Constructor for Receipt class

        :param payment_id: int
        :param receipt_id: int
        :param collected_by: int
        :param collected_date: datetime
        """
        self.__id = payment_id
        self.__receipt_id = receipt_id
        self.__collected_by = collected_by
        self.__collected_date = collected_date

    def get_payment_dict(self) -> dict:
        """
        Get Payment object as dictionary
        """
        return {
            'payment_id': self.__id,
            'receipt_id': self.__receipt_id,
            'collected_by': self.__collected_by,
            'collected_date': self.__collected_date
        }
