# Inventory report — baseline instructions

Read the supplied CSV. It has item and available columns.
Write a JSON object with an items array and a total integer.
For each CSV row, add an object with item and available to items.
Keep the rows in source order. Include rows with zero available stock.
Copy each item name exactly. Copy each quantity exactly as an integer.
Sum all quantities into total. Do not add products or infer missing quantities.
If an item or quantity is missing, or a quantity is not a nonnegative integer, stop and ask for corrected input.
Before delivery, check that the items match every input row and that total is their sum.
