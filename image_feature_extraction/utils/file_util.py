from pathlib import Path


class FileUtil:

    @staticmethod
    def is_image(image_path: str, extensions: list[str]) -> bool:
        suffix = Path(image_path).suffix.lower()
        for extension in extensions:
            if suffix == extension.lower():
                return True
        return False
