import asyncio
import bed_apy as mc_api
async def spawn(entity):
    await mc_api.command(f"spawn {entity}")

async def kill(entity):
    await mc_api.command(f"kill {entity}")

async def effect(entity, effect_type, duration):
    await mc_api.command(f"effect {entity} {effect_type} {duration}")

async def give(entity, item, amount=1):
    await mc_api.command(f"give {entity} {item} {amount}")

async def enchant(entity, item, enchantment, level):
    await mc_api.command(f"enchant {entity} {item} {enchantment} {level}")
    
async def spawn_particle(particle_name, x, y, z, count=1):
    await mc_api.command(f"particle {particle_name} {x} {y} {z} {count}")
