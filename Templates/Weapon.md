<%*
let wType = await tp.system.suggester(
  ["Melee", "Ranged", "Explosive", "Energy", "Pretech", "Other"],
  ["Melee", "Ranged", "Explosive", "Energy", "Pretech", "Other"],
  false,
  "Select weapon type"
)
if (wType === "Other") {
  wType = await tp.system.prompt("Enter custom weapon type")
}

let tech = await tp.system.suggester(
  ["TL0", "TL1", "TL2", "TL3", "TL4", "TL4+", "Pretech"],
  ["TL0", "TL1", "TL2", "TL3", "TL4", "TL4+", "Pretech"],
  false,
  "Select tech level"
)

let dmg = await tp.system.prompt("Damage (e.g. 1d8, 2d6)?")
let range = await tp.system.prompt("Effective range (if any)?")
let value = await tp.system.prompt("Market value in credits?")
let tagsInput = await tp.system.prompt("Weapon tags (comma-separated, e.g. shock, armor_piercing, burst)?")
let skill = await tp.system.suggester(
  ["Shoot", "Stab", "Punch", "Other"],
  ["Shoot", "Stab", "Punch", "Other"],
  false,
  "Select weapon skill"
)
if (skill === "Other") {
  skill = await tp.system.prompt("Enter custom skill")
}

let ammo = await tp.system.prompt("Ammo type / capacity (if any)?")
let faction = await tp.system.prompt("Any associated faction or origin?")

// Build namespaced tag list
let tagsList = tagsInput.split(",").map(tag => `weapon/${tag.trim()}`).join("\n  - ")

tR += `---
title: ${tp.file.title}
tags:
  - swn
  - weapon
  - ${tagsList}
type: weapon
weapon_type: ${wType}
tech_level: ${tech}
damage: ${dmg}
range: ${range}
value: ${value}
skill: ${skill}
ammo: ${ammo}
faction: ${faction}
---

# ⚔ Weapon: ${tp.file.title}

- **Type:** ${wType}
- **Tech Level:** ${tech}
- **Damage:** ${dmg}
- **Range:** ${range}
- **Value:** ${value} cr
- **Skill:** ${skill}
- **Ammo / Capacity:** ${ammo}
- **Faction / Origin:** ${faction}
- **Tags:** ${tagsInput}

## Description

## Special Properties

## Lore / History

## Hooks or Uses
`
%>
