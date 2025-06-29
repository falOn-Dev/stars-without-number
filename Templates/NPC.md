<%*
// Gather prompts
let role = await tp.system.suggester(
  ["Scientist", "Commander", "Merchant", "Psychic", "Pilot", "Explorer", "Smuggler", "Cultist", "Administrator", "Other"],
  ["Scientist", "Commander", "Merchant", "Psychic", "Pilot", "Explorer", "Smuggler", "Cultist", "Administrator", "Other"],
  false,
  "Select NPC role"
)
if (role === "Other") {
  role = await tp.system.prompt("Enter custom role")
}

let attitude = await tp.system.suggester(
  ["Friendly", "Neutral", "Hostile"],
  ["Friendly", "Neutral", "Hostile"],
  false,
  "Select NPC attitude"
)

let location = await tp.system.prompt("Primary location (planet, station, etc)?")
let faction = await tp.system.prompt("Affiliated faction (leave blank if none)?")

let isPsychic = await tp.system.suggester(["Yes", "No"], ["Yes", "No"], false, "Is the NPC psychic?")
let psychicAbilities = ""
if (isPsychic === "Yes") {
  psychicAbilities = await tp.system.prompt("What psychic abilities do they have?")
}

let cyberInput = await tp.system.prompt("Installed cyberware (comma-separated, matches Cyberware.md names)?")
let cyberLinks = ""
if (cyberInput.trim() !== "") {
  cyberLinks = cyberInput.split(",").map(c => `- [[${c.trim()}]]`).join("\n")
}

let extraTags = await tp.system.prompt("Additional descriptive tags (comma-separated)?")

// Build namespaced tags
let tagList = [
  `npc/role/${role.replace(/\s+/g, "_").toLowerCase()}`,
  `npc/attitude/${attitude.toLowerCase()}`
]

if (extraTags.trim() !== "") {
  tagList = tagList.concat(extraTags.split(",").map(t => `npc/${t.trim().toLowerCase().replace(/\s+/g, "_")}`))
}

// Final output
tR += `---
title: ${tp.file.title}
type: npc
tags:
  - swn
  - npc
  - ${tagList.join("\n  - ")}
---

# 👤 NPC: ${tp.file.title}

- **Role:** ${role}
- **Attitude:** ${attitude}
- **Location:** [[${location}]]
- **Faction:** ${faction ? `[[${faction}]]` : "None"}
- **Psychic:** ${isPsychic}
${psychicAbilities ? `- **Psychic Abilities:** ${psychicAbilities}` : ""}
- **Installed Cyberware:** 
${cyberLinks || "- None"}

## Personality & Motivation

(Add personality details here)

## Abilities & Skills

(Add key abilities or skills here)

## Hooks

(Add story hooks related to this NPC)

## Secrets

(Add hidden agendas or secrets)

## Notes

(Any additional notes)
`
%>
