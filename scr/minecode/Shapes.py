"""This is a recreation of the shapes functions in makecode"""



import bed_apy as mc_api
import asyncio
import math

async def draw_line(start, end, block_id):
    steps = max(abs(end[0] - start[0]), abs(end[1] - start[1]), abs(end[2] - start[2]))
    for i in range(steps + 1):
        x = start[0] + (end[0] - start[0]) * (i / steps)
        y = start[1] + (end[1] - start[1]) * (i / steps)
        z = start[2] + (end[2] - start[2]) * (i / steps)
        await mc_api.command(f"setblock {math.floor(x)} {math.floor(y)} {math.floor(z)} {block_id}")

async def place_block(x, y, z, block):
    """Asynchronously places a block."""
    await mc_api.command(f"setblock {x} {y} {z} {block}")

async def draw_circle(center, radius, block="stone"):
    """Draws a circle using parallel execution."""
    cx, cy, cz = center
    tasks = []  # Store async tasks

    for angle in range(0, 360, 5):  # Reduce step size for speed
        radians = math.radians(angle)
        x = round(cx + radius * math.cos(radians))
        z = round(cz + radius * math.sin(radians))
        tasks.append(place_block(x, cy, z, block))  # Add task without waiting

    await asyncio.gather(*tasks)  # Execute all tasks in parallel!
def draw_cube(start, end, block="stone", hollow=False):
    """Draws a solid or hollow cube in Minecraft."""
    x1, y1, z1 = start
    x2, y2, z2 = end
    mode = "hollow" if hollow else ""

    mc_api.command(f"fill {x1} {y1} {z1} {x2} {y2} {z2} {block} {mode}")

def draw_sphere(center, radius, block="stone", hollow=False):
    """Draws a sphere with an optional hollow mode."""
    cx, cy, cz = center

    for y_offset in range(-radius, radius + 1):  # Vertical layers
        circle_radius = math.sqrt(radius**2 - y_offset**2)  # Adjust radius per layer
        
        for angle in range(0, 360, 5):  # Step through horizontal angles
            radians = math.radians(angle)
            x = round(cx + circle_radius * math.cos(radians))
            z = round(cz + circle_radius * math.sin(radians))
            
            # **Hollow mode: Skip inner blocks** except edge layers
            if hollow and abs(circle_radius - radius) > 0.5:
                continue  

            mc_api.command(f"setblock {x} {cy + y_offset} {z} {block}")

def draw_torus(center, major_radius, minor_radius, block="stone", hollow=False):
    """
    Draws a torus (doughnut shape) using parametric equations and magic.
    
    - **major_radius (R)** → Distance from the center of the torus to the middle of the pipe  
    - **minor_radius (r)** → Thickness of the pipe itself  
    - The torus is created by rotating the minor circle around the major circle.
    """

    cx, cy, cz = center

    for theta in range(0, 360, 15):  # Move around the outer ring (major radius)
        major_radians = math.radians(theta)
        major_x = cx + major_radius * math.cos(major_radians)
        major_z = cz + major_radius * math.sin(major_radians)

        for phi in range(0, 360, 10):  # Create the pipe cross-section (minor radius)
            minor_radians = math.radians(phi)
            x = round(major_x + minor_radius * math.cos(minor_radians))
            y = round(cy + minor_radius * math.sin(minor_radians))
            z = round(major_z)

            # Hollow check: Only place outer layer
            if hollow and abs(minor_radius - minor_radius) > 0.5:
                continue  

            mc_api.command(f"setblock {x} {y} {z} {block}")

async def build_plane(corner1, corner2, corner3, corner4, block_id):
    """Creates a plane using four corner positions."""
    
    # Get steps for interpolation (max distance in any direction)
    steps = max(
        abs(corner2[0] - corner1[0]), abs(corner2[1] - corner1[1]), abs(corner2[2] - corner1[2]),
        abs(corner4[0] - corner3[0]), abs(corner4[1] - corner3[1]), abs(corner4[2] - corner3[2])
    )

    for i in range(steps + 1):
        # Interpolate first edge
        edge1_x = corner1[0] + (corner2[0] - corner1[0]) * (i / steps)
        edge1_y = corner1[1] + (corner2[1] - corner1[1]) * (i / steps)
        edge1_z = corner1[2] + (corner2[2] - corner1[2]) * (i / steps)

        edge2_x = corner3[0] + (corner4[0] - corner3[0]) * (i / steps)
        edge2_y = corner3[1] + (corner4[1] - corner3[1]) * (i / steps)
        edge2_z = corner3[2] + (corner4[2] - corner3[2]) * (i / steps)

        # Draw line between interpolated edges
        await draw_line((math.floor(edge1_x), math.floor(edge1_y), math.floor(edge1_z)), 
         (math.floor(edge2_x), math.floor(edge2_y), math.floor(edge2_z)), block_id)