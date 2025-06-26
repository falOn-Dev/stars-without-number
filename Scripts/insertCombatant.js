module.exports = async function insertCombatant(tp) {
  const allFiles = app.vault.getMarkdownFiles();
  const tagFinderRegex = /tags:\s*\[\s*([\s\S]*?)\s*\]/i;
  const enemyFiles = [];

  for (const file of allFiles) {
    const content = await app.vault.read(file);
    const match = content.match(tagFinderRegex);

    if (!match || !match[1]) continue;

    const tagsArray = match[1]
      .split(",")
      .map((tag) => tag.trim().replace(/^["']|["']$/g, ""))
      .filter((tag) => tag.length > 0);

    if (tagsArray.includes("enemy") && file.name !== "Monster.md") {
      enemyFiles.push(file);
    }
  }

  if (enemyFiles.length === 0) {
    return `⚠️ No enemy-tagged notes found.`;
  }

  const choices = enemyFiles.map((f) => f.basename);
  const paths = enemyFiles.map((f) => f.path);

  const selectedPath = await tp.system.suggester(choices, paths);
  const selectedFile = app.vault.getAbstractFileByPath(selectedPath);
  const selectedContent = await app.vault.read(selectedFile);

  const frontmatterMatch = selectedContent.match(/---\n([\s\S]*?)\n---/);
  if (!frontmatterMatch) return `⚠️ No YAML frontmatter found in ${selectedPath}`;

  const frontmatterLines = frontmatterMatch[1].split("\n");
  const yaml = Object.fromEntries(
    frontmatterLines
      .map((line) => line.split(":").map((s) => s.trim()))
      .filter(([k, v]) => k && v)
  );

  const name = yaml.title || selectedFile.basename;
  const hd = parseInt(yaml.hd) || "?";
  const ac = yaml.ac || "?";
  const atk = yaml.atk || "?";
  const weapon = yaml.weapon || "?";
  const dmg = yaml.damage || "?";
  const morale = yaml.morale || "?";
  const move = yaml.move || "?";
  const save = yaml.save || "?";

  // Roll HP and Initiative
  let hp = "?";
  if (typeof hd === "number") {
    hp = 0;
    for (let i = 0; i < hd; i++) {
      hp += Math.floor(Math.random() * 6) + 1;
    }
  }

  const initiative = Math.floor(Math.random() * 8) + 1;

  const block = `- [ ] **${name}** — Init: ${initiative}

\`\`\`
${name} (${hd} HD)  
HP ${hp}, AC ${ac}, Atk ${atk} (${weapon}), Dmg ${dmg}, Mor ${morale}, Move ${move}, Save ${save}
\`\`\``;


  return block;
};
