import random

def main():
    randlist = [16.2, 75.1, 52.3]
    for i in range(3):
        append_random_numbers(randlist, i)
        print(randlist)
    
    # stretch challenge
    randwords = []
    append_random_words(randwords, random.randint(1, 10))
    print(randwords)    

def append_random_numbers(numbers_list, quantity=1):
    randnums = numbers_list
    for _ in range(quantity):
        rand1 = round(random.uniform(0,100), 1)
        randnums.append(rand1)

def  append_random_words(words_list, quantity=1):
    rand_words = ['world', 'left', 'santino', 'yodel', 'endoplasmicreticulum', 'flummery', 'whipjack', 'violence', 'fool', 'belay']
    for _ in range(quantity):
        rand_word = random.choice(rand_words)
        words_list.append(rand_word)
    
main()