import os

DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DIR_TRAIN_PATH = os.path.join(DIR_PATH, "Data/Data_Full/train")
DIR_TEST_PATH = os.path.join(DIR_PATH, "Data/Data_Full/test")
DIR_FEATURE_PATH = os.path.join(DIR_PATH, "Data/Feature")
DIR_DICTIONARY = os.path.join(DIR_PATH, "Data/dictionary.txt")

DIR_MY_DATA_PATH = os.path.join(DIR_PATH, "Data/MyData")
DIR_MY_FEATURE_PATH = os.path.join(DIR_PATH, "Data/MyFeature")

DIR_APP_PATH = os.path.join(DIR_PATH, "Data/App")

SPECIAL_CHARACTER = '0123456789%@$.,=+-!;/()*"&^:#|~_{}[]\n\t\'\"`‘\\ <>?'
STOP_WORD = os.path.join(DIR_PATH, "Data/stopword.txt")
LEFT_WORD = os.path.join(DIR_PATH, "Data/left_word")