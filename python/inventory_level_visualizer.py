import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# ============================================================================
# PART 1: GENERATE PARAMETERS FROM STUDENT IDs
# ============================================================================
## last 3 digits of student id used
student_ids = [366, 201, 397, 204, 296, 61, 97, 538]


def generate_params(ids):
    avg_id = np.mean(ids)

    D = np.sum(ids)

    S = int(avg_id / 10)

    h = int(avg_id / 100)

    return D, S, h


D_val, S_val, h_val = generate_params(student_ids)

print("=" * 70)
print("INVENTORY MANAGEMENT SYSTEM - PARAMETER GENERATION")
print("=" * 70)
print(f"Student IDs: {student_ids}")
print(f"\nGenerated Parameters:")
print(f"  Annual Demand (D):        {D_val} units/year")
print(f"  Ordering Cost (S):        ${S_val}/order")
print(f"  Holding Cost (h):         ${h_val}/unit/year")
print("=" * 70)

# ============================================================================
# PART 2: SYMBOLIC DERIVATION USING SYMPY
# ============================================================================
D, S, h, L, d = sp.symbols('D S h L d', positive=True, real=True)

# Total cost function
Q = sp.Symbol('Q', positive=True)
total_cost = (D / Q) * S + (Q / 2) * h

# Find EOQ by taking derivative and setting to zero
dTC_dQ = sp.diff(total_cost, Q)

EOQ_solutions = sp.solve(dTC_dQ, Q)
EOQ = EOQ_solutions[0]

EOQ_simplified = sp.simplify(EOQ)

daily_demand = D / 365
ROP = daily_demand * L

# ============================================================================
# PART 3: CALCULATE NUMERICAL VALUES
# ============================================================================
EOQ_value = float(EOQ.subs([(D, D_val), (S, S_val), (h, h_val)]))
print(f"  EOQ = {EOQ_value:.2f} units")

TOTAL_COST = int((D_val / EOQ_value) * S_val + (EOQ_value / 2) * h_val)

daily_demand_val = D_val / 365
print(f"  d = {D_val}/365 = {daily_demand_val:.2f} units/day")


# ============================================================================
# PART 4: VISUALIZATION
# ============================================================================
def simulate_ideal_inventory(lead_time_days, delivery_time_days, D_annual, EOQ, days=90):
    daily_demand = D_annual / 365
    rop = daily_demand * lead_time_days

    time_points = np.arange(0, days, 0.1)
    inventory = []
    current_level = EOQ
    pending_order = None

    for t in time_points:
        current_level -= daily_demand * 0.1

        if current_level <= rop and pending_order is None:
            pending_order = t + delivery_time_days  # But actual delivery takes delivery_time

        if pending_order is not None and t >= pending_order:
            current_level += EOQ
            pending_order = None

        if current_level < 0:
            current_level = 0

        inventory.append(current_level)

    return time_points, np.array(inventory)


delivery_time = 9
lead_time_scenarios = [1, 9, 20]

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle(
    f'EOQ Inventory System: Impact of Different Lead Times\nEOQ = {EOQ_value:.1f} units | Daily Demand = {daily_demand_val:.2f} units/day | Delivery time=${delivery_time}',
    fontsize=14, fontweight='bold')

legend_elements = [
    plt.Line2D([0], [0], color='blue', linewidth=2.5, label='Inventory Level'),
    plt.Line2D([0], [0], color='orange', linestyle='--', linewidth=2, label='Reorder Point (ROP)'),
    plt.Line2D([0], [0], color='red', linestyle='--', linewidth=2, label='EOQ (Order Quantity)'),
    plt.Line2D([0], [0], color='red', linestyle='-', linewidth=2, alpha=0.7, label='Zero Line')
]

for idx, lead_time in enumerate(lead_time_scenarios):
    ax = axes[idx]

    rop_val = daily_demand_val * lead_time
    time_points, inventory_level = simulate_ideal_inventory(lead_time, delivery_time, D_val, EOQ_value, days=120)

    ax.plot(time_points, inventory_level, color='blue', linewidth=2.5)
    ax.axhline(y=rop_val, color='orange', linestyle='--', linewidth=2)
    ax.axhline(y=EOQ_value, color='red', linestyle='--', linewidth=2)
    ax.axhline(y=0, color='red', linestyle='-', linewidth=2, alpha=0.7)

    ax.set_xlabel('Time (days)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Inventory Level (units)', fontsize=11, fontweight='bold')
    ax.set_title(f'Lead Time = {lead_time} days', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)

    # Calculate metrics
    min_inventory = np.min(inventory_level)
    max_inventory = np.max(inventory_level)
    avg_inventory = np.mean(inventory_level)

    # Status text
    status_text = f'ROP: {rop_val:.1f}\nMin: {min_inventory:.1f}\nMax: {max_inventory:.1f}\nAvg: {avg_inventory:.1f}'

    if lead_time == delivery_time:
        status_text = 'IDEAL: No Stockouts\nNo Excess Inventory\nMinimal Total Cost'
        box_color = 'lightgreen'
    else:
        if delivery_time > lead_time:
            status_text = f'PROBLEM: Stockouts!\nDelivery too slow\nLost sales'
            box_color = 'lightcoral'
        else:
            status_text = f'PROBLEM: Excess Inventory!\nDelivery too fast\nHigher holding costs'
            box_color = 'lightyellow'

    ax.text(0.02, 1.00,
            status_text,
            transform=ax.transAxes, fontsize=10,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor=box_color, alpha=0.7))

fig.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(0.12, 1), fontsize=10)
plt.tight_layout()
plt.show()
