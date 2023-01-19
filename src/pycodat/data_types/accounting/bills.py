import typing

from pydantic import BaseModel


class SupplierRef(BaseModel):
    id: typing.Optional[str]
    supplierName: typing.Optional[str]


class PurchaseOrderRef(BaseModel):
    id: typing.Optional[str]
    purchaseOrderNumber: typing.Optional[str]


class AccountRef(BaseModel):
    id: typing.Optional[str]
    name: typing.Optional[str]


class TaxRateRef(BaseModel):
    id: typing.Optional[str]
    name: typing.Optional[str]
    effectiveTaxRate: typing.Optional[int]


class ItemRef(BaseModel):
    id: typing.Optional[str]
    name: typing.Optional[str]


class TrackingCategoryRef(BaseModel):
    id: typing.Optional[str]
    name: typing.Optional[str]


class CategoryRef(BaseModel):
    id: typing.Optional[str]
    name: typing.Optional[str]


class CustomerRef(BaseModel):
    id: typing.Optional[str]
    companyName: typing.Optional[str]


class ProjectRef(BaseModel):
    id: typing.Optional[str]
    name: typing.Optional[str]


class Tracking(BaseModel):
    categoryRefs: typing.List[CategoryRef]
    customerRef: typing.Optional[CustomerRef]
    projectRef: typing.Optional[ProjectRef]
    isBilledTo: typing.Optional[str]
    isRebilledTo: typing.Optional[str]


class LineItem(BaseModel):
    description: typing.Optional[str]
    unitAmount: typing.Optional[int]
    quantity: typing.Optional[int]
    discountAmount: typing.Optional[int]
    subTotal: typing.Optional[int]
    taxAmount: typing.Optional[int]
    totalAmount: typing.Optional[int]
    discountPercentage: typing.Optional[int]
    accountRef: AccountRef
    taxRateRef: typing.Optional[TaxRateRef]
    itemRef: typing.Optional[ItemRef]
    trackingCategoryRefs: typing.List[TrackingCategoryRef]
    tracking: typing.Optional[Tracking]
    isDirectCost: typing.Optional[bool]


class WithholdingTaxItem(BaseModel):
    name: typing.Optional[str]
    amount: typing.Optional[int]


class Payment(BaseModel):
    id: typing.Optional[str]
    note: typing.Optional[str]
    reference: typing.Optional[str]
    accountRef: AccountRef
    currency: typing.Optional[str]
    currencyRate: typing.Optional[int]
    paidOnDate: typing.Optional[str]
    totalAmount: typing.Optional[int]


class Allocation(BaseModel):
    currency: typing.Optional[str]
    currencyRate: typing.Optional[int]
    allocatedOnDate: typing.Optional[str]
    totalAmount: typing.Optional[int]


class PaymentAllocation(BaseModel):
    payment: Payment
    allocation: Allocation


class Metadata(BaseModel):
    isDeleted: typing.Optional[bool]


class Bill(BaseModel):
    id: typing.Optional[str]
    reference: typing.Optional[str]
    supplierRef: SupplierRef
    purchaseOrderRefs: typing.List[PurchaseOrderRef]
    issueDate: typing.Optional[str]
    dueDate: typing.Optional[str]
    currency: typing.Optional[str]
    currencyRate: typing.Optional[int]
    lineItems: typing.List[LineItem]
    withholdingTax: typing.List[WithholdingTaxItem]
    status: typing.Optional[str]
    subTotal: typing.Optional[int]
    taxAmount: typing.Optional[int]
    totalAmount: typing.Optional[int]
    amountDue: typing.Optional[int]
    modifiedDate: typing.Optional[str]
    sourceModifiedDate: typing.Optional[str]
    note: typing.Optional[str]
    paymentAllocations: typing.List[PaymentAllocation]
    metadata: Metadata
