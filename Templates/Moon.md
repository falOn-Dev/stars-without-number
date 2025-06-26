---
tags:
  - swn
  - moon
title: <% tp.file.title %>
type: moon
---

<%*
let system = await tp.system.prompt("System")
let orbitalParent = await tp.system.prompt("What planet does this moon orbit?")

let atmosphere = await tp.system.suggester(
	[
		"Corrosive", "Inert", "Airless/Thin", "Breathable",
		"Thick", "Invasive"
	],
	[
		"Corrosive", "Inert", "Airless/Thin", "Breathable",
		"Thick", "Invasive"
	]
)

let temp = await tp.system.suggester(
	[
		"Frozen", "Cold", "Variable Cold-Temp",
		"Temperate",
		"Variable Warm-Temp", "Warm", "Burning"
	],
	[
		"Frozen", "Cold", "Variable Cold-Temp",
		"Temperate",
		"Variable Warm-Temp", "Warm", "Burning"
	]
)

let biosphere = await tp.system.suggester(
	[
		"Remnant", "Microbial", "None", "Human-miscible",
		"Immiscible", "Hybrid", "Engineered"
	],
	[
		"Remnant", "Microbial", "None", "Human-miscible",
		"Immiscible", "Hybrid", "Engineered"
	]
)

let pop = await tp.system.suggester(
	[
		"Failed Colony", "Outpost", "<1m", ">1m", ">100m", ">1b"
	],
	[
		"Failed Colony", "Outpost", "Fewer than a million inhabitants", "Several million inhabitants", "Hundreds of millions of inhabitants", "Billions of inhabitants"
	]
)

let tech = await tp.system.suggester(
  ["TL0", "TL1", "TL2", "TL3", "TL4", "TL4+", "TL5"],
  ["TL0", "TL1", "TL2", "TL3", "TL4", "TL4+", "TL5"]
)

let specialties = ""
if (tech === "TL4+") {
  specialties = await tp.system.prompt("Enter Tech Specialties")
}

let tags = await tp.system.prompt("Enter Moon Tags:")

let poiInput = await tp.system.prompt("Landmarks or POIs? (comma-separated)")
let poiLinks = ""
if (poiInput.trim() !== "") {
  let poiArray = poiInput.split(",").map(p => p.trim()).filter(p => p.length > 0)
  poiLinks = poiArray.map(p => `- [[${p}]]`).join("\n")
}

let orbitalsInput = await tp.system.prompt("Linked orbital bodies (stations, satellites, etc)? (comma-separated)")
let orbitalLinks = ""
if (orbitalsInput.trim() !== "") {
  let orbitalArray = orbitalsInput.split(",").map(o => o.trim()).filter(o => o.length > 0)
  orbitalLinks = orbitalArray.map(o => `- [[${o}]]`).join("\n")
}

let factionInput = await tp.system.prompt("Factions present on or around this moon? (comma-separated)")
let factionLinks = ""
if (factionInput.trim() !== "") {
  let factionArray = factionInput.split(",").map(f => f.trim()).filter(f => f.length > 0)
  factionLinks = factionArray.map(f => `- [[${f}]]`).join("\n")
}

tR += `# 🌙 Moon: ${tp.file.title}

- System: [[${system}]]
- Orbits: [[${orbitalParent}]]
- Atmosphere: ${atmosphere}
- Climate: ${temp}
- Biosphere: ${biosphere}
- Population: ${pop}
- Tech Level: ${tech}
`

if (specialties) {
  tR += `- Tech Specialties: ${specialties}\n`
}

tR += `- Tags: ${tags}

## Description

## Adventure Seeds

## Landmarks/POIs
${poiLinks || "- None"}

## Orbital Bodies
${orbitalLinks || "- None"}

## Factions Present
${factionLinks || "- None"}

## Notes
`
%>
