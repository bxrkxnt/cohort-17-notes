import random

class Book:

    def __init__(self, title: str, author: str, genre: str):
        if author == "Dan Simmons":
            raise ValueError("Monster. Monster!")
        if genre == "Romance":
            raise ValueError("Banned by the state. All books nearby must be burnt")
        self.title = title
        self.author = author
        self.genre = genre
        self.current_page = 0
        self.max_pages = 412
        self._reviews = []

    def turn_page(self):
        if self.current_page <= self.max_pages:
            self.current_page += 1

    @property
    def review(self):
        return random.choice(self._reviews)
        
    @review.setter
    def review(self, user_review):
        self._reviews.append(user_review)

if __name__ == "__main__":
    b = Book("The Return of the King", "J. R. R. Tolkien", "high fantasy")

    books = []

    for b in [
        ("Hyperion", "Dan Simmons", "Travel"),
        ("Charlie and the Chocolate Factory", "Roald Dahl", "Self-help"),
        ("The Mist", "Stephen King", "Romance")
    ]:
        try:
            books.append(Book(b[0], b[1], b[2]))
        except ValueError as e:
        # except: raise ValueError
            print("Caught an error!")
            if str(e) == "Monster. Monster!":
                print("Unable to add book:", b)
            else:
                raise e

    print(books)