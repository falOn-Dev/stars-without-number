---
title: <% tp.file.title %>
type: quest
tags: [swn, quest]
---

<%*
let giver = await tp.system.prompt("Who gave this quest? (NPC, faction, etc.)")
let location = await tp.system.prompt("Where does the quest start?")
let destination = await tp.system.prompt("Where does the quest take place or end?")
let faction = await tp.system.prompt("What faction is involved (if any)?")
let urgency = await tp.system.suggester(["Routine", "Important", "Time-Sensitive", "Urgent", "Secretive"], ["Routine", "Important", "Time-Sensitive", "Urgent", "Secretive"])
let type = await tp.system.suggester(["Exploration", "Assault", "Infiltration", "Escort", "Recovery", "Diplomacy", "Investigation", "Bounty", "Other"], ["Exploration", "Assault", "Infiltration", "Escort", "Recovery", "Diplomacy", "Investigation", "Bounty", "Other"])
if (type === "Other") {
	type = await tp.system.prompt("What type of quest is it?")
}
let reward = await tp.system.prompt("What's the reward or incentive?")
let complication = await tp.system.prompt("Any known complications or risks?")

tR += `# 🧭 Quest: ${tp.file.title}

- Quest Giver: ${giver}
- Location: [[${location}]]
- Destination: [[${destination}]]
- Type: ${type}
- Involved Faction: [[${faction}]]
- Urgency: ${urgency}
- Reward: ${reward}
- Complications: ${complication}

## Objective

_What is the goal of this quest? What completes it?_

## Steps or Phases

- 

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
