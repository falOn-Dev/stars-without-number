<%*
// Gather prompts
let bodyType = await tp.system.suggester(
  ["Moon", "Station", "Asteroid", "Comet", "Megastructure", "Debris Field", "Anomaly", "Other"],
  ["Moon", "Station", "Asteroid", "Comet", "Megastructure", "Debris Field", "Anomaly", "Other"],
  false,
  "Select system body type"
)

if (bodyType === "Other") {
  bodyType = await tp.system.prompt("Enter custom body type")
}

let tech = await tp.system.suggester(
  ["TL0", "TL1", "TL2", "TL3", "TL4", "Pretech", "Postech Ruin"],
  ["TL0", "TL1", "TL2", "TL3", "TL4", "Pretech", "Postech Ruin"],
  false,
  "Select tech level"
)

let population = await tp.system.prompt("Population (if any)?")
let hazards = await tp.system.prompt("Major hazards?")
let controllingFaction = await tp.system.prompt("Primary controlling faction?")
let otherFactions = await tp.system.prompt("Other factions (comma-separated)?")
let extraTags = await tp.system.prompt("Additional descriptive tags (comma-separated)?")

// Build namespaced tags
let tagList = [
  `body_type/${bodyType.replace(/\s+/g, "_").toLowerCase()}`,
  `body_tech/${tech.replace(/\s+/g, "_").toLowerCase()}`
]

if (extraTags.trim() !== "") {
  tagList = tagList.concat(extraTags.split(",").map(t => `body/${t.trim().toLowerCase().replace(/\s+/g, "_")}`))
}

// Build other factions links
let otherFactionsLinks = ""
if (otherFactions.trim() !== "") {
  otherFactionsLinks = otherFactions.split(",").map(f => `- [[${f.trim()}]]`).join("\n")
}

// Final output
tR += `---
tags:
  - swn
  - system_body
  - ${tagList.join("\n  - ")}
title: ${tp.file.title}
type: system_body
---

# 🌌 ${bodyType}: ${tp.file.title}

- **Type:** ${bodyType}
- **Tech Level:** ${tech}
- **Population:** ${population}
- **Hazards:** ${hazards}
- **Controlling Faction:** ${controllingFaction ? `[[${controllingFaction}]]` : "None"}

## Other Factions
${otherFactionsLinks || "None"}

## Description

## Points of Interest

## Secrets or Mysteries

## Hooks
`
%>
