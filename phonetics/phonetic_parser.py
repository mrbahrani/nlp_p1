class PhoneticParser:
    @staticmethod
    def __create_meaningful_phonetic_ranges(phonetics_to_text: dict, phonetics: str):
        phonetic_maximum_length = max(map(len, phonetics_to_text))
        meaningful_phonetics_list = list()
        for length in range(phonetic_maximum_length):
            for start_index in range(len(phonetics) - length + 1):
                if phonetics[start_index:start_index + length] in phonetics_to_text:
                    meaningful_phonetics_list.append([start_index, start_index+length])
        return meaningful_phonetics_list

    @staticmethod
    def __find_all_sequences(graph, starts, stops, path, paths):
        for start_node in starts:
            if start_node in stops:
                path.append(start_node)
                paths.append(path[:])
            else:
                PhoneticParser.__find_all_sequences(graph, graph[start_node], stops, path+[start_node], paths)

    @staticmethod
    def __create_sentence_graph(meaningful_phonetics_ranges):
        sentence_graph = dict()
        for item in meaningful_phonetics_ranges:
            sentence_graph[tuple(item)] = []
            for neighbor_candidate in meaningful_phonetics_ranges:
                if item[1] == neighbor_candidate[0]:
                    sentence_graph[tuple(item)].append(tuple(neighbor_candidate))
        return sentence_graph

    @staticmethod
    def __path_to_phonetics(phonetics, path):
        phonetics_list = list()
        for node in path:
            phonetics_list.append(phonetics[node[0]: node[1]])
        return phonetics_list

    @staticmethod
    def __phonetics_list_to_text_list(phonetics_to_text, phonetics_list):
        all_possible_forms = [""]
        for phonetics in phonetics_list:
            new_all_possible_list = list()
            for word in phonetics_to_text[phonetics]:
                tmp_list = all_possible_forms
                for itr in range(len(tmp_list)):
                    new_all_possible_list.append(tmp_list[itr]+(word+ " "))
            all_possible_forms = new_all_possible_list
        return all_possible_forms

    @staticmethod
    def parse_phonetic_text(phonetic_to_text: dict, phonetic_text: str):
        meaningful_phonetic_ranges = PhoneticParser.__create_meaningful_phonetic_ranges(phonetic_to_text, phonetic_text)
        sentence_graph = PhoneticParser.__create_sentence_graph(meaningful_phonetic_ranges)
        start_list = []
        stop_list = []
        for node in sentence_graph:
                if node[0] == 0:
                    start_list.append(node)
                if node[1] == len(phonetic_text):
                    stop_list.append(node)
        paths = []
        path = []
        PhoneticParser.__find_all_sequences(sentence_graph, start_list, stop_list, path, paths)
        del path
        all_sentences_list = list()
        for path in paths:
            phonetic_list = PhoneticParser.__path_to_phonetics(phonetic_text, path)
            all_sentences_list += PhoneticParser.__phonetics_list_to_text_list(phonetic_to_text, phonetic_list)
        return all_sentences_list

    @staticmethod
    def parse_all(phonetics_to_text: dict, phonetics_text_list: list):
        answer = list()
        for phonetics in phonetics_text_list:
            answer += PhoneticParser.parse_phonetic_text(phonetics_to_text, phonetics)
        return answer
