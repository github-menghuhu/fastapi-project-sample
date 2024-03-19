from datetime import datetime, timedelta
from uuid import UUID, uuid4


def get_random_uuid() -> UUID:
    """
    获取随机uuid
    :return:
    """
    return uuid4()


def get_designated_time(
    designated_time: datetime | None = None, days: int = 1, hours: int = 12
) -> datetime:
    """
    获取给定日期的前后时间
    :param designated_time: 给定日期，默认当前时间
    :param days: 天，正数代表在给定日期加天数，负数代表在给定日期减天数
    :param hours: 小时，正数代表在给定日期加小时数，负数代表在给定日期减小时数
    :return:
    """
    if designated_time is None:
        designated_time = datetime.now()
    return designated_time + timedelta(days=days, hours=hours)
