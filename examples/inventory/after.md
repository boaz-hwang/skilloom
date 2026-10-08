# Inventory report — structural refinement candidate

Convert the supplied item,available CSV to JSON: items (objects with item and integer available) and integer total.
Preserve every row in source order, including zero stock, with exact names and quantities; total must equal their sum.
Stop and ask for corrected input if a name or quantity is missing or a quantity is not a nonnegative integer. Never infer or add data.
Before delivery, check all rows against the source and reconcile total.
