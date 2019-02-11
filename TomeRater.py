class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return self.name + "'s email address has been updated to " + address

    def __repr__(self):
        return "User " + self.name + " , email: " + self.email + " , books read: " + str(len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        sum_of_ratings = []
        total = 0
        for key, value in self.books.items():
            if value is not None:
                sum_of_ratings.append(value)
        for value in sum_of_ratings:
            total += value
        return round(total / len(sum_of_ratings), 1)


class Book:
    def __init__(self, title, isbn):
        self.title = title
        if int(isbn) > 0:
            self.isbn = isbn
        else:
            raise Exception("Invalid ISBN ")
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        if int(isbn) > 0:
            self.isbn = isbn
            print(self.title + " has had it's ISBN updated to: " + str(self.isbn))
        else:
            raise Exception("Invalid ISBN ")

    def add_rating(self, rating):
        if 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        sum_of_rating = []
        total = 0
        for rating in self.ratings:
            if rating is not None:
                sum_of_rating.append(rating)
        for rating in sum_of_rating:
            total += rating
        return round(total / len(sum_of_rating), 1)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            print("No user with email " + email)
        else:
            self.users[email].read_book(book, rating)
            if rating is not None:
                book.add_rating(rating)
                if book in self.books:
                    self.books[book] += 1
                else:
                    self.books[book] = 1

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[new_user.email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)
        return new_user

    def print_catalog(self):
        [print(Book.get_title(key)) for key in self.books.keys()]
        return

    def print_users(self):
        [print(value.name) for value in self.users.values()]
        return

    def most_read_book(self):
        count = 0
        for key, value in self.books.items():
            if value > count:
                book = Book.get_title(key)
                count = value
        return book

    def highest_rated_book(self):
        highest_rating = 0.0
        for key, value in self.books.items():
            rating = Book.get_average_rating(key)
            if rating > highest_rating:
                book = Book.get_title(key)
                highest_rating = rating
        return book

    def most_positive_user(self):
        highest_average_rating = 0.0
        for user in self.users.values():
            rating = User.get_average_rating(user)
            if rating > highest_average_rating:
                highest_average_rating = rating
                highest_user = user.name
        return highest_user

    def get_n_most_read_books(self, number):
        title_value = {}
        for key, value in self.books.items():
            rating = Book.get_average_rating(key)
            book = Book.get_title(key)
            highest_rating = rating
            title_value.update({book: highest_rating})
        most_read = dict(sorted(title_value.items(), key=lambda kv: kv[1], reverse=True))
        most_read_list = list(most_read)
        if number <= len(most_read):
            print("The top " + str(number) + " read books are:")
            for x in range(0, number):
                print(most_read_list[x])
            return
        else:
            print("You need to select a number between 1 and " + str(len(most_read)))
        return

    def get_n_most_prolific_readers(self, number):
        name_book_count = {}
        for user in self.users.values():
            name_book_count.update({user.name: len(user.books)})
        most_read = dict(sorted(name_book_count.items(), key=lambda kv:kv[1], reverse=True))
        most_read_list = list(most_read)
        if number <= len(most_read):
            print("The top " + str(number) + " readers are: ")
            for x in range(0, number):
                print(most_read_list[x])
            return
        else:
            print("You need to select a number between 1 and " + str(len(most_read)))
        return





