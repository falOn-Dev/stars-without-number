import json
import os
import re

output_file = "world_tags.json"

# Load existing data if resuming
if os.path.exists(output_file):
    with open(output_file, "r", encoding="utf-8") as f:
        world_tags = json.load(f)
else:
    world_tags = []

def clean_raw(raw):
    # Join hyphen-split words
    raw = re.sub(r"(\w+)-\s+(\w+)", r"\1\2", raw)
    # Replace remaining newlines with space
    raw = re.sub(r"[\r\n]+", " ", raw)
    # Remove multiple spaces
    raw = re.sub(r"\s{2,}", " ", raw)
    return raw.strip()



def parse_tag(raw):
    pattern = r"(.*?)E (.*?)F (.*?)C (.*?)T (.*?)P (.*)"
    match = re.match(pattern, raw.strip(), re.DOTALL)
    if not match:
        print("❌ Could not parse. Check format!")
        return None
    
    description = match.group(1).strip()
    enemies = [e.strip() for e in match.group(2).split(",")]
    friends = [f.strip() for f in match.group(3).split(",")]
    complications = [c.strip() for c in match.group(4).split(",")]
    things = [t.strip() for t in match.group(5).split(",")]
    places = [p.strip() for p in match.group(6).split(",")]
    
    return {
        "description": description,
        "enemies": enemies,
        "friends": friends,
        "complications": complications,
        "things": things,
        "places": places
    }

# Ensure we continue from where we left off
i = len(world_tags) + 1
while i <= 100:
    print(f"\n=== World Tag {i} ===")
    name = input("Name: ").strip()
    
    print("Paste the raw tag block (single line or wrapped):")
    raw = input().strip()
    raw = clean_raw(raw)
    
    tag_data = parse_tag(raw)
    if tag_data:
        tag_data["name"] = name
        world_tags.append(tag_data)
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(world_tags, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Saved tag {i}: '{name}'. Total so far: {len(world_tags)}")
        i += 1
    else:
        print("❌ Parse failed. Try again for this tag.")

print("🎉 All 100 world tags captured!")
