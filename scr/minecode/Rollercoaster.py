import asyncio
import bed_apy as mc_api
async def build_straight_track(start, length, direction):
    """Builds a straight track with powered rails and redstone block supports."""
    for i in range(length):
        pos = (start[0] + direction[0] * i, start[1], start[2] + direction[2] * i)

        # Place powered rail and redstone block below
        await mc_api.command(f"setblock {pos[0]} {pos[1]} {pos[2]} minecraft:powered_rail")
        await mc_api.command(f"setblock {pos[0]} {pos[1] - 1} {pos[2]} minecraft:redstone_block")

async def build_ramp(start, height, direction):
    """Creates a ramp by incrementing height gradually."""
    for i in range(height):
        pos = (start[0] + direction[0] * i, start[1] + i, start[2] + direction[2] * i)

        # Place powered rail and redstone block at each height level
        await mc_api.command(f"setblock {pos[0]} {pos[1]} {pos[2]} minecraft:powered_rail")
        await mc_api.command(f"setblock {pos[0]} {pos[1] - 1} {pos[2]} minecraft:redstone_block")