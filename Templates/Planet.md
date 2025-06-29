<%*
// Gather prompts
let tagsInput = await tp.system.prompt("World tags (comma-separated, use exact tag note names to link)?")

let atmosphere = await tp.system.suggester(
  ["Airless", "Thin", "Breathable", "Thick", "Corrosive", "Inert gas", "Other"],
  ["Airless", "Thin", "Breathable", "Thick", "Corrosive", "Inert gas", "Other"],
  false,
  "Select atmosphere type"
)
if (atmosphere === "Other") {
  atmosphere = await tp.system.prompt("Enter custom atmosphere")
}

let temperature = await tp.system.suggester(
  ["Frozen", "Cold", "Temperate", "Warm", "Hot"],
  ["Frozen", "Cold", "Temperate", "Warm", "Hot"],
  false,
  "Select temperature"
)

let biosphere = await tp.system.suggester(
  ["None", "Microbial life", "Minimal", "Human-compatible", "Overrun", "Exotic"],
  ["None", "Microbial life", "Minimal", "Human-compatible", "Overrun", "Exotic"],
  false,
  "Select biosphere"
)

let population = await tp.system.prompt("Population description?")
let tech = await tp.system.suggester(
  ["TL0", "TL1", "TL2", "TL3", "TL4", "Pretech", "Postech Ruin"],
  ["TL0", "TL1", "TL2", "TL3", "TL4", "Pretech", "Postech Ruin"],
  false,
  "Select tech level"
)

let government = await tp.system.prompt("Government type?")
let culture = await tp.system.prompt("Key cultural traits?")
let hazards = await tp.system.prompt("Major hazards or challenges?")
let controllingFaction = await tp.system.prompt("Primary controlling faction?")
let otherFactionsInput = await tp.system.prompt("Other factions (comma-separated)?")
let extraTags = await tp.system.prompt("Additional descriptive tags (comma-separated)?")

// Law level dropdown
let law = await tp.system.suggester(
  [
    "0: No law - anarchy, no restrictions",
    "1: Minimal law - scattered enforcement",
    "2: Lax law - only major crimes punished",
    "3: Typical law - basic order, local police",
    "4: Average law - standard restrictions, common enforcement",
    "5: Strict law - notable weapon bans, routine surveillance",
    "6: Harsh law - strong weapon bans, military patrols",
    "7: Repressive law - heavy surveillance, weapon prohibition",
    "8: Authoritarian law - strict controls, ID checks common",
    "9: Totalitarian law - constant monitoring, harsh penalties",
    "10: Absolute control - no tolerance for dissent, weaponry illegal"
  ],
  ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
  false,
  "Select law level"
)

// Law level descriptions
let lawDesc = {
  "0": "No law - anarchy, no restrictions",
  "1": "Minimal law - scattered enforcement",
  "2": "Lax law - only major crimes punished",
  "3": "Typical law - basic order, local police",
  "4": "Average law - standard restrictions, common enforcement",
  "5": "Strict law - notable weapon bans, routine surveillance",
  "6": "Harsh law - strong weapon bans, military patrols",
  "7": "Repressive law - heavy surveillance, weapon prohibition",
  "8": "Authoritarian law - strict controls, ID checks common",
  "9": "Totalitarian law - constant monitoring, harsh penalties",
  "10": "Absolute control - no tolerance for dissent, weaponry illegal"
}

// World tag links
let worldTagLinks = tagsInput
  ? tagsInput.split(",").map(t => `- [[${t.trim()}]]`).join("\n")
  : "None"

// Other faction links
let otherFactionsLinks = otherFactionsInput
  ? otherFactionsInput.split(",").map(f => `- [[${f.trim()}]]`).join("\n")
  : "None"

// Namespaced tags
let tagList = [
  `planet/atmosphere/${atmosphere.replace(/\s+/g, "_").toLowerCase()}`,
  `planet/temp/${temperature.toLowerCase()}`,
  `planet/biosphere/${biosphere.replace(/\s+/g, "_").toLowerCase()}`,
  `planet/tech/${tech.replace(/\s+/g, "_").toLowerCase()}`
]
if (extraTags.trim() !== "") {
  tagList = tagList.concat(extraTags.split(",").map(t => `planet/${t.trim().toLowerCase().replace(/\s+/g, "_")}`))
}

// Final output
tR += `---
title: ${tp.file.title}
type: planet
tags:
  - swn
  - planet
  - ${tagList.join("\n  - ")}
---

# 🌍 Planet: ${tp.file.title}

- **World Tags:**  
${worldTagLinks}
- **Atmosphere:** ${atmosphere}
- **Temperature:** ${temperature}
- **Biosphere:** ${biosphere}
- **Population:** ${population}
- **Tech Level:** ${tech}
- **Government:** ${government}
- **Law Level:** ${law} (${lawDesc[law]})
- **Cultural Traits:** ${culture}
- **Hazards:** ${hazards}
- **Controlling Faction:** ${controllingFaction ? `[[${controllingFaction}]]` : "None"}

## Other Factions
${otherFactionsLinks}

## Points of Interest

(Add points of interest here)

## Adventure Hooks

(Add adventure hooks here)

## Description

(Add detailed description here)
`
%>
