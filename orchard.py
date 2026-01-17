from dataclasses import dataclass
import svgwrite
import math

@dataclass
class Tree:
    name: str
    color: str
    fg: str
    season: str


tree_data = {(1,1): Tree("Red Foxwhelp", 'brown', '5', "Very Late"),
             (2,1): Tree("Medaille D'Or", 'brown', '6', "Very Late"),
             (3,1): Tree('Cambridge Gage', 'violet', '3', "Late"),
             (3,2): Tree('Cambridge Gage', 'violet', '3', "Late"),
             (3,3): Tree('Victoria', 'violet', '3', 'Mid'),
             (3,4): Tree('Old Green Gage', 'violet', '3', 'Late'),
             (3,5): Tree('Blenheim Orange', 'green', '3', "Late"),
             (3,6): Tree("Cox's Orange Pippin", 'green', '3', "Mid"),
             (3,7): Tree("Cox's Orange Pippin", 'green', '3', "Mid"),
             (3,8): Tree('Dabinett', 'brown', '6', "Very Late"),
             (3,9): Tree('Kingston Black', 'brown', '4', "Very Late"),
             (3,10): Tree("Porter's Perfection", 'brown', '3', "Late"),
             (3,11): Tree('Stoke Red', 'brown', '6', "Very Late"),
             (4,1): Tree('Cambridge Gage', 'violet', '3', "Late"),
             (4,2): Tree('Cambridge Gage', 'violet', '3', "Late"),
             (4,3): Tree('Denbigh', 'violet', '3', "Aug / Sep"),
             (4,4): Tree('Bergeron', 'orange', '4', 'Mid'),
             (4,5): Tree('Pomeroy of Heref', 'green', '3', "Oct-Nov"),
             (4,6): Tree("Cox's Orange Pippin", 'green', '3', "Mid"),
             (4,7): Tree('Honeycrisp', 'green', '4', "Late"),
             (4,8): Tree('Kingston Black', 'brown', '4', "Very Late"),
             (4,9): Tree('Kingston Black', 'brown', '4', "Very Late"),
             (4,10): Tree("Harry Master's Jersey", 'brown', '4', "Very Late"),             
             (5,1): Tree('Morello', 'red', '5', "Mid"),
             (5,2): Tree('Lapins', 'red', '2', "Mid"),
             (5,3): Tree('Beurre Superfin', 'yellow', '4', "Late"),
             (5,4): Tree('Beurre Hardy', 'yellow', '4', "Late"),
             (5,5): Tree('Charles Ross', 'green', '3', "Mid"),
             (5,6): Tree('Egremont Russet', 'green', '2', "Late"),
             (5,7): Tree('Golden Delicious', 'green', '4', "Late"),
             (5,8): Tree('Yarlington Mill', 'brown', '5', "Very Late"),
             (5,9): Tree('Yarlington Mill', 'brown', '5', "Very Late"),
             (6,1): Tree('Lapins', 'red', '2', "Mid"),
             (6,2): Tree('Morello', 'red', '5', "Mid"),
             (6,3): Tree('Williams', 'yellow', '3', 'Early'),
             (6,4): Tree('Doyenne du Comice', 'yellow', '4', 'Late'),
             (6,5): Tree('Ten Commandments', 'green', '3', "Nov"),
             (6,6): Tree('Egremont Russet', 'green', '2', "Late"),
             (6,7): Tree('Egremont Russet', 'green', '2', "Late"),
             (6,8): Tree("Ashmead's Kernel", 'green', '4', "Late Oct"),
             (6,9): Tree('Dabinett', 'brown', '6', "Very Late"),
             (7,1): Tree('Black Oliver', 'red', '3', "Mid"),
             (7,2): Tree('Black Oliver', 'red', '3', "Mid"),
             (7,3): Tree("Shrops Lady's Finger", 'green', '3?', "Sep"),
             (7,4): Tree('Adams Pearmain', 'green', '3', "Late"),
             (7,5): Tree('Bringewood Pippin', 'green', '3', "Late"),
             (7,6): Tree("Gascoyne's Scarlett", 'green', '5', "Oct-Jan"),
             (7,7): Tree("Sweeney's Nonparail", 'green', '5', "Oct-Dec"),
             (8,1): Tree('Black Oliver', 'red', '3', "Mid"),
             (8,2): Tree('Williams (graft)', 'yellow', '3', 'Early'),
             (8,3): Tree('Puckrupp Pippin', 'green', '2', "Nov-Jan"),
             (8,4): Tree('Lord of Lambourne', 'green', '2', "Sep-Nov"),
             (8,5): Tree("Ashmead's Kernel", 'green', '4', "Late Oct"),
             (9,1): Tree("Yellow Huffcap", 'yellow', '3', "October"),
             (9,2): Tree("Pitmaston Pine Apple", 'green', '4', "Late"),
             (9,3): Tree("Devonshire Quarrendon", 'green', '2', "Very Early")
             
         }
         



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






