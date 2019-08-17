from ..mapper import PropertyMapper, ApiInterfaceBase

__all__ = ['AccountSummaryUnit', 'AccountSummaryUnitInterface']


class AccountSummaryUnitInterface(ApiInterfaceBase):
    posts_count: int


class AccountSummaryUnit(PropertyMapper, AccountSummaryUnitInterface):
    pass
