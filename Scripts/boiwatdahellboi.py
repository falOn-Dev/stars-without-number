import json

# Load your world_tags.json
with open("world_tags.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"✅ Total tags: {len(data)}\n")

# Extract names
names = [tag['name'] for tag in data]

# Pad to 100 if needed (for clean grid)
while len(names) < 100:
    names.append("")

# Build columns
columns = [names[i*25:(i+1)*25] for i in range(4)]

# Print row by row
for row in range(25):
    row_items = []
    for col in range(4):
        name = columns[col][row] if row < len(columns[col]) else ""
        row_items.append(f"{name:<30}")
    print("  ".join(row_items))
