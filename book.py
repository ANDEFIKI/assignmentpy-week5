class Book:
    def __init__(self, title, author, pages):
        self._title = title            # Encapsulated attribute
        self._author = author          # Encapsulated attribute
        self._pages = pages
        self._is_checked_out = False

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_pages(self):
        return self._pages

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return f"{self._title} checked out."
        return f"{self._title} is already checked out."

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return f"{self._title} returned."
        return f"{self._title} was not checked out."

    def __str__(self):
        return f"'{self._title}' by {self._author} ({self._genre}, {self._pages} pages)"

# Inheritance layer: EBook subclass
class EBook(Book):
    def __init__(self, title, author, pages, genre, file_size_mb):
        super().__init__(title, author, pages, genre)
        self._file_size_mb = file_size_mb

    def get_file_size(self):
        return self._file_size_mb

    # Polymorphism: override check_out method
    def check_out(self):
        return f"EBook '{self._title}' downloaded."

    def __str__(self):
        return f"EBook: '{self._title}' by {self._author} ({self._genre}, {self._pages} pages, {self._file_size_mb}MB)"