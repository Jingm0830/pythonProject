"""
Implement the following class hierarchy using Python: A publication can be either a book or a magazine.
Each publication has a name. Each book also has an author and a page count,
whereas each magazine has a chief editor. Also write the required initializers to both classes.
Create a print_information method to both subclasses for printing out all information of the publication
n question. In the main program, create publications Donald Duck (chief editor Aki Hyyppä) and
Compartment No. 6 (author Rosa Liksom, 192 pages).
Print out all information of both publications using the methods you implemented.
"""
class Publications():
    def __init__(self,Publication_name):
        self.Publication_name= Publication_name
    def print_information(self):
        print(f"{self.Publication_name}")

class Magazine(Publications):
    def __init__(self, Publication_name, chief_editor):
        self.chief_editor=chief_editor
        super().__init__(Publication_name)
    def print_information(self):
        super().print_information()
        print(f"Chief editor: {self.chief_editor}")

class Book(Publications):
    def __init__(self, Publication_name, Author, Page_count):
        self.author=Author
        self.page_count=Page_count
        super().__init__(Publication_name)
    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}, Page count:{self.page_count}")

Publications = []
Publications.append(Magazine("Donald Duck", "Aki Hyyppä"))
Publications.append(Book("Compartment No. 6", "Rosa Liksom", "192 pages"))

for i in Publications:
    i.print_information()