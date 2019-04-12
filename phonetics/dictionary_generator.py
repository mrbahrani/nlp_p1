class DictionaryGenerator:
    def __init__(self):
        pass

    @staticmethod
    def remove_double_quotation(text: str):
        if text[0] == "\"" or text[0] == "\'":
            text = text[1:]
        if text[-1] == "\"" or text[-1] == "\'":
            text = text[:len(text) - 1]
        return text

    @staticmethod
    def generate_from_csv_file(csv_file: str, key_index: int, value_index: int):
        csv_file_stream = open(csv_file, "r", encoding="utf-8")
        converting_dictionary = dict()
        for entry in csv_file_stream:
            entry_list = list(map(DictionaryGenerator.remove_double_quotation, entry.split(",")))
            if not (entry_list[key_index] in converting_dictionary):
                converting_dictionary[entry_list[key_index]] = {entry_list[value_index]}
            else:
                converting_dictionary[entry_list[key_index]] = \
                    converting_dictionary[entry_list[key_index]].union({entry_list[value_index]})
        return converting_dictionary
