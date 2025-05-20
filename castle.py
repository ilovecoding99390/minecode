
import Shapes
async def build_castle_plane(p1, p2, material="minecraft:stone_bricks"):
    """Creates a flat castle wall using minecode.plane()."""
    p3 = (p1[0], p2[1], p1[2])  # Align height with p2
    p4 = (p2[0], p1[1], p2[2])  # Align height with p1
    await Shapes.build_plane(p1, p2, p3, p4, material)

async def build_tower(center, radius, height, block="minecraft:stone_bricks"):
    """Creates a cylindrical tower by stacking circular layers."""
    for y in range(height):
        pos = (center[0], center[1] + y, center[2])  # Increase height with each step
        await Shapes.draw_circle(pos, radius, block)

