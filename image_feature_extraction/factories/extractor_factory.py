from image_feature_extraction.enumerators.extractor_enumerator import ExtractorEnumerator
from image_feature_extraction.extractors.base_extractor import BaseExtractor
from image_feature_extraction.extractors.haralick_extractor import HaralickExtractor


class ExtractorFactory:

    def __init__(self, extractor_enumerator: ExtractorEnumerator):
        self.__extractor_enumerator = extractor_enumerator

    def create(self) -> BaseExtractor:
        extractor = None
        match self.__extractor_enumerator:
            case ExtractorEnumerator.HARALICK:
                extractor = HaralickExtractor()
        if extractor is None:
            raise Exception(f"Unable to create object for enumerator '{self.__extractor_enumerator}'.")
        return extractor
