import datetime
import typing

from pydantic import BaseModel


class SyncSetting(BaseModel):
    dataType: str
    fetchOnFirstLink: bool
    syncSchedule: typing.Optional[int] = None
    syncOrder: typing.Optional[int] = None
    syncFromUtc: typing.Optional[datetime.datetime] = None
    syncFromWindow: typing.Optional[int] = None
    monthsToSync: typing.Optional[int] = None


class SyncSettings(BaseModel):

    companyId: str
    settings: typing.List[SyncSetting]
    overridesDefaults: bool
