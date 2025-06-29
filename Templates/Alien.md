<%*
// Gather prompts
let classification = await tp.system.suggester(
  ["Humanoid", "Insectoid", "Reptilian", "Amorphous", "Plantlike", "Synthetic", "Energy Being", "Other"],
  ["Humanoid", "Insectoid", "Reptilian", "Amorphous", "Plantlike", "Synthetic", "Energy Being", "Other"],
  false,
  "Select alien classification"
)
if (classification === "Other") {
  classification = await tp.system.prompt("Enter custom classification")
}

let tech = await tp.system.suggester(
  ["TL0", "TL1", "TL2", "TL3", "TL4", "TL4+", "Pretech Relic", "Post-Singularity", "Unknown"],
  ["TL0", "TL1", "TL2", "TL3", "TL4", "TL4+", "Pretech Relic", "Post-Singularity", "Unknown"],
  false,
  "Select tech level"
)

let disposition = await tp.system.suggester(
  ["Hostile", "Wary", "Curious", "Friendly", "Subversive", "Indifferent"],
  ["Hostile", "Wary", "Curious", "Friendly", "Subversive", "Indifferent"],
  false,
  "Select disposition"
)

let homeworld = await tp.system.prompt("Homeworld or origin world?")
let environment = await tp.system.prompt("Preferred environment (e.g. desert, aquatic, vacuum)?")
let language = await tp.system.prompt("Primary language or method of communication?")
let culture = await tp.system.prompt("Key cultural trait or behavior?")
let society = await tp.system.prompt("Social structure or governance?")
let physiology = await tp.system.prompt("Notable physical traits or adaptations?")
let traits = await tp.system.prompt("Special abilities or tech (if any)?")

let alliesInput = await tp.system.prompt("Associated ally factions or races? (comma-separated)")
let enemiesInput = await tp.system.prompt("Associated enemy factions or races? (comma-separated)")

let hd = await tp.system.prompt("Hit Dice (HD)?")
let ac = await tp.system.prompt("Armor Class (AC)?")
let atk = await tp.system.prompt("Attack Bonus?")
let weapon = await tp.system.prompt("Weapon or attack style?")
let dmg = await tp.system.prompt("Damage?")
let move = await tp.system.prompt("Move Speed?")
let morale = await tp.system.prompt("Morale?")
let save = await tp.system.prompt("Save Target Number?")

let extraTags = await tp.system.prompt("Additional descriptive tags (comma-separated)?")

// Format allies/enemies links
let alliesLinks = ""
if (alliesInput.trim() !== "") {
  let arr = alliesInput.split(",").map(a => a.trim()).filter(a => a.length > 0)
  alliesLinks = arr.map(a => `- [[${a}]]`).join("\n")
}

let enemiesLinks = ""
if (enemiesInput.trim() !== "") {
  let arr = enemiesInput.split(",").map(e => e.trim()).filter(e => e.length > 0)
  enemiesLinks = arr.map(e => `- [[${e}]]`).join("\n")
}

// Build namespaced tags
let tagList = [
  `alien/classification/${classification.replace(/\s+/g, "_").toLowerCase()}`,
  `alien/tech/${tech.replace(/\s+/g, "_").toLowerCase()}`,
  `alien/disposition/${disposition.replace(/\s+/g, "_").toLowerCase()}`,
  `alien/environment/${environment.replace(/\s+/g, "_").toLowerCase()}`
]

if (extraTags.trim() !== "") {
  tagList = tagList.concat(extraTags.split(",").map(t => `alien/${t.trim().toLowerCase().replace(/\s+/g, "_")}`))
}

// Build final output
tR += `---
tags:
  - swn
  - alien
  - ${tagList.join("\n  - ")}
title: ${tp.file.title}
type: alien
---

# 👽 Alien Species: ${tp.file.title}

- **Classification:** ${classification}
- **Disposition:** ${disposition}
- **Tech Level:** ${tech}
- **Homeworld:** [[${homeworld}]]
- **Preferred Environment:** ${environment}
- **Language:** ${language}
- **Culture:** ${culture}
- **Social Structure:** ${society}
- **Physiology:** ${physiology}
- **Traits/Abilities:** ${traits || "None"}

## Allies
${alliesLinks || "None"}

## Enemies
${enemiesLinks || "None"}

## Description

## Interactions with Other Species

## Secrets or Mysteries

## Combat Stats

- **HD:** ${hd}
- **AC:** ${ac}
- **Attack Bonus:** ${atk}
- **Weapon/Attack:** ${weapon}
- **Damage:** ${dmg}
- **Move:** ${move}
- **Morale:** ${morale}
- **Save:** ${save}
`
%>
