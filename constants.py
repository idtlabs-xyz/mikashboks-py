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


class GroupStatus(Enum):
    DRAFT = 'DRAFT'
    ACTIVE = 'ACTIVE'
    DONE = 'DONE'


class GroupTypes(Enum):
    VSLA = 'VSLA'
    ROSCA = 'ROSCA'


class GroupDayUOM(Enum):
    DAY = 'DAY'
    WEEK = 'WEEK'
    MONTH = 'MONTH'


class LoanStatus(Enum):
    ACTIVE = 'ACTIVE'
    PAID = 'PAID'
    UNPAID = 'UNPAID'


class MemberIdentificationType(Enum):
    VOTER = 'VOTER'
    PASSPORT = 'PASSPORT'
    NATIONAL = 'NATIONAL'
    DRIVER = 'DRIVER'


class MemberStatus(Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    PENDING = 'PENDING'
    PROBATION = 'PROBATION'


class ObserverStatus(Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    REQUESTED = 'REQUESTED'
    INVALID = 'INVALID'


class TokenDirection(Enum):
    IN = 'IN'
    OUT = 'OUT'


class TransactionDirection(Enum):
    IN = 'IN'
    OUT = 'OUT'


class TransactionAccount(Enum):
    DEPOSIT = 'DEPOSIT'
    INSURANCE = 'INSURANCE'


class TransactionPaymentMethod(Enum):
    CASH = 'CASH'
    MOBILE_MONEY = 'MOBILE_MONEY'
    DEBIT_CARD = 'DEBIT_CARD'


class TransactionType(Enum):
    DEPOSIT = 'DEPOSIT'
    LOAN = 'LOAN'  # Repayments are in and disbursement are out
    INSURANCE = 'INSURANCE'  # should not be displayed in balance calculations
    FINE = 'FINE'
    ADJUSTMENT = 'ADJUSTMENT'
