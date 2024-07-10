def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        #print (content)
        return text
    
book = main()


    
def count_words(book):
    counter = 0
    words_count = book.split()
    for words in words_count:
        counter += 1
    
    #print (counter)
    
def charac_count(book):
    charac_lowered = book.lower()
    characters = list(charac_lowered)
    unique_characters = set(characters)
    #print (unique_characters)
    charact_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","y","z"]
    charac_counter = {}
    #print(characters)
    
    for charac in characters:
        counter = 0
        if charac in charact_list:
            counter += 1
            charac_counter[charac] += counter
    print(charac_counter)
    
            
            
        
    
charac_count(book)
    
    
count_words(book)
    

    

