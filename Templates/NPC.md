---
tags:
	- swn
	- npc
title: <% tp.file.title %>
type: npc
---

<%*
let role = await tp.system.suggester(
  ["Scientist", "Commander", "Merchant", "Psychic", "Pilot", "Explorer", "Smuggler", "Cultist", "Administrator", "Other"],
  ["Scientist", "Commander", "Merchant", "Psychic", "Pilot", "Explorer", "Smuggler", "Cultist", "Administrator", "Other"]
)
if (role === "Other") {
  role = await tp.system.prompt("Enter custom role")
}

let location = await tp.system.prompt("Primary location (planet, station, etc)?")
let faction = await tp.system.prompt("Affiliated faction (leave blank if none)")

let isPsychic = await tp.system.suggester(["Yes", "No"], ["Yes", "No"])
let psychicAbilities = ""
if (isPsychic === "Yes") {
  psychicAbilities = await tp.system.prompt("What psychic abilities do they have?")
}

let hasCyberware = await tp.system.suggester(["Yes", "No"], ["Yes", "No"])
let cyberList = ""
if (hasCyberware === "Yes") {
  cyberList = await tp.system.prompt("What cyberware do they have?")
}

tR += `# 👤 NPC: ${tp.file.title}

- Role: ${role}
- Location: [[${location}]]
- Faction: ${faction ? `[[${faction}]]` : "None"}
- Psychic: ${isPsychic}
`
if (psychicAbilities) {
  tR += `- Psychic Abilities: ${psychicAbilities}\n`
}

tR += `- Cyberware: ${hasCyberware}
`
if (cyberList) {
  tR += `- Installed Cyberware: ${cyberList}\n`
}

tR += `
## Personality & Motivation

## Abilities & Skills

## Hooks

## Secrets

## Notes
`
%>
