---
title: <% tp.file.title %>
type: item
category: <% await tp.system.suggester(["Weapon", "Armor", "Tool", "Artifact", "Cyberware", "Other"], ["Weapon", "Armor", "Tool", "Artifact", "Cyberware", "Other"]) %>
tech_level: <% await tp.system.suggester(["TL0", "TL1", "TL2", "TL3", "TL4", "TL4+", "Pretech", "Postech"], ["TL0", "TL1", "TL2", "TL3", "TL4", "TL4+", "Pretech", "Postech"]) %>
rarity: <% await tp.system.suggester(["Common", "Uncommon", "Rare", "Unique"], ["Common", "Uncommon", "Rare", "Unique"]) %>
value: <% await tp.system.prompt("Market value (credits)?") %>
factions: <% await tp.system.prompt("Any factions associated with this item?") %>
---

# 🧰 Item: <% tp.file.title %>

- **Category:** <% tp.frontmatter.category %>
- **Tech Level:** <% tp.frontmatter.tech_level %>
- **Rarity:** <% tp.frontmatter.rarity %>
- **Value:** <% tp.frontmatter.value %> cr
- **Associated Factions:** <% tp.frontmatter.factions %>

## Description

## Game Effects

## Special Properties

## Hooks or Lore
