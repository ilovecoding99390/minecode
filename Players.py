"""Players is a copy of makecodes player function except without listeners because they are broken"""




import bed_apy as mc_api
import random
# PLAYER COMMANDS

async def teleport(player, x, y, z):
    """Teleport the player to specified coordinates."""
    await mc_api.command(f"tp {player} {x} {y} {z}")

async def say(message):
    """Make the player send a message using 'me' command."""
    await mc_api.command(f"me {message}")

async def give_item(player, item, quantity=1):
    """Give a specified item to the player."""
    await mc_api.command(f"give {player} {item} {quantity}")

async def clear_inventory(player):
    """Clear the player's inventory."""
    await mc_api.command(f"clear {player}")

async def set_gamemode(player, mode):
    """Change the player's game mode (survival, creative, adventure)."""
    await mc_api.command(f"gamemode {mode} {player}")

async def random_teleport(player, min_x, max_x, min_z, max_z):
    """Teleports the player to a random location within the given range."""
    x = random.randint(min_x, max_x)
    y = 64  # Default height to avoid underground issues
    z = random.randint(min_z, max_z)
    
    await mc_api.command(f"tp {player} {x} {y} {z}")
    print(f"{player} has been teleported to ({x}, {y}, {z})!")

