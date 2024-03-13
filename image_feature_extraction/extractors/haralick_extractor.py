import cv2
import mahotas as mt

from image_feature_extraction.extractors.base_extractor import BaseExtractor


class HaralickExtractor(BaseExtractor):
    """
    Reference:
        R. M. Haralick, K. Shanmugam and I. Dinstein, "Textural Features for Image Classification",
        in IEEE Transactions on Systems, Man, and Cybernetics, vol. SMC-3, no. 6, pp. 610-621, Nov. 1973,
        doi: 10.1109/TSMC.1973.4309314.
    """

    def extract_features(self, image_path: str) -> list:
        image = cv2.imread(filename=image_path)
        gray = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
        textures = mt.features.haralick(f=gray)
        return textures.mean(axis=0)
