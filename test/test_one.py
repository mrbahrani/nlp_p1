import sys
from phonetics.dictionary_generator import DictionaryGenerator
from phonetics.text_parser import TextParser
from phonetics.phonetic_parser import PhoneticParser
sys.setrecursionlimit(1000000)
if "--help" in sys.argv:
    print(
        """
        Hello
        The program asks for input itself
        You don't expect me to develop a full user-friendly application in a half of a day :(
        """
    )

entry = input("Enter the Entries paths (in csv format)")
persian_index = 1
phonetics_index = 0
text_to_phonetics = DictionaryGenerator.generate_from_csv_file(entry, 1, 0)
address = input("Enter input file")
input_sentence = open(address, "r", encoding="utf-8").read()
output_address = input("Enter output file")
output_file = open(output_address, "w", encoding="utf-8")
phonetics = TextParser.parse(text_to_phonetics, input_sentence)
phonetics_to_text = DictionaryGenerator.generate_from_csv_file(entry, 0, 1)
results_list = PhoneticParser.parse_all(phonetics_to_text, phonetics)
for item in results_list:
    output_file.write(item+"\n")
output_file.close()
