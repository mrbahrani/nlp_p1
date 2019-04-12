class TextParser:
    @staticmethod
    def parse(text_to_phonetic, text: str):
        all_possible_phonetics = [""]
        word_list = text.split(" ")
        for word in word_list:
            new_all_possible_list = list()
            for phonetic in text_to_phonetic[word]:
                tmp_list = all_possible_phonetics[:]
                for itr in range(len(tmp_list)):
                    new_all_possible_list.append(tmp_list[itr] + phonetic)
            all_possible_phonetics = new_all_possible_list
        return all_possible_phonetics
