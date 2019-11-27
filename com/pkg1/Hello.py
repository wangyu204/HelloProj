# coding=utf-8

import enum


# 防止重复
@enum.unique
class WeekDays(enum.IntEnum):
    # 枚举常量列表
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3  # 'Wed.'
    THURSDAY = 4
    FRIDAY = 5  # 1


day = WeekDays.FRIDAY

print(day)
print(day.value)
print(day.name)
