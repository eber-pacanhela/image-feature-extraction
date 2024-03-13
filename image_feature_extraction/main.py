import argparse
import os

from image_feature_extraction.enumerators.extractor_enumerator import ExtractorEnumerator
from image_feature_extraction.factories.extractor_factory import ExtractorFactory
from image_feature_extraction.utils.directory_util import DirectoryUtil
from image_feature_extraction.utils.enumerator_util import EnumeratorUtil
from image_feature_extraction.utils.file_util import FileUtil

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--images_path", type=str, required=True, help="Images path.")
    parser.add_argument("-e", "--extractors", nargs='+', required=True,
                        help="List of extractor names. Possible values: See 'ExtractorEnumerator' enumerator.")
    parser.add_argument("-x", "--extensions", nargs='+', default=['.jpg', '.jpeg'], help="Image extensions list.")
    opt = parser.parse_args()

    OUTPUT_DIRECTORY = "./output"
    DirectoryUtil.validate(path=opt.images_path, message="Images path not found.")
    DirectoryUtil.make(path=OUTPUT_DIRECTORY)
    for extractor_name in opt.extractors:
        extractor_enumerator = EnumeratorUtil.find_by_name(name=extractor_name, enumerator_type=ExtractorEnumerator)
        extractor = ExtractorFactory(extractor_enumerator=ExtractorEnumerator(extractor_enumerator)).create()
        with open(f"{OUTPUT_DIRECTORY}/{extractor_name}.csv", mode='w') as file:
            header = ""
            for image_name in sorted(os.listdir(path=opt.images_path)):
                image_path = f"{opt.images_path}/{image_name}"
                if not FileUtil.is_image(image_path=image_path, extensions=opt.extensions):
                    continue
                features = extractor.extract_features(image_path=image_path)
                if header == "":
                    header = "image_name"
                    for i in range(len(features)):
                        header += f";feature_{i}"
                    file.write(f"{header}\n")
                body = image_name.replace(";", "")
                for feature in features:
                    body += f";{feature}"
                file.write(body)
