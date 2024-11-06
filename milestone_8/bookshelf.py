class Book:
    def __init__(self, title_book, author_by_book, category):
        self.title_book = title_book
        self.author_by_book = author_by_book
        self.category = category

    def __repr__(self):
        return f'Назва книги: {self.title_book}, Автор: {self.author_by_book}'

book1 = Book('Іди туди, де страшно', 'Джим Лоулесс', 'Популярна психологія')
book2 = Book('Багатий тато, бідний тато', 'Роберт Кіосакі', 'Бізнес')
book3 = Book('Майстер і Маргарита', 'Михайло Булгаков', 'Світова класика')
book4 = Book('Думай і багатій', 'Наполеон Гілл', 'Бізнес')

class Shelf:
    def __init__(self):
        self.books = []  

    def add_book(self, book):
        self.books.append(book)  

    def sort_books(self):
        self.books.sort(key=lambda book: book.title_book)  

    def __repr__(self):
        categories = {}  
        for book in self.books:
            if book.category not in categories:
                categories[book.category] = []
            categories[book.category].append(book)

        result = []
        for category, books in categories.items():
            result.append(f"Категорія: {category}:\n" + "\n".join([f"    {i+1}: {book}" for i, book in enumerate(books)]))
        return "\n\n".join(result)  


class Bookshelf:
    def __init__(self):
        self.shelves = []  

    def add_shelf(self):
        shelf = Shelf()  
        self.shelves.append(shelf)  
        return shelf 

    def sort_shelves(self):
        for shelf in self.shelves:
            shelf.sort_books()  

    def __repr__(self):
        result = []
        for i, shelf in enumerate(self.shelves):
            result.append(f"Полиця {i+1}:\n" + str(shelf))  
        return "\n\n".join(result)  


bookshelf = Bookshelf()
shelf1 = bookshelf.add_shelf()
shelf1.add_book(book1)
shelf1.add_book(book2)
shelf1.add_book(book4)

shelf2 = bookshelf.add_shelf()
shelf2.add_book(book3)


bookshelf.sort_shelves()


print(bookshelf)


