import copy
from collections import OrderedDict


class Book:

    def __init__(self, name, authors, price, **rest):
        '''Examples of rest: publisher, length, tags, publication date'''

        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):        
        my_list = []
        ordered = OrderedDict(sorted(self.__dict__.items()))

        for key in ordered.keys():
            my_list.append('{}: {}'.format(key, ordered[key]))
            if key == 'price':
                my_list.append('PLN')
            my_list.append('\n')
        return ''.join(my_list)


class PrototypeFactory:
    pass # TODO


def main():
    book_c = Book('The C Programming Langauage', ('Brian W. Kernighan', 'Dennis M. Ritchie'), price=118, 
              publisher='Prentice Hall', length=228, publication_date='1978-02-22', 
              tags=('C', 'programming', 'algorithms', 'data', 'structures'))

    prototype = PrototypeFactory()

    book_id = 'k&r first'
    prototype.register(book_id, book_c) 

    cloned_book_c = prototype.clone(book_id)

    print("ID b1 : {} != ID b2 : {}".format(id(book_c), id(cloned_book_c)))

    print("=" * 60)
    
    for b in (book_c, cloned_book_c):
        print(b)


if __name__ == '__main__':
    main()