# 🧠 Encounter: <% tp.file.title %>

- **Date:** <% tp.date.now("YYYY-MM-DD") %>
- **Round:** 1

## 🔢 Initiative Order

Write names + initiative here in sorted order:

1. 

---

## 🧍 Player Characters

- [ ] **Name** — Init: __ — HP __ / __
- [ ] **Name** — Init: __ — HP __ / __

---

## 💀 Enemy Combatants

<%*
const count = await tp.system.prompt("How many enemies?");
const num = parseInt(count);
let result = "";

for (let i = 0; i < num; i++) {
  const block = await tp.user.insertCombatant(tp);
  result += block + "\n\n";
}

tR += result;
%>
