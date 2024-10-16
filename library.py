from abc import ABC, abstractmethod
class LibraryItem(ABC):
    def __init__(self,ID,title,author):
        self.ID=ID
        self.title=title
        self.author=author
    @abstractmethod
    def display_details(self):
        pass
    def __str__(self):
        return f'ID:{self.ID},title:{self.title},author:{self.author}'
class Book(LibraryItem):
    def __init__(self, ID, title, author,pages,genre):
        super().__init__(ID, title, author)
        self.pages=pages
        self.genre=genre
    def display_details(self):
        print(self.__str__())
    def __str__(self):
        return f'Book:{super().__str__()},pages:{self.pages},genre:{self.genre}'
class Magazine(LibraryItem):
    def __init__(self, ID, title,author, number,date):
        super().__init__(ID, title, author)
        self.number=number
        self.date=date
    def display_details(self):
        print(self.__str__())
    def __str__(self):
        return f'Magazine:{super().__str__()},num:{self.number},date:{self.date}'
class Article(LibraryItem):
    def __init__(self, ID, title, author,date,summary):
        super().__init__(ID, title, author)
        self.date=date
        self.summary=summary
    def display_details(self):
        print(self.__str__())
    def __str__(self):
        return f'Article:{super().__str__()},date:{self.date},sammary:{self.summary}'

if __name__ == "__main__":
    book=Book('book1','python program','john doe',300,'education')
    magazine=Magazine('m001','nature','jane smith','2024-09','2024-09-01')
    article=Article('a001','machine','alice janson','2024-10-01','summary michine learning')
    print(book)
    print(book.__dict__)
    print(magazine)
    print(magazine.__dict__)
    print(article)
    print(article.__dict__)
    book.display_details()
    magazine.display_details()
    article.display_details()
