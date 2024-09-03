from typing import Counter


url = "books/frankenstein.txt"


def main():
    with open(url) as f:
        text = f.read()
        #print (text)
        count_words(text)
        count_charac(text)
        report(count_charac)
        return text
    
def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count
    
def count_charac (text):
    lowered_string = text.lower()
    character_counter = Counter(lowered_string)
    list_of_charact = [{count,char}for char, count in character_counter.items()]
    #print (list_of_charact)
    return list_of_charact

def report (list):
    order_list = list
    print(order_list)

main() 