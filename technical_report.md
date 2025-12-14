# Technical Report: Inventory Level Visualizer and Reorder Symbolic Policy

## Abstract
This project developed an inventory management tool using symbolic derivation, simulation, visualization, and parametric design. An EOQ-style formula and reorder point were symbolically derived with SymPy in Python. Inventory levels were simulated and plotted over time for different lead-time scenarios using Matplotlib. A parametric storage bin was designed in FreeCAD. Results demonstrate the impact of lead times on inventory dynamics, stockouts, and costs.

## Introduction
Inventory management optimizes costs while preventing stockouts. The Economic Order Quantity (EOQ) model minimizes holding and ordering costs [1]. This team-based project symbolically derived EOQ and reorder point formulas, visualized inventory levels under varying lead times, and designed a physical bin.

### Objectives
- Symbolically derive EOQ and reorder point
- Simulate and plot inventory under varying lead times
- Design a parametric bin in FreeCAD

## Methodology
### A. Project Planning
A dynamic Gantt chart in Excel modeled tasks, milestones, and dependencies.
[Placeholder: Excel Gantt Chart Screenshot]

### B. Symbolic Derivation
Using SymPy, variables were defined: annual demand $D$, ordering cost $K$, holding cost per unit per year $h$, lead time $L$ (days).

Derived EOQ:

$ Q = \sqrt{\frac{2DK}{h}} $

Reorder point:

$ R = (D / 365) \times L $
Daily demand rate: 
$d = D / 365 \approx 5.92$ units/day (derived from team-specific parameters using last three digits of student ID).

**[Python Code - Simulation and Plotting](./python/inventory_level_visualizer.py)**

### C. Simulation and Visualization
Inventory was simulated over 120 days with constant demand. Parameters generated EOQ = 241.5 units, daily demand ≈5.92 units/day. Lead times: 1, 9, 20 days. Matplotlib generated sawtooth plots showing:

- Short lead time (1 day): High inventory, slow turnover, potential lost sales.
- Optimal lead time (9 days): No stockouts, minimal excess inventory, lowest total cost.
- Long lead time (20 days): Excess inventory, higher holding costs.

**[Python Code - Symbolic Derivation](./python/inventory_level_visualizer.py)**

**[Inventory Level Plots: EOQ Inventory System - Impact of Different Lead Times](./images/inventory-level-visualization.jpg)**

### D. Parametric Design
A bin was modeled in FreeCAD with parametric dimensions, mounting holes, and labels using the spreadsheet workbench.

[Placeholder: FreeCAD Screenshots]

## III. Results
EOQ = 241.5 units; reorder point varied with lead time. Plots illustrated stockout risks or excess holding with mismatched lead times, confirming optimal performance near 9-day delivery time.

## IV. Discussion
Symbolic derivation enables flexible analysis [2]. Visualizations clearly highlight lead-time effects on costs and risks. Limitations: constant demand assumption; no safety stock. Future extensions: incorporate stochastic demand.

## V. Conclusion
The project integrated computational and design tools to demonstrate effective inventory reorder policies, achieving all deliverables.

## References
[1] F. W. Harris, "How many parts to make at once," Factory, Mag. Manage., vol. 10, no. 2, pp. 135–136, 1913.

[2] SymPy Development Team, "SymPy: Python library for symbolic mathematics," [Online]. Available: https://www.sympy.org/

[3] J. D. Hunter, "Matplotlib: A 2D graphics environment," Comput. Sci. Eng., vol. 9, no. 3, pp. 90–95, 2007.

[4] FreeCAD Project, "FreeCAD: Open-source parametric 3D CAD modeler," [Online]. Available: https://www.freecad.org/

## Appendices
**A. Python Code**  
[Full Python Script](./python/inventory_level_visualizer.py)

**B. FreeCAD Model**  
[FreeCAD Parametric Bin Model](./freecad/Parametric_Gridfinity_Baseplate.FCStd) | [Screenshots](./freecad/screenshots/)
