from typing import Union
from dataclasses import dataclass
import json
import xml.etree.ElementTree as et
from dataclasses import dataclass

from attr import attr


@dataclass
class Book:
    id: int
    title: str
    author: str
    price: float

    def __str__(self) -> str:
        return f"Book(id={self.id}, title='{self.title}', author={self.author}, price={self.price})"


class BookSerializer:
    def serialize(self, book: Book, format: str):
        if format == 'JSON':
            book_properties = {
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'price': book.price
            }
            book_object = {'Book': book_properties}
            return json.dumps(book_object)
        elif format == 'XML':
            book_info = et.Element('book')
            id = et.SubElement(book_info, 'id')
            id.text = repr(book.id)
            title = et.SubElement(book_info, 'title')
            title.text = book.title
            author = et.SubElement(book_info, 'author')
            author.text = book.author
            price = et.SubElement(book_info, 'price')
            price.text = str(book.price)
            return et.tostring(book_info, encoding='unicode')
        else:
            raise ValueError(format)


def main():
    book_gof = Book(1, 'Design Patterns',
                    'Gamma Erich, Helm Richard, Johnson Ralph, Vlissides John', 34.01)
    print(book_gof)

    book_cpp = Book(2, 'Thinking in C++', 'Bruce Eckel', 10.1)
    print(book_cpp)

    book_serializer = BookSerializer()
    print(book_serializer.serialize(book_gof, "JSON"))
    print(book_serializer.serialize(book_cpp, "XML"))


if __name__ == "__main__":
    main()
