import asyncio

async def run_x_every_x_ticks(code, interval):
    """Repeats execution of 'code' every 'interval' ticks."""
    while True:
        await asyncio.sleep(interval * 0.05)  # 1 tick = ~0.05 sec
        await code()

async def run_after_x_ticks(code, delay):
    """Delays execution of 'code' for 'delay' ticks."""
    await asyncio.sleep(delay * 0.05)  # Convert ticks to seconds
    await code()

async def run_x_for_x_ticks(code, duration):
    """Runs 'code' for 'duration' ticks and then stops."""
    task = asyncio.create_task(run_x_every_x_ticks(code, 1))
    await asyncio.sleep(duration * 0.05)  # Convert ticks to seconds
    task.cancel()

async def run_x_until_condition(code, check_func, interval=1):
    """Runs code every 'interval' ticks until 'check_func' returns True."""
    while not check_func():
        await asyncio.sleep(interval * 0.05)
        await code()

async def run_x_with_dynamic_interval(code, get_interval):
    """Runs code repeatedly, allowing the interval to change dynamically."""
    while True:
        interval = get_interval()
        await asyncio.sleep(interval * 0.05)
        await code()

async def run_x_with_cooldown(code, repeat_count, cooldown_ticks):
    """Runs code 'repeat_count' times, then pauses for 'cooldown_ticks' before restarting."""
    while True:
        for _ in range(repeat_count):
            await code()
            await asyncio.sleep(0.05)  # 1 tick
        await asyncio.sleep(cooldown_ticks * 0.05)  # Cooldown delay

async def run_x_cycle(actions, interval):
    """Loops through multiple actions in order, running one every 'interval' ticks."""
    while True:
        for action in actions:
            await asyncio.sleep(interval * 0.05)
            await action()

async def run_x_on_event(code, event_checker):
    """Runs 'code' whenever 'event_checker()' returns True."""
    while True:
        await asyncio.sleep(0.05)  # Tick-based checking
        if event_checker():
            await code()

async def run_x_chain(actions, delay_between):
    """Runs a chain of actions in sequence, with a set delay between each."""
    for action in actions:
        await action()
        await asyncio.sleep(delay_between * 0.05)
import asyncio

async def run_x_n_times(code, n, interval=1):
    """Runs 'code' exactly 'n' times, with 'interval' ticks between executions."""
    for _ in range(n):
        await asyncio.sleep(interval * 0.05)  # Convert ticks to seconds
        await code()