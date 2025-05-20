"""recreation of makecode's block functions """

import bed_apy as mc_api
import json

async def set_block(x, y, z, block_type):
    """Places a single block at a specific coordinate."""
    await mc_api.command(f"setblock {x} {y} {z} {block_type}")
    print(f"Placed {block_type} at ({x}, {y}, {z})")

# FILL - Fills an area with a block type
async def fill_area(x1, y1, z1, x2, y2, z2, block_type):
    """Fills a rectangular region with a specific block."""
    await mc_api.command(f"fill {x1} {y1} {z1} {x2} {y2} {z2} {block_type}")
    print(f"Filled area ({x1}, {y1}, {z1}) to ({x2}, {y2}, {z2}) with {block_type}")
    
async def clone_area(x1, y1, z1, x2, y2, z2, x_dest, y_dest, z_dest):
    """Clones blocks from one region to another."""
    await mc_api.command(f"clone {x1} {y1} {z1} {x2} {y2} {z2} {x_dest} {y_dest} {z_dest}")
    print(f"Cloned area ({x1}, {y1}, {z1}) to ({x2}, {y2}, {z2}) at ({x_dest}, {y_dest}, {z_dest})")

def get_block_id(block_name):
    """Function to retrieve the block ID (or None if not found)"""
    with open("cleaned_blocks.json", "r", encoding="utf-8") as file:
        block_data = json.load(file)
    for block_id, name in block_data.items():
        if name == block_name:
            return block_id
    return None  # Not found

def block_exists(block_name):
    """Boolean function to check if a block exists"""
    return get_block_id(block_name) != "Unknown Item"

# Function to get item name by ID
def get_item_name(item_id):
    with open("cleaned_items.json", "r", encoding="utf-8") as file:
        item_data = json.load(file)
    # Ensure item_id has a meta value (defaulting to ":0" if missing)
    if ":" not in item_id:
        item_id += ":0"
    
    return item_data.get(item_id, "Unknown Item")

# Boolean function to check if an item ID exists
def item_exists(item_id):
    return get_item_name(item_id) != "Unknown Item"
