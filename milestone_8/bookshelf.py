class Book:
    def __init__(self, title_book, author_by_book, category):

        self.title_book = title_book
        self.author_by_book = author_by_book
        self.category = category

    def __repr__(self):
        return f'Назва книги: {self.title_book},\nАвтор: {self.author_by_book},\nКатегорія: {self.category}'
    
book1 = Book('Іди туди, де страшно', 'Джим Лоулесс', 'Популярна психологія')
book2 = Book('Багатий тато, бідний тато', 'Роберт Кіосакі', 'Бізнес')
book3 = Book('Майстер і Маргарита', 'Михайло Булгаков', 'Світова класика')


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
        dict(sorted(self.books.items(), key=lambda item: item[1].title_book))

    def __repr__(self):
        books_str = "\n".join(f"{num}: {book}" for num, book in self.books.items())
        return f'Категорія: {self.category},\nКниги: {self.books}'

business_shelf = Shelf("Бізнес")
business_shelf.add_book(book2)
business_shelf.add_book(book4)
business_shelf.add_book(book3)
business_shelf.sort_book()
print(business_shelf)



