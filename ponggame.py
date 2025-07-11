import pygame
import random
import sys

# Game window dimensions
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# Color definitions (Red, Green, Blue)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)

def main():
    # Set up the game window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong Game")
    
    # Control game speed
    clock = pygame.time.Clock()
    
    # Track game status
    started = False
    game_over = False
    winner = ""
    bot_mode = False  # AI opponent for single player
    game_mode_selected = False  # Player has chosen game mode
    
    # Create paddles (left and right)
    paddle_1_rect = pygame.Rect(30, SCREEN_HEIGHT // 2 - 50, 7, 100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2 - 50, 7, 100)
    
    # Track paddle movement speed
    paddle_1_move = 0
    paddle_2_move = 0
    
    # Create ball in center
    ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)
    
    # Set initial ball speed
    ball_accel_x = random.randint(3, 6) * 0.1  # Regular speed
    ball_accel_y = random.randint(3, 6) * 0.1  # Regular speed
    
    # Speed control system
    speed_multiplier = 1.0  # Normal speed
    max_speed_multiplier = 2.5  # Maximum speed limit
    speed_increase_per_hit = 0.1  # Speed increase per paddle hit
    
    # Randomize ball direction
    if random.randint(1, 2) == 1:
        ball_accel_x *= -1
    if random.randint(1, 2) == 1:
        ball_accel_y *= -1
    
    # Main game loop
    while True:
        # Clear screen to black
        screen.fill(COLOR_BLACK)
        
        # Get time since last frame for smooth movement
        delta_time = clock.tick(60)
        
        # Check for keyboard and mouse events
        for event in pygame.event.get():
            # Handle key presses
            if event.type == pygame.KEYDOWN:
                # Player 1 controls (W/S keys)
                if event.key == pygame.K_w:
                    paddle_1_move = -0.5  # Move up
                if event.key == pygame.K_s:
                    paddle_1_move = 0.5   # Move down

                # Player 2 controls (Arrow keys)
                if event.key == pygame.K_UP:
                    paddle_2_move = -0.5  # Move up
                if event.key == pygame.K_DOWN:
                    paddle_2_move = 0.5   # Move down
                
                # Space bar actions
                if event.key == pygame.K_SPACE:
                    if game_over:
                        # Reset everything for new game
                        started = False
                        game_over = False
                        winner = ""
                        game_mode_selected = False
                        speed_multiplier = 1.0  # Reset speed to normal
                        
                        # Put ball back in center
                        ball_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                        
                        # Give ball new random direction
                        ball_accel_x = random.randint(3, 6) * 0.1  # Regular speed
                        ball_accel_y = random.randint(3, 6) * 0.1  # Regular speed
                        if random.randint(1, 2) == 1:
                            ball_accel_x *= -1
                        if random.randint(1, 2) == 1:
                            ball_accel_y *= -1
                        
                        # Reset speed to normal
                        speed_multiplier = 1.0
                    else:
                        started = True  # Start the game
                        speed_multiplier = 1.0  # Ensure normal starting speed
                
                # Choose game mode before starting
                if not game_mode_selected and not started:
                    if event.key == pygame.K_1:
                        bot_mode = True      # Single player vs AI
                        game_mode_selected = True
                        speed_multiplier = 1.0  # Reset speed for new game
                    elif event.key == pygame.K_2:
                        bot_mode = False     # Two player mode
                        game_mode_selected = True
                        speed_multiplier = 1.0  # Reset speed for new game

            # Handle key releases (stop movement)
            if event.type == pygame.KEYUP:
                # Stop paddle 1 when W or S is released
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle_1_move = 0.0
                # Stop paddle 2 when arrow keys are released
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle_2_move = 0.0

            # Close game window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Update paddle positions
        paddle_1_rect.top += paddle_1_move * delta_time
        paddle_2_rect.top += paddle_2_move * delta_time
        
        # Keep paddles inside screen boundaries
        if paddle_1_rect.top < 0:
            paddle_1_rect.top = 0
        if paddle_1_rect.bottom > SCREEN_HEIGHT:
            paddle_1_rect.bottom = SCREEN_HEIGHT

        if paddle_2_rect.top < 0:
            paddle_2_rect.top = 0
        if paddle_2_rect.bottom > SCREEN_HEIGHT:
            paddle_2_rect.bottom = SCREEN_HEIGHT
        
        # AI controls paddle 2 in single player mode
        if bot_mode and started and not game_over:
            # Only move AI when ball is coming towards it
            if ball_accel_x > 0:  # Ball moving right (towards AI)
                # Calculate when ball will reach AI paddle
                distance_to_paddle = paddle_2_rect.left - ball_rect.right
                time_to_reach = distance_to_paddle / ball_accel_x if ball_accel_x != 0 else 0
                
                # Predict where ball will be when it reaches paddle
                predicted_y = ball_rect.top + (ball_accel_y * time_to_reach)
                
                # Add less randomness for more reliable first hits
                predicted_y += random.randint(-10, 10)  # Reduced randomness
                
                # Move AI paddle towards predicted ball position
                paddle_center = paddle_2_rect.centery
                if predicted_y < paddle_center - 5:  # Smaller tolerance for more accuracy
                    paddle_2_move = -0.4  # Slightly faster movement
                elif predicted_y > paddle_center + 5:
                    paddle_2_move = 0.4   # Slightly faster movement
                else:
                    paddle_2_move = 0.0   # Stay still
            else:
                # Ball moving away, return to center
                paddle_center = paddle_2_rect.centery
                screen_center = SCREEN_HEIGHT // 2
                if paddle_center < screen_center - 10:
                    paddle_2_move = 0.2
                elif paddle_center > screen_center + 10:
                    paddle_2_move = -0.2
                else:
                    paddle_2_move = 0.0
        
        # Show menu screens before game starts
        if not started:
            # Set up text display
            font = pygame.font.SysFont('Consolas', 30)
            
            if not game_mode_selected:
                # Show game mode selection menu
                title_text = font.render('PONG GAME', True, COLOR_WHITE)
                title_rect = title_text.get_rect()
                title_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60)
                screen.blit(title_text, title_rect)
                
                mode1_text = font.render('Press 1 for Single Player (vs AI)', True, COLOR_WHITE)
                mode1_rect = mode1_text.get_rect()
                mode1_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                screen.blit(mode1_text, mode1_rect)
                
                mode2_text = font.render('Press 2 for Multiplayer (2 Players)', True, COLOR_WHITE)
                mode2_rect = mode2_text.get_rect()
                mode2_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)
                screen.blit(mode2_text, mode2_rect)
            else:
                # Show selected mode and start instruction
                mode_text = font.render('Single Player vs AI' if bot_mode else 'Two Player Mode', True, COLOR_WHITE)
                mode_rect = mode_text.get_rect()
                mode_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)
                screen.blit(mode_text, mode_rect)
                
                start_text = font.render('Press Space to Start', True, COLOR_RED)
                start_rect = start_text.get_rect()
                start_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)
                screen.blit(start_text, start_rect)
                
                # Show control instructions
                if bot_mode:
                    controls_text = font.render('Player 1: W/S keys', True, COLOR_WHITE)
                else:
                    controls_text = font.render('Player 1: W/S keys | Player 2: Up/Down arrows', True, COLOR_WHITE)
                controls_rect = controls_text.get_rect()
                controls_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
                screen.blit(controls_text, controls_rect)
            
            # Update screen and skip rest of game logic
            pygame.display.flip()
            continue
        
        # Check if ball went out of bounds (game over)
        if ball_rect.left <= 0 or ball_rect.left >= SCREEN_WIDTH:
            game_over = True
            winner = "Player 2 Wins!" if ball_rect.left <= 0 else "Player 1 Wins!"
        
        # Show game over screen
        if game_over:
            # Set up text display
            font = pygame.font.SysFont('Consolas', 30)
            
            # Show winner
            winner_text = font.render(winner, True, COLOR_WHITE)
            winner_rect = winner_text.get_rect()
            winner_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)
            screen.blit(winner_text, winner_rect)
            
            # Show restart instruction
            restart_text = font.render('Press Space to Restart', True, COLOR_RED)
            restart_rect = restart_text.get_rect()
            restart_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)
            screen.blit(restart_text, restart_rect)
            
            # Update screen and skip rest of game logic
            pygame.display.flip()
            continue
        
        # Ball bounces off top and bottom walls
        if ball_rect.top < 0:
            ball_accel_y *= -1  # Reverse vertical direction
            ball_rect.top = 0
        if ball_rect.bottom > SCREEN_HEIGHT:
            ball_accel_y *= -1  # Reverse vertical direction
            ball_rect.bottom = SCREEN_HEIGHT
        
        # Ball bounces off paddles
        # Check collision with left paddle (moving right)
        if paddle_1_rect.colliderect(ball_rect) and ball_accel_x < 0:
            ball_accel_x *= -1  # Reverse horizontal direction
            ball_rect.left = paddle_1_rect.right  # Move ball outside paddle
        
        # Check collision with right paddle (moving left)
        if paddle_2_rect.colliderect(ball_rect) and ball_accel_x > 0:
            ball_accel_x *= -1  # Reverse horizontal direction
            ball_rect.right = paddle_2_rect.left  # Move ball outside paddle
        
        # Update ball position
        ball_rect.left += ball_accel_x * delta_time
        ball_rect.top += ball_accel_y * delta_time
        
        # Draw game objects
        pygame.draw.rect(screen, COLOR_BLUE, paddle_1_rect)   # Blue left paddle
        pygame.draw.rect(screen, COLOR_RED, paddle_2_rect)    # Red right paddle
        pygame.draw.rect(screen, COLOR_WHITE, ball_rect)      # White ball
        
        # Update the display
        pygame.display.update()

if __name__ == "__main__":
    main()