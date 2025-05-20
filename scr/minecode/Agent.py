import bed_apy as mc_api

async def agent_move(direction):
    await mc_api.command(f"agent.move {direction}")

async def agent_turn(turn_direction):
    await mc_api.command(f"agent.turn {turn_direction}")

async def agent_attack(direction):
    await mc_api.command(f"agent.attack {direction}")

async def agent_destroy(direction):
    await mc_api.command(f"agent.destroy {direction}")

async def agent_drop(slot_num, quantity, direction):
    await mc_api.command(f"agent.drop {slot_num} {quantity} {direction}")

async def agent_dropall(direction):
    await mc_api.command(f"agent.dropall {direction}")

async def agent_transfer(src_slot, quantity, dst_slot):
    await mc_api.command(f"agent.transfer {src_slot} {quantity} {dst_slot}")

async def agent_create():
    await mc_api.command("agent.create")

async def agent_tp(x, y, z):
    await mc_api.command(f"agent.tp {x} {y} {z}")

async def agent_collect(item):
    await mc_api.command(f"agent.collect {item}")

async def agent_till(direction):
    await mc_api.command(f"agent.till {direction}")

async def agent_place(slot_num, direction):
    await mc_api.command(f"agent.place {slot_num} {direction}")

async def agent_setitem(slot_num, quantity, amount, data):
    await mc_api.command(f"agent.setitem {slot_num} {quantity} {amount} {data}")