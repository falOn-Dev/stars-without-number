---
tags:
	- swn
	- system
title: <% tp.file.title %>
type: system
---

<%*
let hex = await tp.system.prompt("Hex Code")

let star = await tp.system.suggester(
  ["Red Dwarf", "Yellow Star", "Blue Giant", "Binary Pair", "White Dwarf", "Neutron Star", "Black Hole", "Unknown"],
  ["Red Dwarf", "Yellow", "Blue Giant", "Binary", "White Dwarf", "Neutron", "Black Hole", "Unknown"]
)

let planetInput = await tp.system.prompt("Planets / Sites in this system? (comma-separated)")
let planetLinks = ""
if (planetInput.trim() !== "") {
  let planetArray = planetInput.split(",").map(p => p.trim()).filter(p => p.length > 0)
  planetLinks = planetArray.map(p => `- [[${p}]]`).join("\n")
}

let factionInput = await tp.system.prompt("Factions Present in this system? (comma-separated)")
let factionLinks = ""
if (factionInput.trim() !== "") {
  let factionArray = factionInput.split(",").map(f => f.trim()).filter(f => f.length > 0)
  factionLinks = factionArray.map(f => `- [[${f}]]`).join("\n")
}

tR += `# 🌌 System: ${tp.file.title}

- Hex Code: ${hex}
- Star Type: ${star}

## Planets / Sites
${planetLinks || "- None"}

## Factions Present
${factionLinks || "- None"}

## Adventure Hooks

## Notes
`
%>
