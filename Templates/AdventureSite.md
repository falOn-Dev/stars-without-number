<%*
// Gather prompts
let location = await tp.system.prompt("Located on or orbiting what world/station?")

let type = await tp.system.suggester(
  [
    "Ancient Ruin", "Pretech Facility", "Alien Structure", "Military Bunker", "Research Station",
    "Temple or Cult Site", "Derelict Ship", "Buried Vault", "Psychic Node", "City", "Other"
  ],
  [
    "Ancient Ruin", "Pretech Facility", "Alien Structure", "Military Bunker", "Research Station",
    "Temple or Cult Site", "Derelict Ship", "Buried Vault", "Psychic Node", "City", "Other"
  ]
)
if (type === "Other") {
  type = await tp.system.prompt("What type of adventure site is it?")
}

let condition = await tp.system.suggester(
  ["Intact", "Partially Ruined", "Collapsed", "Hidden", "Shielded", "Corrupted"],
  ["Intact", "Partially Ruined", "Collapsed", "Hidden", "Shielded", "Corrupted"]
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
let extraTags = await tp.system.prompt("Additional descriptive tags (comma-separated)?")

let factionInput = await tp.system.prompt("Factions involved or watching the site? (comma-separated)")
let factionLinks = ""
if (factionInput.trim() !== "") {
  let factionArray = factionInput.split(",").map(f => f.trim()).filter(f => f.length > 0)
  factionLinks = factionArray.map(f => `- [[${f}]]`).join("\n")
}

// Build namespaced tags
let tagList = [
  `site/type/${type.replace(/\s+/g, "_").toLowerCase()}`,
  `site/theme/${theme.replace(/\s+/g, "_").toLowerCase()}`,
  `site/condition/${condition.replace(/\s+/g, "_").toLowerCase()}`,
  `site/danger/${danger.toLowerCase()}`
]

if (extraTags.trim() !== "") {
  tagList = tagList.concat(extraTags.split(",").map(t => `site/${t.trim().toLowerCase().replace(/\s+/g, "_")}`))
}

// Build final note
tR += `---
tags:
  - swn
  - adventure-site
  - ${tagList.join("\n  - ")}
title: ${tp.file.title}
type: site
---

# 🗺️ Site: ${tp.file.title}

- **Location:** [[${location}]]
- **Type:** ${type}
- **Condition:** ${condition}
- **Danger Level:** ${danger}
- **Theme:** ${theme}
- **Potential Rewards:** ${loot}

## Factions
${factionLinks}

## Description

## Hazards

## Secrets

## Plot Hooks
`
%>
