# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is an orchard visualization tool that generates an SVG diagram of fruit tree locations. The script maps tree positions in a hexagonal grid pattern and outputs `orchard.svg`.

## Running

```bash
python orchard.py
```

This generates/updates `orchard.svg` with the current tree layout.

## Dependencies

```bash
pip install -r requirements.txt
```

## Architecture

- **Tree data** (`trees.json`): Array of tree objects with:
  - `row`, `col` - grid-absolute position
  - `name`, `type`, `flowering_group`, `season` - displayed on SVG
  - `planting_date`, `rootstock`, `source`, `notes` - optional metadata (not displayed)
- **Type to color mapping** (`TYPE_COLORS`): apple=green, pear=yellow, plum=violet, cherry=red, apricot=orange, cider=brown
- **Grid system**: Hexagonal layout computed automatically from tree positions; odd rows are staggered by 0.5. SVG dimensions derived from data.

## Module structure

- `load_trees(filename)` - Load tree data from JSON file
- `generate_orchard_svg(tree_data, output_file)` - Generate complete SVG
- `draw_tree(dwg, row, col, tree)` - Draw a single tree
- `draw_legend(dwg, x, y)` - Draw the color legend

The module can be imported for reuse:
```python
from orchard import load_trees, generate_orchard_svg
generate_orchard_svg(load_trees('other.json'), 'other.svg')
```
