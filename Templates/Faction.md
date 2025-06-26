---
tags: [swn, faction]
title: <% tp.file.title %>
type: faction
---
<%*
let scope = await tp.system.suggester(
  ["Planetary", "System-Spanning", "Sector-Wide", "Hidden Cell", "Extinct", "Nomadic Fleet"],
  ["Planetary", "System", "Sector", "Cell", "Extinct", "Fleet"]
)

let type = await tp.system.suggester(
  [
    "Religious Cult", "Military Force", "Criminal Syndicate", "Corporate Entity",
    "AI/Machine Group", "Pretech Remnant", "Rebel Movement", "Governing Body",
    "Academic Guild", "Alien Civilization", "Other"
  ],
  [
    "Religious Cult", "Military", "Criminal", "Corporate",
    "AI", "Pretech", "Rebellion", "Government",
    "Academia", "Alien", "Other"
  ]
)

if (type === "Other") {
  type = await tp.system.prompt("Enter custom faction type")
}

let base = await tp.system.prompt("Primary base of operations (planet, station, etc)?")
let leader = await tp.system.prompt("Leader(s) or ruling body?")
let goals = await tp.system.prompt("Faction goals or objectives?")
let methods = await tp.system.prompt("How do they pursue their goals?")
let doctrine = await tp.system.prompt("Beliefs, rules, or ethos?")

let speciesInput = await tp.system.prompt("Non-human species involved? (comma-separated, leave blank if none)")
let speciesLinks = ""
if (speciesInput.trim() !== "") {
  let speciesArray = speciesInput.split(",").map(s => s.trim()).filter(s => s.length > 0)
  speciesLinks = speciesArray.map(s => `- [[${s}]]`).join("\n")
}

let allyInput = await tp.system.prompt("Allies or client factions? (comma-separated)")
let allyLinks = ""
if (allyInput.trim() !== "") {
  let allyArray = allyInput.split(",").map(a => a.trim()).filter(a => a.length > 0)
  allyLinks = allyArray.map(a => `- [[${a}]]`).join("\n")
}

let enemyInput = await tp.system.prompt("Enemies or rivals? (comma-separated)")
let enemyLinks = ""
if (enemyInput.trim() !== "") {
  let enemyArray = enemyInput.split(",").map(e => e.trim()).filter(e => e.length > 0)
  enemyLinks = enemyArray.map(e => `- [[${e}]]`).join("\n")
}

tR += `# 🏛️ Faction: ${tp.file.title}

- Scope: ${scope}
- Type: ${type}
- Base of Operations: [[${base}]]
- Leadership: ${leader}
- Goals: ${goals}
- Methods: ${methods}
- Doctrine: ${doctrine}


## Non-Human Species Involved
${speciesLinks || "- None"}

## Allies
${allyLinks || "- None"}

## Enemies
${enemyLinks || "- None"}

## Description

## Recent Activity

## Assets or Holdings

## Secrets or Hidden Agendas

## Hooks for Players

## Notes
`
%>
