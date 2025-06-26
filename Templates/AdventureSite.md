---
tags: [swn, adventure-site]
title: <% tp.file.title %>
type: site
---

<%*
let location = await tp.system.prompt("Located on or orbiting what world/station?")

let type = await tp.system.suggester(
  [
    "Ancient Ruin", "Pretech Facility", "Alien Structure", "Military Bunker", "Research Station",
    "Temple or Cult Site", "Derelict Ship", "Buried Vault", "Psychic Node", "City", "Other"
  ],
  [
    "Ancient Ruin", "Pretech Facility", "Alien Structure", "Military Bunker", "Research Station",
    "Temple", "Derelict Ship", "Vault", "Psychic Node", "City", "Other"
  ]
)
if (type === "Other") {
  type = await tp.system.prompt("What type of adventure site is it?")
}

let condition = await tp.system.suggester(
  ["Intact", "Partially Ruined", "Collapsed", "Hidden", "Shielded", "Corrupted"],
  ["Intact", "Ruined", "Collapsed", "Hidden", "Shielded", "Corrupted"]
)

let danger = await tp.system.suggester(
  ["Low", "Moderate", "High", "Extreme", "Unknown"],
  ["Low", "Moderate", "High", "Extreme", "Unknown"]
)

let theme = await tp.system.suggester(
  ["Tech", "Horror", "Mystery", "Religious", "Warfare", "Exploration", "Psychic", "Other"],
  ["Tech", "Horror", "Mystery", "Religious", "Warfare", "Exploration", "Psychic", "Other"]
)
if (theme === "Other") {
  theme = await tp.system.prompt("What is the theme of the site?")
}

let loot = await tp.system.prompt("What kind of loot/reward might be found?")
let tags = await tp.system.prompt("Tags or descriptive keywords?")

let factionInput = await tp.system.prompt("Factions involved or watching the site? (comma-separated)")
let factionLinks = ""

if (factionInput.trim() !== "") {
  let factionArray = factionInput.split(",").map(f => f.trim()).filter(f => f.length > 0)
  factionLinks = factionArray.map(f => `- [[${f}]]`).join("\n")
}


tR += `# 🗺️ Site: ${tp.file.title}

- Location: [[${location}]]
- Type: ${type}
- Condition: ${condition}
- Danger Level: ${danger}
- Theme: ${theme}
- Tags: ${tags}
- Potential Rewards: ${loot}

## Factions Involved
${factionLinks || "- None"}

## Description

## Entry Points & Layout

## Notable Features or Rooms

## Inhabitants or Threats

## Secrets or Triggers

## Hooks & Player Engagement

## Notes
`
%>
