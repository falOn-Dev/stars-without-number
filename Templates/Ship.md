---
title: <% tp.file.title %>
type: ship
class: <% await tp.system.prompt("Ship Class (e.g. Frigate, Courier, Gunboat)?") %>
hull_points: <% await tp.system.prompt("Hull Points?") %>
speed: <% await tp.system.prompt("Speed (e.g. 2 Hexes)?") %>
armor: <% await tp.system.prompt("Armor Value?") %>
crew: <% await tp.system.prompt("Recommended Crew?") %>
faction: <% await tp.system.prompt("Faction or Owner?") %>
tags: <% await tp.system.prompt("Tags or keywords (comma-separated)?") %>
---

# 🚀 Ship: <% tp.file.title %>

- **Class:** <% tp.frontmatter.class %>
- **Hull Points:** <% tp.frontmatter.hull_points %>
- **Speed:** <% tp.frontmatter.speed %>
- **Armor:** <% tp.frontmatter.armor %>
- **Crew:** <% tp.frontmatter.crew %>
- **Faction:** <% tp.frontmatter.faction %>
- **Tags:** <% tp.frontmatter.tags %>

## Description

## Armaments

## Modifications

## Quirks or Secrets

## Hooks
