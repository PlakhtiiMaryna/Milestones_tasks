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


