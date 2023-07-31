import pandas as pd
class book_lover:

    #constructor
    def __init__(self, name, email, fav_genre, book_list = None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]}) if book_list is None else book_list
        
    #method 1
    def add_book(self, book_name, book_rating):
        if book_name in self.book_list['book_name']:
            print('This book is already in the book list')
            return False
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]})
            
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
    
    #method 2
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            print('This book has already been read')
            return True
        if book_name not in self.book_list['book_name'].values:
            print('This book has not been read yet')
            return False
    
    #method 3
    def num_books_read(self):
        num_books = len(self.book_list)
        return num_books
    
    #method 4
    def fav_books(self):
        good_books = self.book_list[self.book_list['book_rating'] > 3]
        return good_books