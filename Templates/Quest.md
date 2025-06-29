<%*
// Gather prompts
let giver = await tp.system.prompt("Who gave this quest? (NPC, faction, etc.)")
let location = await tp.system.prompt("Where does the quest start?")
let destination = await tp.system.prompt("Where does the quest take place or end?")
let faction = await tp.system.prompt("What faction is involved (if any)?")

let type = await tp.system.suggester(
  ["Exploration", "Assault", "Infiltration", "Escort", "Recovery", "Diplomacy", "Investigation", "Bounty", "Other"],
  ["Exploration", "Assault", "Infiltration", "Escort", "Recovery", "Diplomacy", "Investigation", "Bounty", "Other"],
  false,
  "Select quest type"
)
if (type === "Other") {
  type = await tp.system.prompt("What type of quest is it?")
}

let urgency = await tp.system.suggester(
  ["Routine", "Important", "Time-Sensitive", "Urgent", "Secretive"],
  ["Routine", "Important", "Time-Sensitive", "Urgent", "Secretive"],
  false,
  "Select urgency level"
)

let reward = await tp.system.prompt("What's the reward or incentive?")
let complication = await tp.system.prompt("Any known complications or risks?")
let extraTags = await tp.system.prompt("Additional descriptive tags (comma-separated)?")

// Build namespaced tags
let tagList = [
  `quest/type/${type.replace(/\s+/g, "_").toLowerCase()}`,
  `quest/urgency/${urgency.replace(/\s+/g, "_").toLowerCase()}`
]

if (extraTags.trim() !== "") {
  tagList = tagList.concat(extraTags.split(",").map(t => `quest/${t.trim().toLowerCase().replace(/\s+/g, "_")}`))
}

// Final output
tR += `---
title: ${tp.file.title}
type: quest
tags:
  - swn
  - quest
  - ${tagList.join("\n  - ")}
---

# 🧭 Quest: ${tp.file.title}

- **Quest Giver:** ${giver}
- **Location:** [[${location}]]
- **Destination:** [[${destination}]]
- **Type:** ${type}
- **Involved Faction:** ${faction ? `[[${faction}]]` : "None"}
- **Urgency:** ${urgency}
- **Reward:** ${reward}
- **Complications:** ${complication}

## Objective

_What is the goal of this quest? What completes it?_

## Steps or Phases

- [ ]

## Related NPCs

- 

## Related Locations or Sites

- [[${location}]]
- [[${destination}]]

## Hooks or Leads

- 

## Hidden Agendas

- 

## Notes
`
%>
