"""Practica de lambda sorting"""
import functools

health = 10

people = [
    ("Jason", "McDonald"),
    ("Denis", "Pobedrya"),
    ("Daniel", "Foerster"),
    ("Jaime", "López"),
    ("James", "Beecham")
]

by_last_name = sorted(people, key=lambda x: x[1])
print(by_last_name)


def function_1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if health <= 0:
            print("Too week")
            return
        result = func(*args, **kwargs)
        print("Health")
        return result
    return wrapper
