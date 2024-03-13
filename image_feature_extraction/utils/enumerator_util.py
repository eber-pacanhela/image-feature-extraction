from enum import Enum


class EnumeratorUtil:

    @staticmethod
    def find_by_name(name: str, enumerator_type: type[Enum]) -> Enum:
        enumerator_name = f"{enumerator_type.__name__}.{name}".lower()
        for enum in enumerator_type:
            if enumerator_name == str(enum).lower():
                return enum
        raise Exception(f"Enumerator '{name}' not found.")
