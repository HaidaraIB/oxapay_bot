from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def get_values(cls):
        return list(map(lambda x: x.value, list(cls)))
