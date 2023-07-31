import unittest
from booklover import booklover
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        book1 = book_lover("Quinn", "qdg9xwb@virginia.edu", "Contemporary")
        title = "My Year of Rest and Relaxation"
        book1.add_book(title, 4)
        self.assertEqual(title, book1.book_list['book_name'][0])
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        book1 = book_lover("Quinn", "qdg9xwb@virginia.edu", "Contemporary")
        title = "My Year of Rest and Relaxation"
        book1.add_book(title, 4)
        book1.add_book(title, 4)
        print(book1.book_list)
        expected = 1
        self.assertEqual(len(book1.book_list), expected)
        

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        book1 = book_lover("Quinn", "qdg9xwb@virginia.edu", "Contemporary")
        title = "My Year of Rest and Relaxation"
        book1.add_book(title, 4)
        truebook = book1.has_read(title)
        self.assertTrue(truebook)
        

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        book1 = book_lover("Quinn", "qdg9xwb@virginia.edu", "Contemporary")
        title = "My Year of Rest and Relaxation"
        book1.add_book(title, 4)
        falsebook = book1.has_read("Pride and Predjudice")
        self.assertFalse(falsebook)

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        book1 = book_lover("Quinn", "qdg9xwb@virginia.edu", "Contemporary")
        book1.add_book("My Year of Rest and Relaxation", 4)
        book1.add_book("Play It As It Lays", 5)
        book1.add_book("It Ends With Us", 1)
        expected = 3
        actual = len(book1.book_list)
        self.assertEqual(expected, actual)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        book1 = book_lover("Quinn", "qdg9xwb@virginia.edu", "Contemporary")
        book1.add_book("My Year of Rest and Relaxation", 4)
        book1.add_book("Play It As It Lays", 5)
        book1.add_book("It Ends With Us", 1)
        expected = 2
        actual = len(book1.fav_books())
        self.assertEqual(expected, actual)
        

if __name__ == '__main__':

    unittest.main(verbosity=3)