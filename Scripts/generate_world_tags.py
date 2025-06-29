import os
import json

# Directory to save files
output_dir = "WorldTags"
os.makedirs(output_dir, exist_ok=True)

# Load the world tags data
with open("world_tags.json", "r", encoding="utf-8") as f:
    world_tags = json.load(f)

def slugify(name):
    return name.lower().replace(" ", "_").replace("/", "_")

# Generate files
for tag in world_tags:
    filename = os.path.join(output_dir, f"{tag['name']}.md")
    tags = [
        "swn",
        "world_tag",
        f"world_tag/{slugify(tag['name'])}"
    ]
    content = f"""---
title: {tag['name']}
type: world_tag
tags:
  - {'\n  - '.join(tags)}
---
# 🌐 World Tag: {tag['name']}

## Description
{tag['description']}
## Enemies
{''.join([f"- {e}\n" for e in tag['enemies']]) or "- None"}
## Friends
{''.join([f"- {f}\n" for f in tag['friends']]) or "- None"}
## Complications
{''.join([f"- {c}\n" for c in tag['complications']]) or "- None"}
## Things
{''.join([f"- {t}\n" for t in tag['things']]) or "- None"}
## Places
{''.join([f"- {p}\n" for p in tag['places']]) or "- None"}
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Generated {len(world_tags)} world tag notes in '{output_dir}/'")
