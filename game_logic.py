"""
Main game logic for Breakout Elite
"""

import time
import random
from config import *
from game_objects import PowerUp, GameState
from game_creation import (create_enhanced_bricks, create_enhanced_paddle, 
                          create_enhanced_ball, update_enhanced_paddle, 
                          create_powerup_visual, cleanup_turn)
from physics import (handle_wall_bounces, check_enhanced_collisions, 
                    handle_paddle_collision, check_ball_out_of_bounds, 
                    initialize_ball_velocity, update_powerups)
from visuals import (create_particle_explosion, update_particles, 
                    create_ui_elements, update_score_display, 
                    update_combo_display, add_ball_effects)


def play_turn(canvas, turn_number, current_score):
    """Play a single turn of the game with enhanced features"""
    # Initialize game state
    game_state = GameState()
    
    # Create UI elements
    score_text, turn_text, combo_text = create_ui_elements(canvas, turn_number, current_score)
    
    # Set up the game objects
    bricks = create_enhanced_bricks(canvas)
    paddle = create_enhanced_paddle(canvas)
    ball = create_enhanced_ball(canvas)
    
    game_state.bricks_remaining = len(bricks)
    
    # Initialize ball velocity
    change_x, change_y = initialize_ball_velocity(game_state.ball_speed_multiplier)
    
    # Game loop
    frame_count = 0
    
    while True:
        frame_count += 1
        
        # Move the ball
        ball_main, ball_highlight = ball
        canvas.move(ball_main, change_x, change_y)
        canvas.move(ball_highlight, change_x, change_y)
        
        # Update paddle position
        paddle = update_enhanced_paddle(canvas, paddle, game_state.paddle_size_multiplier)
        
        # Check for bounces off walls
        change_x, change_y = handle_wall_bounces(canvas, ball, change_x, change_y)
        
        # Check if ball hit bottom wall (game over condition)
        if check_ball_out_of_bounds(canvas, ball):
            cleanup_turn(canvas, bricks, paddle, ball, game_state.particles, 
                        game_state.powerups, [score_text, turn_text, combo_text])
            return game_state.score
        
        # Check for collisions
        collision_result, hit_row = check_enhanced_collisions(canvas, ball, paddle, bricks)
        
        if collision_result == "paddle":
            # Handle paddle collision with spin effect
            change_x, change_y = handle_paddle_collision(
                canvas, ball, paddle, game_state.paddle_size_multiplier, change_x, change_y)
            game_state.reset_combo()
            
        elif collision_result == "brick":
            # Handle brick collision
            brick_score = BRICK_SCORES[hit_row] if hit_row < len(BRICK_SCORES) else 30
            game_state.add_score(brick_score)
            
            # Create particle explosion
            ball_main, ball_highlight = ball
            ball_x = canvas.get_left_x(ball_main) + BALL_RADIUS
            ball_y = canvas.get_top_y(ball_main) + BALL_RADIUS
            create_particle_explosion(canvas, game_state.particles, ball_x, ball_y)
            
            # Chance to spawn power-up
            if random.random() < POWER_UP_CHANCE:
                powerup = PowerUp(ball_x, ball_y, random.choice(["expand", "speed", "multi"]))
                create_powerup_visual(canvas, powerup)
                game_state.powerups.append(powerup)
            
            change_y = -change_y
            game_state.bricks_remaining -= 1
            
            # Update displays
            score_text = update_score_display(canvas, score_text, current_score + game_state.score)
            combo_text = update_combo_display(canvas, combo_text, game_state.combo)
            
            # Check win condition
            if game_state.bricks_remaining == 0:
                # Bonus for clearing all bricks
                game_state.score += 1000
                cleanup_turn(canvas, bricks, paddle, ball, game_state.particles, 
                           game_state.powerups, [score_text, turn_text, combo_text])
                return -1  # Special value indicating game won
        
        # Update particles
        update_particles(canvas, game_state.particles)
        
        # Update powerups
        game_state.paddle_size_multiplier, game_state.ball_speed_multiplier = update_powerups(
            canvas, game_state.powerups, paddle, 
            game_state.paddle_size_multiplier, game_state.ball_speed_multiplier)
        
        # Add visual effects to ball
        add_ball_effects(canvas, ball, frame_count)
        
        time.sleep(0.016)  # ~60 FPS