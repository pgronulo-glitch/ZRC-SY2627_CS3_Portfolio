
class Publication:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title: str):
        self.__title = title

    def set_author(self, author: str):
        self.__author = author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title: str, author: str, number_pages: int):
        Publication.__init__(self, title, author)
        self.__number_of_pages = None
        self.set_number_of_pages(number_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_pages: int):
        if number_pages > 0:
            self.__number_of_pages = number_pages
        else:
            print("Number of pages must be positive.")

    def display_info(self):
        Publication.display_info(self)

class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):
        Publication.__init__(self, title, author)
        self.__issue_number = None
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return f"Issue number: {self.__issue_number}"

    def set_issue_number(self, issue_number: int):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("Issue number must be positive.")

    def display_info(self):
        Publication.display_info(self)

pub1 = Publication(
    "Journal of Experimental Psychology",
    "Ratchiff, R. & Van Dongen, H."
)
pub2 = Publication("The Science of Everything", "John Smith")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1178)

mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("TIME", "Various Authors", 150)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print("Number of pages:", book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())

print("\nPublication Information:")
pub2.display_info()

print("\nBook Information:")
book2.set_number_of_pages(-310)
book2.display_info()
print("Number of pages:", book2.get_number_of_pages())

print("\nMagazine Information:")
mag2.display_info()
print(mag2.get_issue_number())
