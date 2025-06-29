<%*
let pcClass = await tp.system.suggester(
  ["Warrior", "Expert", "Psychic", "AI", "Other"],
  ["Warrior", "Expert", "Psychic", "AI", "Other"],
  false,
  "Select the character class"
)
if (pcClass === "Other") {
  pcClass = await tp.system.prompt("Enter custom class")
}

let level = await tp.system.prompt("Character level?")
let background = await tp.system.prompt("Background?")
let faction = await tp.system.prompt("Affiliated faction (if any)?")
let focus = await tp.system.prompt("Current focus?")
let homeworld = await tp.system.prompt("Homeworld?")

let psychic = await tp.system.suggester(
  ["Yes", "No"],
  ["Yes", "No"],
  false,
  "Does this character have psychic abilities?"
)
let psychicDetail = ""
if (psychic === "Yes") {
  psychicDetail = await tp.system.prompt("Describe psychic powers or disciplines")
}

let cyberware = await tp.system.suggester(
  ["Yes", "No"],
  ["Yes", "No"],
  false,
  "Does this character have cyberware?"
)
let cyberDetail = ""
if (cyberware === "Yes") {
  cyberDetail = await tp.system.prompt("Describe installed cyberware")
}

let allyInput = await tp.system.prompt("Allies (comma-separated, leave blank if none)?")
let allyArray = allyInput.split(",").map(a => a.trim()).filter(a => a.length > 0)
let allyLinks = allyArray.map(a => `- [[${a}]]`).join("\n")
let allyYaml = allyArray.join(", ")

let enemyInput = await tp.system.prompt("Enemies (comma-separated, leave blank if none)?")
let enemyArray = enemyInput.split(",").map(e => e.trim()).filter(e => e.length > 0)
let enemyLinks = enemyArray.map(e => `- [[${e}]]`).join("\n")
let enemyYaml = enemyArray.join(", ")

tR += `---
title: ${tp.file.title}
type: pc
tags:
	- swn
	- pc
class: ${pcClass}
level: ${level}
background: ${background}
faction: ${faction}
focus: ${focus}
homeworld: ${homeworld}
psychic: ${psychic}
psychic_abilities: ${psychicDetail || "None"}
cyberware: ${cyberware}
cyberware_detail: ${cyberDetail || "None"}
allies: [${allyYaml}]
enemies: [${enemyYaml}]
---

# 🧑‍🚀 Player Character: ${tp.file.title}

- **Class:** ${pcClass}
- **Level:** ${level}
- **Background:** ${background}
- **Faction:** ${faction}
- **Focus:** ${focus}
- **Homeworld:** [[${homeworld}]]
- **Psychic:** ${psychic}
${psychic === "Yes" ? `- **Psychic Abilities:** ${psychicDetail}` : ""}
- **Cyberware:** ${cyberware}
${cyberware === "Yes" ? `- **Cyberware Details:** ${cyberDetail}` : ""}

## Allies
${allyLinks || "- None"}

## Enemies
${enemyLinks || "- None"}

## Description & Personality

## Skills

## Equipment

## Notes & Backstory
`
%>
