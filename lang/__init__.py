# fileName : lang/__init__.py
# copyright ยฉ๏ธ 2021 nabilanavab

from configs.config import settings

langList = {
        "eng" : ["๐ด๐ฝ๐ถ๐ป๐ธ๐๐ท", "English"],
        "chi" : ["๐ฒ๐ท๐ธ๐ฝ๐ด๐๐ด", "Chinese"],
        "mal" : ["๐ผ๐ฐ๐ป๐ฐ๐๐ฐ๐ป๐ฐ๐ผ", "เดฎเดฒเดฏเดพเดณเด"],
        "uzb" : ["๐๐๐ฑ๐ด๐บ๐ธ๐๐๐ฐ๐ฝ", "O'zbekiston"],
        "hnd" : ["๐ท๐ธ๐ฝ๐ณ๐ธ", "เคนเคฟเคจเฅเคฆเฅ"],
        "rus" : ["๐๐๐๐๐ธ๐ฐ๐ฝ", "ััััะบะธะน"],
        "frn" : ["๐ต๐๐ด๐ฝ๐ฒ๐ท", "franรงaise"],
        "spn" : ["๐๐ฟ๐ฐ๐ฝ๐ธ๐๐ท", "espaรฑola"],
        "arb" : ["๐ฐ๐๐ฐ๐ฑ๐ธ๐ฒ", "ุนุฑุจู"]
    }

# Display Lang in a Beutiful Way
async def disLang(lang):
    if lang in langList:
        return langList[lang][0]
    else:
        return langList[settings.DEFAULT_LANG][0]

# ===================================================================================================================================[NABIL A NAVAB -> TG: nabilanavab]
