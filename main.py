import sys
import time

def print_typewriter(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

print_typewriter("Welcome to the game")
input("select a game to play('r' for rock paper scissors):")
