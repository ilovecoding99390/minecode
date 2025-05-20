"""gameplay is a bunch of simple functions simalar to makecodes gameplay functions"""


import bed_apy as mc_api

async def set_time(time_value):
    """Sets the game time (day, night, specific tick value)."""
    await mc_api.command(f"time set {time_value}")

async def set_weather(weather_type):
    """Changes the weather (clear, rain, thunder)."""
    await mc_api.command(f"weather {weather_type}")

async def add_xp(amount, target="@p"):
    """Gives XP points or levels to a player."""
    await mc_api.command(f"xp {amount} {target}")

async def change_gamerule(rule, value):
    """Adjusts a game rule (e.g., keep inventory, mob spawning)."""
    await mc_api.command(f"gamerule {rule} {value}")

async def change_gamemode(mode, target="@p"):
    """Switches a player's gamemode (survival, creative, adventure)."""
    await mc_api.command(f"gamemode {mode} {target}")

async def play_music(track="record.pigstep"):
    """Plays the specified music track asynchronously using /music. Defaults to 'record.pigstep'."""
    command = f"/music play {track}"
    await mc_api.command(command)