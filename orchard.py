from dataclasses import dataclass
import json
import math
import svgwrite


@dataclass
class Tree:
    name: str
    tree_type: str
    fg: str
    season: str


TYPE_COLORS = {
    'apple': 'green',
    'pear': 'yellow',
    'plum': 'violet',
    'cherry': 'red',
    'apricot': 'orange',
    'cider': 'brown',
}


def load_trees(filename='trees.json'):
    with open(filename) as f:
        data = json.load(f)
    return {(t['row'], t['col']): Tree(t['name'], t['type'], t['fg'], t['season']) for t in data}


tree_data = load_trees()

row_space = 80.0
tree_distance = row_space / math.sin(math.pi / 3)

# Compute SVG dimensions from tree positions (with padding for circle radius)
max_x = max(row for row, col in tree_data) * row_space
max_y = max((0.5 if row % 2 == 1 else 0) + col for row, col in tree_data) * tree_distance
width = max_x + tree_distance + tree_distance / 2
height = max_y + tree_distance / 2
dwg = svgwrite.Drawing('orchard.svg', size=(width, int(height) + 1))

for (row, col), t in tree_data.items():
    x = row * row_space
    hex_stagger = 0.5 if row % 2 == 1 else 0
    y = (hex_stagger + col) * tree_distance
    color = TYPE_COLORS[t.tree_type]

    dwg.add(svgwrite.shapes.Circle(center=(x, y), r=tree_distance/2, stroke=color, stroke_width=3, fill='white'))
    dwg.add(dwg.text(t.name,
                     style="text-anchor: middle",
                     font_size='10px',
                     insert=(x, y+10)))
    dwg.add(dwg.text(t.fg,
                     style="text-anchor: middle",
                     font_size='15px',
                     font_weight="bold",
                     insert=(x, y-10)))
    dwg.add(dwg.text(t.season,
                     style="text-anchor: middle",
                     font_size='8px',
                     insert=(x, y+20)))

dwg.save()
