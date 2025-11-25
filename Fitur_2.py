import os
import sys
import time
import random

if os.name == "nt":
    import msvcrt
    def get_key():
        if msvcrt.kbhit():
            return msvcrt.getch().decode('utf-8').lower()
        return None
else:
    import tty
    import termios
    import select

    def get_key():
        dr, dw, de = select.select([sys.stdin], [], [], 0)
        if dr:
            return sys.stdin.read(1).lower()
        return None


WIDTH = 40
HEIGHT = 20
SPEED = 0.1 

snake = [(10, 5), (9, 5), (8, 5)]
direction = "d"
food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
score = 0

def draw():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"SNAKE GAME  |  SCORE: {score}")
    print("=" * WIDTH)

    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if (x, y) == snake[0]:
                row += "@" 
            elif (x, y) in snake:
                row += "o" 
            elif (x, y) == food:
                row += "*" 
            else:
                row += " "
        print(row)
    print("=" * WIDTH)
    print("Controls: W A S D | Ctrl+C to exit")

try:
    while True:
        draw()
        time.sleep(SPEED)
        key = get_key()
        if key in ("w", "a", "s", "d"):
            if (direction, key) not in [("w", "s"), ("s", "w"),
                                        ("a", "d"), ("d", "a")]:
                direction = key
        head_x, head_y = snake[0]

        if direction == "w": head_y -= 1
        if direction == "s": head_y += 1
        if direction == "a": head_x -= 1
        if direction == "d": head_x += 1

        new_head = (head_x, head_y)
        if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in snake
        ):
            draw()
            print("\nGAME OVER! Kamu menabrak!")
            print(f"Final Score: {score}")
            break
        
        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
        else:
            snake.pop()

except KeyboardInterrupt:
    print("\nKeluar dari game.")
    sys.exit()
