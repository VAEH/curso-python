import random

def read_words():
    #words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        words = [word.strip() for word in f]
        return words

def aleatorio(word): 
    return random.choice(word)
    
    #num_word= len(read_words())
def word_incog():
    pass 

def run():
    word = aleatorio(read_words())
    print(word)
    #aleatorio()
    

if __name__=="__main__":
    run()