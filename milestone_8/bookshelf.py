class Book:
    def __init__(self, title_book, author_by_book, category):

        self.title_book = title_book
        self.author_by_book = author_by_book
        self.category = category

    def __repr__(self):
        return f'Назва книги: {self.title_book},\nАвтор: {self.author_by_book}'
    
book1 = Book('Іди туди, де страшно', 'Джим Лоулесс', 'Популярна психологія')
book2 = Book('Багатий тато, бідний тато', 'Роберт Кіосакі', 'Бізнес')
book3 = Book('Майстер і Маргарита', 'Михайло Булгаков', 'Світова класика')
book4 = Book('Думай і багатій','Наполеон Гілл', 'Бізнес')

# book1
# book3



class Shelf:
    def __init__(self, category):
        self.category = category
        self.books = {} 
        self.book_counter = 1

    def add_book(self, book):
        if book.category == self.category:
            self.books[self.book_counter] = book
            self.book_counter += 1
        else:
            print (f'Книга {book.title_book} не відповідає категорії полиці {self.category}')

    def sort_book(self):
        self.books = dict(sorted(self.books.items(), key=lambda item: item[1].title_book))

    def __repr__(self):
        books_str = "\n".join(f"{num}: {book}" for num, book in self.books.items())
        return f'Категорія: {self.category},\nКниги: {books_str}'

# business_shelf = Shelf("Бізнес")
# business_shelf.add_book(book2)
# business_shelf.add_book(book4)
# business_shelf.add_book(book3)
# business_shelf.sort_book()
# print(business_shelf)

class Bookshelf:
    def __init__(self):
        self.book_by_category = {}

    def add_shelf(self, category):
        if category not in self.book_by_category:
              self.book_by_category[category] = Shelf(category)                    
        else:
             print (f'Категорія {category} вже існує') 

    def add_book_to_shelf(self, book):
        if book.category in self.book_by_category:
            self.book_by_category[book.category].add_book(book)
        else:
            print (f'Полиця для категорії {book.category} вже існує')

    def sort_shelf(self):
        for shelf in self.book_by_category.values():
            shelf.sort_book()
    
    def __repr__(self):
        shelves_str = "\n".join(f"{category}:\n{shelf}" for category, shelf in self.book_by_category.items())
        return f'Bookshelf:\n{shelves_str}'


bookshelf = Bookshelf()
bookshelf.add_shelf('Популярна психологія')
bookshelf.add_shelf('Світова класика')
bookshelf.add_shelf('Бізнес')

# Додаємо книги на відповідні полиці
bookshelf.add_book_to_shelf(book1)
bookshelf.add_book_to_shelf(book2)
bookshelf.add_book_to_shelf(book3)
bookshelf.add_book_to_shelf(book4)

# Сортуємо книги на полицях
bookshelf.sort_shelf()

print(bookshelf)



