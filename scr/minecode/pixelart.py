from PIL import Image
import math
import bed_apy
# Minecraft concrete RGB values
CONCRETE_COLORS = {
    "white": (207, 213, 214),
    "orange": (224, 97, 1),
    "magenta": (169, 48, 159),
    "light_blue": (36, 137, 199),
    "yellow": (249, 198, 40),
    "lime": (127, 204, 25),
    "pink": (235, 89, 179),
    "gray": (55, 58, 62),
    "light_gray": (125, 125, 115),
    "cyan": (21, 119, 136),
    "purple": (100, 32, 156),
    "blue": (45, 47, 143),
    "brown": (96, 60, 32),
    "green": (73, 91, 36),
    "red": (142, 33, 33),
    "black": (8, 10, 15)
}

def closest_concrete_color(pixel):
    """Finds the closest Minecraft concrete color to the given pixel."""
    def color_distance(c1, c2):
        return sum((c1[i] - c2[i]) ** 2 for i in range(3))  # Simple Euclidean distance
    
    return min(CONCRETE_COLORS.keys(), key=lambda color: color_distance(pixel, CONCRETE_COLORS[color]))

async def image_to_minecraft_commands(image_path, start_x, start_y, start_z):
    """Converts an image into Minecraft concrete blocks using setblock commands."""
    img = Image.open(image_path).convert("RGBA")  # Ensure transparency is handled
    width, height = img.size

    commands = []

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))

            # Handle transparency (alpha channel)
            if pixel[3] == 0:  # Fully transparent pixel
                block_type = "air"
            else:
                block_type = closest_concrete_color(pixel[:3])  # Ignore alpha, match RGB

            # Generate Minecraft command
            command = f"setblock {start_x + x} {start_y} {start_z + y} minecraft:{block_type}_concrete"
            await bed_apy.command(command)
