import datetime
import typing

from pydantic import BaseModel


class SyncSetting(BaseModel):
    dataType: str
    fetchOnFirstLink: bool
    syncSchedule: int = None
    syncOrder: int = None
    syncFromUtc: datetime.datetime = None
    syncFromWindow: int = None
    monthsToSync: int = None


class SyncSettings(BaseModel):

    companyId: str
    settings: typing.List[SyncSetting]
    overridesDefaults: bool
