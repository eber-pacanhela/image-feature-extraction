from abc import ABC


class BaseExtractor(ABC):

    def extract_features(self, image_path: str) -> list:
        pass
