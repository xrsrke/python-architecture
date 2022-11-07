from typing import Union, Optional


# class Book:
#     def __init__(self, name):
#         self.name = name

# class Library:
#     def __init__(self, items):
#         self.items = items


# book_ids = [1, 2, 3, 4]
# books = Book("Homo Sapiens")
# book_name = "Chemistry"

# lib_1 = Library(book_ids)
# lib_2 = Library(books)
# lib_3 = Library(book_name)

# class HotDog: pass

# class Pretzel: pass

# def dispense_snack(user_input: str) -> Union[HotDog, Pretzel]:
#     if user_input == "Hot Dog":
#         return 2
#     elif user_input == "Pretzel":
#         return 1
    
#     raise RuntimeError("Should never reach this code...")

# def place_order() -> Optional[HotDog]:
#     result = dispense_snack("Pretzel")
#     return result

from dataclasses import dataclass

@dataclass
class Snack:
    name: str
    condiments: set[str]
    error_code: int
    disposed_of: bool