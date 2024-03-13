import os
from pathlib import Path


class DirectoryUtil:

    @staticmethod
    def exists(path: str) -> bool:
        p = Path(path)
        return p.exists() and p.is_dir()

    @staticmethod
    def validate(path: str, message: str):
        if not DirectoryUtil.exists(path=path):
            raise Exception(message)

    @staticmethod
    def make(path: str):
        if not DirectoryUtil.exists(path=path):
            os.makedirs(path)
