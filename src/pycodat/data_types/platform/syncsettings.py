import datetime
import typing

from pydantic import BaseModel


class SyncSetting(BaseModel):
    dataType: typing.Optional[str] = None
    fetchOnFirstLink: bool
    syncSchedule: int
    syncOrder: int
    syncFromUtc: typing.Optional[datetime.datetime] = None
    syncFromWindow: typing.Optional[int] = None
    monthsToSync: typing.Optional[int] = None


class SyncSettings(BaseModel):

    companyId: str
    settings: typing.Optional[typing.List[SyncSetting]] = None
    overridesDefaults: bool
