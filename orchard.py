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

ROW_SPACE = 80.0
TREE_DISTANCE = ROW_SPACE / math.sin(math.pi / 3)


def load_trees(filename='trees.json'):
    with open(filename) as f:
        data = json.load(f)
    return {(t['row'], t['col']): Tree(t['name'], t['type'], t['fg'], t['season']) for t in data}


def draw_tree(dwg, row, col, tree):
    """Draw a single tree at the specified grid position."""
    x = row * ROW_SPACE
    hex_stagger = 0.5 if row % 2 == 1 else 0
    y = (hex_stagger + col) * TREE_DISTANCE
    color = TYPE_COLORS[tree.tree_type]

    dwg.add(svgwrite.shapes.Circle(center=(x, y), r=TREE_DISTANCE/2, stroke=color, stroke_width=3, fill='white'))
    dwg.add(dwg.text(tree.name,
                     style="text-anchor: middle",
                     font_size='10px',
                     insert=(x, y+10)))
    dwg.add(dwg.text(tree.fg,
                     style="text-anchor: middle",
                     font_size='15px',
                     font_weight="bold",
                     insert=(x, y-10)))
    dwg.add(dwg.text(tree.season,
                     style="text-anchor: middle",
                     font_size='8px',
                     insert=(x, y+20)))


def draw_legend(dwg, x, y):
    """Draw a color legend at the specified position."""
    dwg.add(dwg.text('Legend',
                     style="text-anchor: start",
                     font_size='12px',
                     font_weight="bold",
                     insert=(x, y)))

    for i, (tree_type, color) in enumerate(TYPE_COLORS.items()):
        legend_y = y + 20 + i * 20
        dwg.add(svgwrite.shapes.Circle(center=(x + 8, legend_y - 4), r=6,
                                        stroke=color, stroke_width=2, fill='white'))
        dwg.add(dwg.text(tree_type.capitalize(),
                         style="text-anchor: start",
                         font_size='10px',
                         insert=(x + 20, legend_y)))


def generate_orchard_svg(tree_data, output_file='orchard.svg'):
    """Generate an SVG visualization of the orchard."""
    # Compute SVG dimensions from tree positions (with padding for circle radius)
    max_x = max(row for row, col in tree_data) * ROW_SPACE
    max_y = max((0.5 if row % 2 == 1 else 0) + col for row, col in tree_data) * TREE_DISTANCE
    width = max_x + TREE_DISTANCE + TREE_DISTANCE / 2
    height = max_y + TREE_DISTANCE / 2
    dwg = svgwrite.Drawing(output_file, size=(width, int(height) + 1))

    for (row, col), tree in tree_data.items():
        draw_tree(dwg, row, col, tree)

    draw_legend(dwg, 10, 20)
    dwg.save()


def main():
    tree_data = load_trees()
    generate_orchard_svg(tree_data)


if __name__ == '__main__':
    main()
