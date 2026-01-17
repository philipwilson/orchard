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

- **Tree data** (`trees.json`): Array of tree objects with `row`, `col`, `name`, `type`, `fg` (pollination group), and `season`
- **Type to color mapping** (`TYPE_COLORS` in orchard.py): apple=green, pear=yellow, plum=violet, cherry=red, apricot=orange, cider=brown
- **Grid system**: Hexagonal layout with staggered rows; `row_starts` in orchard.py defines vertical offset and tree count per row
