# Delete Operation

### __Instruction__ Delete the book you created and confirm the deletion by trying to retrieve all books again.

command:
from bookshelf.models import Book
>>> book.delete()

output:
>>> (1, {'bookshelf.Book': 1})
