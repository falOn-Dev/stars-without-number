<%*
// Gather prompts
let hex = await tp.system.prompt("Hex Code")

let star = await tp.system.suggester(
  ["Red Dwarf", "Yellow Star", "Blue Giant", "Binary Pair", "White Dwarf", "Neutron Star", "Black Hole", "Unknown"],
  ["Red Dwarf", "Yellow Star", "Blue Giant", "Binary Pair", "White Dwarf", "Neutron Star", "Black Hole", "Unknown"],
  false,
  "Select star type"
)

let danger = await tp.system.suggester(
  ["Safe", "Contested", "Hazardous", "Dead", "Unknown"],
  ["Safe", "Contested", "Hazardous", "Dead", "Unknown"],
  false,
  "Select system danger level"
)

let theme = await tp.system.prompt("System theme / notes (e.g. trade hub, war zone)?")

let planetInput = await tp.system.prompt("Planets / Sites in this system? (comma-separated)")
let planetLinks = ""
if (planetInput.trim() !== "") {
  let arr = planetInput.split(",").map(p => p.trim()).filter(p => p.length > 0)
  planetLinks = arr.map(p => `- [[${p}]]`).join("\n")
}

let factionInput = await tp.system.prompt("Factions present in this system? (comma-separated)")
let factionLinks = ""
if (factionInput.trim() !== "") {
  let arr = factionInput.split(",").map(f => f.trim()).filter(f => f.length > 0)
  factionLinks = arr.map(f => `- [[${f}]]`).join("\n")
}

let extraTags = await tp.system.prompt("Additional descriptive tags (comma-separated)?")

// Build namespaced tags
let tagList = [
  `system/star_type/${star.replace(/\s+/g, "_").toLowerCase()}`,
  `system/danger/${danger.toLowerCase()}`
]

if (extraTags.trim() !== "") {
  tagList = tagList.concat(extraTags.split(",").map(t => `system/${t.trim().toLowerCase().replace(/\s+/g, "_")}`))
}

// Final output
tR += `---
title: ${tp.file.title}
type: system
tags:
  - swn
  - system
  - ${tagList.join("\n  - ")}
---

# 🌌 System: ${tp.file.title}

- **Hex Code:** ${hex}
- **Star Type:** ${star}
- **Danger Level:** ${danger}
- **Theme / Notes:** ${theme}

## Planets / Sites
${planetLinks || "- None"}

## Factions Present
${factionLinks || "- None"}

## Adventure Hooks

(Add plot ideas, mysteries, conflicts)

## Notes
`
%>
