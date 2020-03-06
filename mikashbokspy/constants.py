#!/usr/bin/python
from enum import Enum


class BaseEnum(Enum):
    """
    Base enum
    """

    @classmethod
    def from_value(cls, value):
        """
        Returns the valid enum if value found else none
        :param value: enum value
        :return: return valid
        """
        try:
            return cls(value)
        except ValueError:
            return None

    @classmethod
    def values(cls):
        """
        Returns list of values for an enum
        :return: list of values for an enum
        """
        return [enum_member.value for enum_member in cls]


class GroupStatus(BaseEnum):
    DRAFT = 'DRAFT'
    ACTIVE = 'ACTIVE'
    DONE = 'DONE'


class GroupTypes(BaseEnum):
    VSLA = 'VSLA'
    ROSCA = 'ROSCA'
    Custom = 'Custom'
    TimeDepositOpen = 'TimeDepositOpen'
    TimeDepositFixed = 'TimeDepositFixed'
    InsuranceFund = 'InsuranceFund'


class GroupDayUOM(BaseEnum):
    DAY = 'DAY'
    WEEK = 'WEEK'
    MONTH = 'MONTH'


class LoanStatus(BaseEnum):
    ACTIVE = 'ACTIVE'
    PAID = 'PAID'
    UNPAID = 'UNPAID'


class MemberIdentificationType(BaseEnum):
    VOTER = 'VOTER'
    PASSPORT = 'PASSPORT'
    NATIONAL = 'NATIONAL'
    DRIVER = 'DRIVER'


class MemberStatus(BaseEnum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    PENDING = 'PENDING'
    PROBATION = 'PROBATION'


class ObserverStatus(BaseEnum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    REQUESTED = 'REQUESTED'
    INVALID = 'INVALID'


class TokenDirection(BaseEnum):
    IN = 'IN'
    OUT = 'OUT'


class TransactionDirection(BaseEnum):
    IN = 'IN'
    OUT = 'OUT'


class TransactionAccount(BaseEnum):
    DEPOSIT = 'DEPOSIT'
    INSURANCE = 'INSURANCE'


class TransactionPaymentMethod(BaseEnum):
    CASH = 'CASH'
    MOBILE_MONEY = 'MOBILE_MONEY'
    DEBIT_CARD = 'DEBIT_CARD'


class TransactionType(BaseEnum):
    DEPOSIT = 'DEPOSIT'
    LOAN = 'LOAN'  # Repayments are in and disbursement are out
    INSURANCE = 'INSURANCE'  # should not be displayed in balance calculations
    FINE = 'FINE'
    ADJUSTMENT = 'ADJUSTMENT'
