<%*
// Gather prompts
let type = await tp.system.suggester(
  ["Creature", "Human", "Robot", "Pretech Entity", "Alien", "Psychic Horror", "Other"],
  ["Creature", "Human", "Robot", "Pretech Entity", "Alien", "Psychic Horror", "Other"],
  false,
  "Select monster type"
)

if (type === "Other") {
  type = await tp.system.prompt("Enter custom monster type")
}

let danger = await tp.system.suggester(
  ["Low", "Moderate", "High", "Extreme", "Unknown"],
  ["Low", "Moderate", "High", "Extreme", "Unknown"],
  false,
  "Select danger level"
)

let environment = await tp.system.prompt("Preferred environment (e.g. desert, space, underwater)?")

let hd = await tp.system.prompt("Hit Dice (HD)? (e.g. 3)")
let ac = await tp.system.prompt("Armor Class (AC)?")
let atk = await tp.system.prompt("Attack Bonus? (e.g. +2)")
let weapon = await tp.system.prompt("Weapon or Attack Type?")
let dmg = await tp.system.prompt("Damage? (e.g. 1d8)")
let move = await tp.system.prompt("Move Speed? (e.g. 10m)")
let morale = await tp.system.prompt("Morale? (2d6 scale, e.g. 8)")
let save = await tp.system.prompt("Save Target Number? (Usually 15 - HD)")

let abilities = await tp.system.prompt("Special Abilities or Traits?")
let powers = await tp.system.prompt("Psychic Powers or Tech Abilities?")

let extraTags = await tp.system.prompt("Additional descriptive tags (comma-separated)?")

// Build namespaced tags
let tagList = [
  `enemy/type/${type.replace(/\s+/g, "_").toLowerCase()}`,
  `enemy/danger/${danger.toLowerCase()}`,
  `enemy/environment/${environment.replace(/\s+/g, "_").toLowerCase()}`
]

if (extraTags.trim() !== "") {
  tagList = tagList.concat(extraTags.split(",").map(t => `enemy/${t.trim().toLowerCase().replace(/\s+/g, "_")}`))
}

// Build final output
tR += `---
tags:
  - swn
  - enemy
  - ${tagList.join("\n  - ")}
title: ${tp.file.title}
type: enemy

hd: ${hd}
ac: ${ac}
atk: ${atk}
weapon: ${weapon}
damage: ${dmg}
move: ${move}
morale: ${morale}
save: ${save}
---

# 💀 Enemy: ${tp.file.title}

- **Type:** ${type}
- **Danger Level:** ${danger}
- **Preferred Environment:** ${environment}
- **Hit Dice:** ${hd}
- **Armor Class:** ${ac}
- **Attack Bonus:** ${atk}
- **Weapon:** ${weapon}
- **Damage:** ${dmg}
- **Move:** ${move}
- **Morale:** ${morale}
- **Save:** ${save}

## Description

## Behavior & Instincts

## Abilities
${abilities || "None"}

## Powers
${powers || "None"}

---

### ⚔️ **Stat Block**
\`\`\`
${tp.file.title} (${hd} HD)  
AC ${ac}, Atk ${atk} (${weapon}), Dmg ${dmg}, Mor ${morale}, Move ${move}, Save ${save}
\`\`\`
`
%>
