from typing import Counter


url = "books/frankenstein.txt"


def main():
    with open(url) as f:
        text = f.read()
        #print (text)
        words = count_words(text)
        characters = sorted(count_charac(text),key=lambda x: x["count"], reverse=True)
        
        
        print (f" -- Begin Report of {url} --")
        print (f"{words} words found  in the document")
        print ()
        for item in characters:
            if not item["char"].isalpha():
                continue
            print(f"Character: {item['char']} appears {item['count']} times.")
            
        print(" -- End Report -- ")
            
    
def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count
    
def count_charac (text):
    lowered_string = text.lower()
    character_counter = Counter(lowered_string)
    list_of_charact = [{'char':char,'count':count}for char, count in character_counter.items()]
    #print (list_of_charact)
    return list_of_charact

main() 