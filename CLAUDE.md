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

- `svgwrite` - SVG generation library

## Architecture

- **Tree data structure**: `Tree` dataclass with `name`, `color` (border color indicating fruit type), `fg` (pollination group number), and `season` (harvest time)
- **Grid system**: Trees are positioned using (row, col) tuples in a hexagonal layout with staggered rows
- **Color coding**: violet=plums/gages, green=apples, red=cherries, orange=peaches/apricots, yellow=pears, brown=cider apples
- **Row configuration**: `row_starts` defines the vertical offset and tree count for each row
