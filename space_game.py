pip install pgzero


	3.	Make a file called space_game.py.

2. Paste this code into space_game.py

import random

WIDTH  = 800
HEIGHT = 600

# Player ship (a simple rectangle)
ship_x = WIDTH // 2
ship_y = HEIGHT - 50
ship_speed = 6

# Falling asteroid
ast_x = random.randint(0, WIDTH)
ast_y = -40
ast_speed = 4

game_over = False

def update():
    global ship_x, ast_x, ast_y, game_over

    if game_over:
        return

    # Move ship with arrow keys
    if keyboard.left:
        ship_x -= ship_speed
    if keyboard.right:
        ship_x += ship_speed

    # Keep ship on screen
    ship_x = max(40, min(WIDTH - 40, ship_x))

    # Move asteroid down
    ast_y += ast_speed

    # If asteroid goes off screen, reset it
    if ast_y > HEIGHT + 40:
        ast_y = -40
        ast_x = random.randint(0, WIDTH)

    # Simple collision check
    if abs(ship_x - ast_x) < 40 and abs(ship_y - ast_y) < 40:
        game_over = True

def draw():
    screen.clear()
    screen.fill((0, 0, 20))  # dark space color

    # Title
    screen.draw.text("SPACE DODGE", center=(WIDTH//2, 30),
                     fontsize=48, color="white")

    # Draw ship (a bright rectangle)
    screen.draw.filled_rect(Rect((ship_x - 30, ship_y - 10), (60, 20)), "cyan")

    # Draw asteroid (a gray circle)
    screen.draw.filled_circle((ast_x, ast_y), 25, "gray")

    if game_over:
        screen.draw.text("BOOM! GAME OVER",
                         center=(WIDTH//2, HEIGHT//2),
                         fontsize=64, color="red")
        screen.draw.text("Press ESC to quit",
                         center=(WIDTH//2, HEIGHT//2 + 60),
                         fontsize=32, color="white")
