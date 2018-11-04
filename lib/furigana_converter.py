import MeCab

class FuriganaConverter():
    def __init__(self):
        self.mecab = MeCab.Tagger("-Ochasen -d /usr/local/mecab/lib/mecab/dic/mecab-ipadic-neologd")
        
    def get_furigana(self, text):
        analyzed = self.morphological_analysis(text)
        furigana_list = self.parse_to_list(analyzed)
        furigana = self.aggregate_furigana(''.join(furigana_list))
        return self.aggregate_furigana(furigana)

    def morphological_analysis(self, text):
        return self.mecab.parse(text)

    def parse_to_list(self, text):
        splited = text.split("\n")
        tab_splited = [el.split("\t") for el in splited]
        furiganas = [word_el[1] for word_el in tab_splited if len(word_el) >= 2]
        return furiganas

    def aggregate_furigana(self, furigana):
        symbols = ["。", "、", ",", ".", "!", "?", "！", "？"]
        for symbol in symbols:
            furigana = furigana.replace(symbol, "")
        return furigana
