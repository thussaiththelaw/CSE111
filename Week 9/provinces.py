#Zak Law
#written 11/8/2021

#this code goes through a .txt file 
def main():
    #read and print the original file
    provinces_original = read_list('provinces.txt', True)
    print (provinces_original)
    print(' ')
    #read the file and replace the instances of 'AB' with 'Alberta'
    provinces = read_list('provinces.txt')
    print(provinces)

    #remove the first element from the list
    provinces.pop(0)

    #remove the last element from the list
    provinces.pop()

    #count how many times Alberta shows up in the modified list
    alberta_count = count_alberta(provinces)
    print(f'Alberta shows up {alberta_count} times in the modified list')



def read_list(file_name, original = False):
    provinces_list = []

    with open(file_name, 'rt') as text_file:
        if original == False:
            for line in text_file:
                line = line.rstrip()
                if line != 'AB':
                    provinces_list.append(line)
                elif line == 'AB':
                    full_name = 'Alberta'
                    provinces_list.append(full_name)
        else:
            for line in text_file:
                line = line.rstrip()
                provinces_list.append(line)
    return provinces_list

def count_alberta(provinces):
    number_of_albertas = 0
    for i in provinces:
        if i == 'Alberta':
            number_of_albertas += 1
    return number_of_albertas

main()