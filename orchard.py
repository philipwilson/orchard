from dataclasses import dataclass
import json
import math
import svgwrite

@dataclass
class Tree:
    name: str
    color: str
    fg: str
    season: str


def load_trees(filename='trees.json'):
    with open(filename) as f:
        data = json.load(f)
    return {(t['row'], t['col']): Tree(t['name'], t['color'], t['fg'], t['season']) for t in data}


tree_data = load_trees()
         



row_space = 80.0
tree_distance = row_space / math.sin(math.pi / 3)

dwg = svgwrite.Drawing('orchard.svg', size=(8*row_space+2*tree_distance, int(12*tree_distance)+1))


row_starts = (0, (9.5, 1), (10, 1), (0.5, 11), (1, 10), (0.5, 9), (0, 9), (1.5, 7), (2, 5), (3.5, 3))

for row in range(1,10):
    x = row * row_space
    start, trees = row_starts[row]
    y_start = start * tree_distance
    for col in range(1,trees + 1):
        y = y_start + (col * tree_distance)
        t = tree_data[(row,col)]
        dwg.add(svgwrite.shapes.Circle(center=(x,y), r=tree_distance/2,stroke=t.color, stroke_width=3, fill='white' ))
        dwg.add(dwg.text(t.name,
                         style="text-anchor: middle",
                         font_size='10px',
#                         font_weight="bold",
                         insert=(x, y+10)))
        dwg.add(dwg.text(t.fg,
                         style="text-anchor: middle",
                         font_size='15px',
                         font_weight="bold",
                         insert=(x, y-10)))

        dwg.add(dwg.text(t.season,
                         style="text-anchor: middle",
                         font_size='8px',
#                         font_weight="bold",
                         insert=(x, y+20)))
        
dwg.save()






