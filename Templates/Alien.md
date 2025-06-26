---
tags: [swn, alien]
title: <% tp.file.title %>
type: alien
---

<%*
let classification = await tp.system.suggester(["Humanoid", "Insectoid", "Reptilian", "Amorphous", "Plantlike", "Synthetic", "Energy Being", "Other"], ["Humanoid", "Insectoid", "Reptilian", "Amorphous", "Plantlike", "Synthetic", "Energy", "Other"])
if (classification === "Other") {
  classification = await tp.system.prompt("Enter custom classification")
}

let tech = await tp.system.suggester(["TL0", "TL1", "TL2", "TL3", "TL4", "TL4+", "Pretech Relic", "Post-Singularity", "Unknown"], ["TL0", "TL1", "TL2", "TL3", "TL4", "TL4+", "Pretech", "Post-Singularity", "Unknown"])
let disposition = await tp.system.suggester(["Hostile", "Wary", "Curious", "Friendly", "Subversive", "Indifferent"], ["Hostile", "Wary", "Curious", "Friendly", "Subversive", "Indifferent"])

let language = await tp.system.prompt("Primary language or method of communication?")
let culture = await tp.system.prompt("Key cultural trait or behavior?")
let society = await tp.system.prompt("Social structure or governance?")
let physiology = await tp.system.prompt("Notable physical traits or adaptations?")

let hd = await tp.system.prompt("Hit Dice (HD)?")
let ac = await tp.system.prompt("Armor Class (AC)?")
let atk = await tp.system.prompt("Attack Bonus?")
let weapon = await tp.system.prompt("Weapon or attack style?")
let dmg = await tp.system.prompt("Damage?")
let move = await tp.system.prompt("Move Speed?")
let morale = await tp.system.prompt("Morale?")
let save = await tp.system.prompt("Save Target Number?")
let traits = await tp.system.prompt("Special abilities or tech (if any)?")

tR += `# 👽 Alien Species: ${tp.file.title}

- Classification: ${classification}
- Disposition: ${disposition}
- Tech Level: ${tech}
- Language: ${language}
- Culture: ${culture}
- Social Structure: ${society}
- Physiology: ${physiology}
- Traits/Abilities: ${traits || "None"}

## Description

## Interactions with Other Species

## Secrets or Mysteries

## Hooks

---

### ⚔️ Stat Block
\`\`\`
${tp.file.title} (${hd} HD)  
AC ${ac}, Atk ${atk} (${weapon}), Dmg ${dmg}, Mor ${morale}, Move ${move}, Save ${save}
\`\`\`
`
%>
