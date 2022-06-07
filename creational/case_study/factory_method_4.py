from abc import ABC, abstractmethod
from typing import Any, Union
from dataclasses import dataclass
import json
import xml.etree.ElementTree as et
import yaml


class Serializer(ABC):
    @abstractmethod
    def start_object(self, object_name: str):
        pass

    @abstractmethod
    def add_property(self, name: str, value: Any):
        pass

    @abstractmethod
    def to_str(self):
        pass


class JsonSerializer:
    def __init__(self):
        self._current_object = None
        self._properties = {}

    def start_object(self, object_name: str):
        self._current_object = {
            object_name: self._properties
        }

    def add_property(self, name, value):
        self._properties[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class YamlSerializer(JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)


class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name):
        self._element = et.Element(object_name)

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = repr(value)

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')


class SerializerFactory:

    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()


factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)
factory.register_format('YAML', YamlSerializer)


class ObjectSerializer:
    def serialize(self, serializable: Any, format: str):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()


@dataclass
class Book:
    id: int
    title: str
    author: str
    price: float

    def __str__(self) -> str:
        return f"Book(title='{self.title}', author={self.author}, price={self.price})"

    def serialize(self, serializer: Serializer):
        serializer.start_object('Book')
        serializer.add_property('id', self.id)
        serializer.add_property('title', self.title)
        serializer.add_property('author', self.author)
        serializer.add_property('price', self.price)


def main():
    book_gof = Book(1, 'Design Patterns',
                    'Gamma Erich, Helm Richard, Johnson Ralph, Vlissides John', 34.01)
    print(book_gof)

    book_cpp = Book(2, 'Thinking in C++', 'Bruce Eckel', 10.1)
    print(book_cpp)

    serializer = ObjectSerializer()
    print(serializer.serialize(book_gof, "JSON"))
    print(serializer.serialize(book_cpp, "XML"))
    print(serializer.serialize(book_cpp, "YAML"))


if __name__ == "__main__":
    main()
