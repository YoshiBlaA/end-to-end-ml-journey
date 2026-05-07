"""
Write a function that receives an initial greeting and then multiple names, printing a customized greeting per each one.

Example:
massive_greeting("Hi!", "Ana", "Luis", "María")
Salida:
Hi!, Ana!
Hi!, Luis!
Hi!, Maria!
"""

def massive_greeting(custom_greeting, *args):
    for name in args:
        print(f"{custom_greeting}, {name}!")

names = ("Ana", "Luis", "Maria")

massive_greeting("Hi!", *names)