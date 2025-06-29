<%*
// Gather prompts
const tagsInput = await tp.system.prompt("Additional encounter tags (comma-separated)?");

const type = await tp.system.suggester(
  ["Combat", "Social", "Exploration", "Trap", "Puzzle", "Other"],
  ["Combat", "Social", "Exploration", "Trap", "Puzzle", "Other"],
  false,
  "Select encounter type"
);
let typeTag = `encounter/type/${type.toLowerCase()}`;

const danger = await tp.system.suggester(
  ["Low", "Moderate", "High", "Extreme", "Unknown"],
  ["Low", "Moderate", "High", "Extreme", "Unknown"],
  false,
  "Select danger level"
);
let dangerTag = `encounter/danger/${danger.toLowerCase()}`;

const location = await tp.system.prompt("Where does this encounter take place? (planet/station/hex/etc)");

const objective = await tp.system.prompt("What is the objective of this encounter?");

const count = await tp.system.prompt("How many enemies?");
const num = parseInt(count);

const baseTags = ["swn", "encounter", typeTag, dangerTag];
const extraTags = tagsInput
  ? tagsInput.split(",").map(t => t.trim()).filter(t => t.length > 0)
  : [];
const allTags = baseTags.concat(extraTags);

let result = "";
for (let i = 0; i < num; i++) {
  const block = await tp.user.insertCombatant(tp);
  result += block + "\n\n";
}

// Build final output
tR += `---
title: ${tp.file.title}
type: encounter
tags:
${allTags.map(t => `  - ${t}`).join("\n")}
---

# 🧠 Encounter: ${tp.file.title}

- **Date:** ${tp.date.now("YYYY-MM-DD")}
- **Round:** 1
- **Type:** ${type}
- **Danger Level:** ${danger}
- **Location:** [[${location}]]
- **Objective:** ${objective}

## 🔢 Initiative Order

Write names + initiative here in sorted order:

1.

---

## 🧍 Player Characters

- [ ] **Name** — Init: __ — HP __ / __
- [ ] **Name** — Init: __ — HP __ / __

---

## 💀 Enemy Combatants

${result}

---

## 📝 Notes

(Add any special rules, tactics, or twists here)
`
%>
