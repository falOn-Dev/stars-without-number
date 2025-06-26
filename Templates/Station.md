---
tags:
  - swn
  - station
title: <% tp.file.title %>
type: station
---
<%*
let orbit = await tp.system.prompt("What planet or object does this station orbit (or 'None')?")

let func = await tp.system.suggester(
  [
    "Military Installation", "Civilian Hub", "Research Lab", "Trade Depot",
    "Pirate Haven", "Religious Site", "Colony Support", "Listening Post",
    "Medical Facility", "Prison Station", "Other"
  ],
  [
    "Military Installation", "Civilian Hub", "Research Lab", "Trade Depot",
    "Pirate Haven", "Religious Site", "Colony Support", "Listening Post",
    "Medical Facility", "Prison Station", "Other"
  ]
)

if (func === "Other") {
  func = await tp.system.prompt("Enter custom station function")
}

let status = await tp.system.suggester(
  ["Operational", "Damaged", "Derelict", "Under Construction", "Abandoned", "Secret"],
  ["Operational", "Damaged", "Derelict", "Under Construction", "Abandoned", "Secret"]
)

let crew = await tp.system.prompt("Estimated crew or garrison size?")

let factionInput = await tp.system.prompt("Factions Present or Involved? (comma-separated)")
let factionLinks = ""
if (factionInput.trim() !== "") {
  let factionArray = factionInput.split(",").map(f => f.trim()).filter(f => f.length > 0)
  factionLinks = factionArray.map(f => `- [[${f}]]`).join("\n")
}

let defenses = await tp.system.prompt("Defensive systems (turrets, shields, etc)?")
defenses = defenses.trim() !== "" ? defenses : "N/A"

let hazards = await tp.system.prompt("Internal hazards (environmental, hostile AI, etc)?")
hazards = hazards.trim() !== "" ? hazards : "N/A"

tR += `# 🛰️ Station: ${tp.file.title}

- Orbiting: ${orbit.toLowerCase() === "none" ? "None" : `[[${orbit}]]`}
- Function: ${func}
- Status: ${status}
- Crew/Garrison: ${crew}
- Defenses: ${defenses}
- Hazards: ${hazards}

## Factions Present
${factionLinks || "- None"}

## Description

## Layout & Points of Interest

## Adventure Hooks

## Secrets or Hidden Functions

## Notes
`
%>
