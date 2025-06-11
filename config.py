"""
Game configuration constants and settings
"""

# Canvas dimensions
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 700

# Paddle settings
PADDLE_Y = CANVAS_HEIGHT - 50
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

# Ball settings
BALL_RADIUS = 8
BALL_SPEED = 7

# Brick settings
BRICK_GAP = 3
BRICK_WIDTH = (CANVAS_WIDTH - BRICK_GAP * 11) / 10
BRICK_HEIGHT = 15
BRICK_ROWS = 8
BRICK_COLS = 10
BRICK_Y_OFFSET = 80

# Game settings
TURNS_PER_GAME = 3
POWER_UP_CHANCE = 0.15

# Scoring system
BRICK_SCORES = [100, 90, 80, 70, 60, 50, 40, 30]  # Points per row

# Color schemes - Universal colors that work on both light and dark backgrounds
BRICK_COLORS = [
    "#DC2626",
    "#EF4444",  # Strong red variants
    "#EA580C",
    "#F97316",  # Orange variants
    "#D97706",
    "#F59E0B",  # Amber variants
    "#059669",
    "#10B981",  # Emerald variants
]

# Particle effects - vibrant but not too bright
PARTICLE_COLORS = ["#F59E0B", "#F97316", "#EF4444", "#10B981", "#3B82F6"]

# Universal UI colors
UI_COLORS = {
    "text_primary": "#1F2937",  # Dark gray for light mode, readable on light bg
    "text_secondary": "#4B5563",  # Medium gray
    "text_accent": "#059669",  # Emerald for important text
    "text_warning": "#DC2626",  # Red for warnings/game over
    "text_success": "#059669",  # Green for success
    "ball_main": "#3B82F6",  # Blue - visible on both backgrounds
    "ball_highlight": "#60A5FA",  # Lighter blue
    "paddle_main": "#6B7280",  # Medium gray
    "paddle_highlight": "#9CA3AF",  # Light gray
    "background_accent": "#F3F4F6",  # Very light gray for accents
}

# Star colors for background
STAR_COLORS = [
    "#9CA3AF",
    "#6B7280",
    "#4B5563",
]  # Gray variants that work on both backgrounds

# Power-up colors
POWERUP_COLORS = {
    "expand": "#3B82F6",
    "speed": "#DC2626",
    "multi": "#7C3AED",  # Purple that works on both backgrounds
}

# Power-up symbols
POWERUP_SYMBOLS = {"expand": "⬌", "speed": "⚡", "multi": "✦"}
