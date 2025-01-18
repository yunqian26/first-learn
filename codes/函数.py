
def display_message():
    print('i learn how to use this type of sentence.')

def favorite_book(title):
    print('One of my favorite book is '+title.title())

def make_shirt(size='中号',word='I love Python'):
    print('The shirt is in the size of '+size+' with the word '+'"'+word+'"')

def describe_city(city_name,country='China'):
    print(city_name.title()+' is belong to '+country.title()+'.')

def make_album(singer_name,album_name):
    return{'singer_name':singer_name,'album_name':album_name}

def show_magicians(list_of_magicians):
    new_list=[]
    for magician in list_of_magicians:
        magician='The great ' + magician.title()
        new_list.append(magician)
    print(list_of_magicians)
    print(new_list)

def Car_message(car_name,car_company,**other_message):
    return{'car_name':car_name,'car_company':car_company,'other_message':other_message}

def main():
    display_message()
    favorite_book(input('Enter your favorite book title: '))
    make_shirt(input('Enter a word that on the shirt: '),input('Enter a size of the shirt: '))
    make_shirt(size='大号')
    describe_city(city_name=input('Please enter a city belong to china: '))
    singer_name = input('Please enter a singer name: ')
    dictionaries={}
    while singer_name!=' ':
       album_name = input('Please enter an album name: ')
       dictionary=make_album(singer_name,album_name)
       dictionaries[album_name]=dictionary
       singer_name = input('Please enter an singer name: (use space to break)')
    print(dictionaries)
    list_of_magician=[]
    new_magic=input('Enter a magician name: ')
    while new_magic!=' ':
        list_of_magician.append(new_magic)
        new_magic = input('Enter a magician name: (use space to break)')
    show_magicians(list_of_magician)
    cars=Car_message(input('Car name: '),input('Car company: '),color=input('Car color: '),seat=input('Car seat: '))
    print(cars)


if __name__ == '__main__':
    main()


