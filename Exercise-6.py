class Library:
    def __init__(self):
        self.no_of_books = 10
        self.books = ['munshi premchand', 'Why i killed gandhi', 'Anandwan', 'The C programing laungage',
                      'past and history of linux', 'machine learning', 'hitler', 'the brief history of time', 'coder', 'wings of fire']


class SecLibrary(Library):
    def __init__(self):
        Library.__init__(self)  # Initialize the parent class
        self.added_books = []

    def booklistinfo(self):
        for i in range(self.no_of_books):
            print(f'book {i + 1} : {self.books[i]}')

    def addbook(self):
        print('Enter name of your book:')
        namebook = input()
        self.added_books.append(namebook)
        self.no_of_books += 1
        self.books.append(namebook)

    def removebook(self):
        print('Enter index of the book to remove:')
        indexbook = int(input())
        if 0 <= indexbook < len(self.books):
            removed_book = self.books.pop(indexbook)
            print(f'"{removed_book}" has been removed from the library.')
            self.no_of_books -= 1
        else:
            print('Invalid index. Book removal failed.')


sec_lib = SecLibrary()
sec_lib.booklistinfo()
sec_lib.addbook()
sec_lib.booklistinfo()

sec_lib.removebook()
sec_lib.booklistinfo()
