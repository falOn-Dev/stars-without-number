import os

cyberware_list = [
    {"name": "Adrenal Suppression Pump", "cost": 30000, "strain": 1, "tl": "TL4", "category": "combat",
     "desc": "A concealed glandular implant that monitors and moderates hormone levels. When activated, it floods the body with chemical suppressors, eliminating fear, anger, or hesitation. The user gains a cold, detached demeanor in stressful situations, ideal for combat scenarios.",
     "effect": "+2 initiative; -2 on all social skill checks while active."},
    {"name": "Bioadaptation Augments", "cost": 10000, "strain": 1, "tl": "TL4", "category": "utility",
     "desc": "Subtle modifications to the user’s internal organs allow survival on near-habitable worlds. Respiratory systems adjust to trace atmospheres, and metabolic regulators prevent poisoning from minor contaminants.",
     "effect": "Survive hostile atmospheres without vacc suit on near-habitable worlds."},
    {"name": "Body Arsenal Array", "cost": 10000, "strain": 1, "tl": "TL4", "category": "combat",
     "desc": "Mechanical mounts hidden beneath the skin house retractable weapons. A simple neural impulse brings medium weapons or a laser rifle into the user's hands, transforming them into a walking arsenal.",
     "effect": "Conceals medium weapon and laser rifle in body; deploy as needed."},
    {"name": "Body Sculpting", "cost": 10000, "strain": 1, "tl": "TL4", "category": "utility",
     "desc": "A suite of tissue re-sculpting implants that allow dramatic alteration of the user’s appearance. Skin tone, facial features, and body shape can be changed at will, enabling new identities or disguises.",
     "effect": "Alters appearance to desired specifications."},
    {"name": "Dermal Armor", "cost": 20000, "strain": 2, "tl": "TL4", "category": "combat",
     "desc": "A lattice of high-density polymer plating is bonded beneath the skin, forming invisible armor that resists bullets and blades. The user appears normal, but their skin can stop small arms fire.",
     "effect": "AC 16; immune to primitive weapon Shock."},
    {"name": "Drone Control Link", "cost": 20000, "strain": 1, "tl": "TL4", "category": "utility",
     "desc": "A neural interface that allows the user to control drones as if they were extensions of their body. Commands are issued at the speed of thought.",
     "effect": "Directly control drone via neural link, no remote required."},
    {"name": "Eelskin Capacitor Mesh", "cost": 25000, "strain": 1, "tl": "TL4", "category": "combat",
     "desc": "A flexible mesh beneath the skin stores and discharges electrical energy, allowing the user to emit a disabling shock. The system also scrambles unauthorized electrical intrusions.",
     "effect": "Emit electrical shock; immune to electrical hacking."},
    {"name": "Gecko Anchors", "cost": 15000, "strain": 1, "tl": "TL4", "category": "utility",
     "desc": "Specialized pads on hands and feet provide adhesion to surfaces, enabling the user to scale walls and ceilings with ease.",
     "effect": "Climb vertical and sheer surfaces unaided."},
    {"name": "Ghost Talker Transceiver", "cost": 15000, "strain": 1, "tl": "TL4", "category": "utility",
     "desc": "A built-in compad system integrated into the jawbone, providing clear audio-visual communication without external devices.",
     "effect": "Built-in comms device with audio and video."},
    {"name": "Holdout Cavity", "cost": 10000, "strain": 1, "tl": "TL4", "category": "stealth",
     "desc": "A surgically created hollow within the body for concealing small items or contraband, invisible to casual inspection.",
     "effect": "Conceal small item within body."},
    {"name": "Holoskin Emitters", "cost": 15000, "strain": 1, "tl": "TL4", "category": "stealth",
     "desc": "Microscopic projectors beneath the skin generate a lifelike holographic overlay, masking the user’s true appearance.",
     "effect": "Disguise appearance with projected holograms."},
    {"name": "Identity Submersion Trigger", "cost": 25000, "strain": 1, "tl": "TL4", "category": "stealth",
     "desc": "Embedded routines in the user’s neural pattern allow them to adopt a fully programmed secondary identity at will.",
     "effect": "Switches to secondary identity on demand."},
    {"name": "Immunofiltration System", "cost": 25000, "strain": 2, "tl": "TL4", "category": "medical",
     "desc": "Nanite-infused bloodstreams and enhanced organs neutralize toxins and pathogens before they can harm the user.",
     "effect": "Complete immunity to diseases and toxins."},
    {"name": "Induced Coma Trigger", "cost": 20000, "strain": 1, "tl": "TL4", "category": "stealth",
     "desc": "A self-controlled system that halts vital functions, allowing the user to convincingly feign death.",
     "effect": "Feign death, stop vital signs at will."},
    {"name": "Neurointruder Alert", "cost": 50000, "strain": 1, "tl": "Pretech", "category": "utility",
     "desc": "An advanced neural monitor that detects psychic intrusion attempts and shields the mind.",
     "effect": "+3 save vs telepathy; detects mental intrusion."},
    {"name": "Panspectral Optics", "cost": 15000, "strain": 1, "tl": "TL4", "category": "utility",
     "desc": "Cybernetic eyes capable of seeing across multiple spectra, including infrared and radio bands.",
     "effect": "See in low light, thermal, radio spectra."},
    {"name": "Pressure Sheathing", "cost": 15000, "strain": 1, "tl": "TL4", "category": "utility",
     "desc": "A hidden layer beneath the skin that can rigidify to provide short-term vacuum protection.",
     "effect": "Survive in vacuum for short durations."},
    {"name": "Prosthetic Limb", "cost": 2500, "strain": 1, "tl": "TL4", "category": "medical",
     "desc": "An artificial replacement for a lost limb, offering functionality equivalent to the original.",
     "effect": "Restores normal function of lost limb."},
    {"name": "Revenant Wiring", "cost": 50000, "strain": 3, "tl": "Pretech", "category": "combat",
     "desc": "A pretech marvel that keeps the body functional for a short time after fatal injury.",
     "effect": "Keep fighting for several rounds post-mortem."},
    {"name": "Slowtime Window", "cost": 30000, "strain": 2, "tl": "Pretech", "category": "utility",
     "desc": "A cortical accelerator that quickens mental processing and reaction speed in dangerous situations.",
     "effect": "Acts first in combat; immune to surprise."},
    {"name": "Stabilization Overrides", "cost": 25000, "strain": 2, "tl": "TL4", "category": "medical",
     "desc": "Automated systems that stabilize critical injuries without external aid.",
     "effect": "Auto-stabilizes at 0 HP."},
    {"name": "Tagger Nanites", "cost": 15000, "strain": 1, "tl": "TL4", "category": "utility",
     "desc": "Microscopic machines that allow the user to tag and track items remotely.",
     "effect": "Tag objects for remote tracking."},
    {"name": "Toxin Injector", "cost": 20000, "strain": 2, "tl": "TL4", "category": "combat",
     "desc": "A hidden injector system for delivering toxins or sedatives directly into a target.",
     "effect": "Inject toxins into targets covertly."},
    {"name": "Twitchlock Actuators", "cost": 30000, "strain": 2, "tl": "TL4", "category": "combat",
     "desc": "Enhanced muscle fibers and micro-actuators that improve manual precision and speed.",
     "effect": "Greatly improves manual precision and accuracy."}
]

output_dir = "Cyberware"
os.makedirs(output_dir, exist_ok=True)

def slugify(name):
    return name.lower().replace(" ", "_").replace("/", "_")

for c in cyberware_list:
    filename = os.path.join(output_dir, f"{c['name']}.md")
    tags = [
        "swn",
        "cyberware",
        f"cyberware/category/{c['category']}",
        f"cyberware/tech/{c['tl'].lower()}"
    ]
    content = f"""---
title: {c['name']}
type: cyberware
tags:
  - {'\n  - '.join(tags)}
cost: {c['cost']}
strain: {c['strain']}
tech_level: {c['tl']}
---

# 🤖 Cyberware: {c['name']}

- **Category:** {c['category'].capitalize()}
- **Cost:** {c['cost']} cr
- **Strain:** {c['strain']}
- **Tech Level:** {c['tl']}

## Description
{c['desc']}

## Game Effects
{c['effect']}

## Quirks / Side Effects

(Add quirks or side effects)

## Hooks / Uses

(Add hooks or uses)
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Generated {len(cyberware_list)} cyberware notes in '{output_dir}/'")
