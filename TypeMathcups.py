# Data for all type matchups in Python code

NORMAL = "Normal"
SUPER_EFFECTIVE = "Super effective"
NOT_VERY_EFFECTIVE = "Not very effective"
IMMUNE = "Immune"

bugDefending = {
    "Bug": NORMAL,
    "Dark": NORMAL,
    "Dragon": NORMAL,
    "Electric": NORMAL,
    "Fairy": NORMAL,
    "Fighting": NOT_VERY_EFFECTIVE,
    "Fire": SUPER_EFFECTIVE,
    "Flying": SUPER_EFFECTIVE,
    "Ghost": NORMAL,
    "Grass": NOT_VERY_EFFECTIVE,
    "Ground": NOT_VERY_EFFECTIVE,
    "Ice": NOT_VERY_EFFECTIVE,
    "Normal": NORMAL,
    "Poison": NORMAL,
    "Psychic": NORMAL,
    "Rock": SUPER_EFFECTIVE,
    "Steel": NORMAL,
    "Water": NORMAL
}

darkDefending = {
	"Bug": NOT_VERY_EFFECTIVE,
	"Dark": SUPER_EFFECTIVE,
	"Dragon": NORMAL,
	"Electric": NORMAL,
	"Fairy": NOT_VERY_EFFECTIVE,
	"Fighting": NOT_VERY_EFFECTIVE,
	"Fire": NORMAL,
	"Flying": NORMAL,
	"Ghost": SUPER_EFFECTIVE,
	"Grass": NORMAL,
	"Ground": NORMAL,
	"Ice": NORMAL,
	"Normal": NORMAL,
	"Poison": NORMAL,
	"Psychic": IMMUNE,
	"Rock": NORMAL,
	"Steel": NORMAL,
	"Water": NORMAL
}

dragonDefending = {
	"Bug": "Normal",
	"Dark": "Normal",
	"Dragon": SUPER_EFFECTIVE,
	"Electric": "Not very effective",
	"Fairy": SUPER_EFFECTIVE,
	"Fighting": "Normal",
	"Fire": "Not very effective",
	"Flying": "Normal",
	"Ghost": "Normal",
	"Grass": "Not very effective",
	"Ground": "Normal",
	"Ice": SUPER_EFFECTIVE,
	"Normal": "Normal",
	"Poison": "Normal",
	"Psychic": "Normal",
	"Rock": "Normal",
	"Steel": "Normal",
	"Water": "Not very effective"
}

electricDefending = {
	"Par": "Immune",
	"Bug": "Normal",
	"Dark": "Normal",
	"Dragon": "Normal",
	"Electric": "Not very effective",
	"Fairy": "Normal",
	"Fighting": "Normal",
	"Fire": "Normal",
	"Flying": "Not very effective",
	"Ghost": "Normal",
	"Grass": "Normal",
	"Ground": SUPER_EFFECTIVE,
	"Ice": "Normal",
	"Normal": "Normal",
	"Poison": "Normal",
	"Psychic": "Normal",
	"Rock": "Normal",
	"Steel": "Not very effective",
	"Water": "Normal"
}

fairyDefending: {
	"Bug": "Not very effective",
	"Dark": "Not very effective",
	"Dragon": "Immune",
	"Electric": "Normal",
	"Fairy": "Normal",
	"Fighting": "Not very effective",
	"Fire": "Normal",
	"Flying": "Normal",
	"Ghost": "Normal",
	"Grass": "Normal",
	"Ground": "Normal",
	"Ice": "Normal",
	"Normal": "Normal",
	"Poison": SUPER_EFFECTIVE,
	"Psychic": "Normal",
	"Rock": "Normal",
	"Steel": SUPER_EFFECTIVE,
	"Water": "Normal"
}

fightingDefending = {
	"Bug": "Not very effective",
	"Dark": "Not very effective",
	"Dragon": "Normal",
	"Electric": "Normal",
	"Fairy": SUPER_EFFECTIVE,
	"Fighting": "Normal",
	"Fire": "Normal",
	"Flying": SUPER_EFFECTIVE,
	"Ghost": "Normal",
	"Grass": "Normal",
	"Ground": "Normal",
	"Ice": "Normal",
	"Normal": "Normal",
	"Poison": "Normal",
	"Psychic": SUPER_EFFECTIVE,
	"Rock": "Not very effective",
	"Steel": "Normal",
	"Water": "Normal"
}


fireDefending = {
	"Brn": "Immune",
	"Bug": "Not very effective",
	"Dark": "Normal",
	"Dragon": "Normal",
	"Electric": "Normal",
	"Fairy": "Not very effective",
	"Fighting": "Normal",
	"Fire": "Not very effective",
	"Flying": "Normal",
	"Ghost": "Normal",
	"Grass": "Not very effective",
	"Ground": SUPER_EFFECTIVE,
	"Ice": "Not very effective",
	"Normal": "Normal",
	"Poison": "Normal",
	"Psychic": "Normal",
	"Rock": SUPER_EFFECTIVE,
	"Steel": "Not very effective",
	"Water": SUPER_EFFECTIVE
}

flyingDefending = {
	"Bug": "Not very effective",
	"Dark": "Normal",
	"Dragon": "Normal",
	"Electric": SUPER_EFFECTIVE,
	"Fairy": "Normal",
	"Fighting": "Not very effective",
	"Fire": "Normal",
	"Flying": "Normal",
	"Ghost": "Normal",
	"Grass": "Not very effective",
	"Ground": "Immune",
	"Ice": SUPER_EFFECTIVE,
	"Normal": "Normal",
	"Poison": "Normal",
	"Psychic": "Normal",
	"Rock": SUPER_EFFECTIVE,
	"Steel": "Normal",
	"Water": "Normal"
}

ghostDefending = {
	"Trapped": "Immune",
	"Bug": "Not very effective",
	"Dark": SUPER_EFFECTIVE,
	"Dragon": "Normal",
	"Electric": "Normal",
	"Fairy": "Normal",
	"Fighting": "Immune",
	"Fire": "Normal",
	"Flying": "Normal",
	"Ghost": SUPER_EFFECTIVE,
	"Grass": "Normal",
	"Ground": "Normal",
	"Ice": "Normal",
	"Normal": "Immune",
	"Poison": "Not very effective",
	"Psychic": "Normal",
	"Rock": "Normal",
	"Steel": "Normal",
	"Water": "Normal"
}

grassDefending = {
	"Powder": "Immune",
	"Bug": SUPER_EFFECTIVE,
	"Dark": "Normal",
	"Dragon": "Normal",
	"Electric": "Not very effective",
	"Fairy": "Normal",
	"Fighting": "Normal",
	"Fire": SUPER_EFFECTIVE,
	"Flying": SUPER_EFFECTIVE,
	"Ghost": "Normal",
	"Grass": "Not very effective",
	"Ground": "Not very effective",
	"Ice": SUPER_EFFECTIVE,
	"Normal": "Normal",
	"Poison": SUPER_EFFECTIVE,
	"Psychic": "Normal",
	"Rock": "Normal",
	"Steel": "Normal",
	"Water": "Not very effective"
}

groundDefending = {
	"Sandstorm": "Immune",
	"Bug": "Normal",
	"Dark": "Normal",
	"Dragon": "Normal",
	"Electric": "Immune",
	"Fairy": "Normal",
	"Fighting": "Normal",
	"Fire": "Normal",
	"Flying": "Normal",
	"Ghost": "Normal",
	"Grass": SUPER_EFFECTIVE,
	"Ground": "Normal",
	"Ice": SUPER_EFFECTIVE,
	"Normal": "Normal",
	"Poison": "Not very effective",
	"Psychic": "Normal",
	"Rock": "Not very effective",
	"Steel": "Normal",
	"Water": SUPER_EFFECTIVE
}

iceDefending = {
	"Hail": "Immune",
	"Frz": "Immune",
	"Bug": "Normal",
	"Dark": "Normal",
	"Dragon": "Normal",
	"Electric": "Normal",
	"Fairy": "Normal",
	"Fighting": SUPER_EFFECTIVE,
	"Fire": SUPER_EFFECTIVE,
	"Flying": "Normal",
	"Ghost": "Normal",
	"Grass": "Normal",
	"Ground": "Normal",
	"Ice": "Not very effective",
	"Normal": "Normal",
	"Poison": "Normal",
	"Psychic": "Normal",
	"Rock": SUPER_EFFECTIVE,
	"Steel": SUPER_EFFECTIVE,
	"Water": "Normal"
}

normalDefending = {
	"Bug": "Normal",
	"Dark": "Normal",
	"Dragon": "Normal",
	"Electric": "Normal",
	"Fairy": "Normal",
	"Fighting": SUPER_EFFECTIVE,
	"Fire": "Normal",
	"Flying": "Normal",
	"Ghost": "Immune",
	"Grass": "Normal",
	"Ground": "Normal",
	"Ice": "Normal",
	"Normal": "Normal",
	"Poison": "Normal",
	"Psychic": "Normal",
	"Rock": "Normal",
	"Steel": "Normal",
	"Water": "Normal"
}

poisonDefending = {
	"Psn": "Immune",
	"Tox": "Immune",
	"Bug": "Not very effective",
	"Dark": "Normal",
	"Dragon": "Normal",
	"Electric": "Normal",
	"Fairy": "Not very effective",
	"Fighting": "Not very effective",
	"Fire": "Normal",
	"Flying": "Normal",
	"Ghost": "Normal",
	"Grass": "Not very effective",
	"Ground": SUPER_EFFECTIVE,
	"Ice": "Normal",
	"Normal": "Normal",
	"Poison": "Not very effective",
	"Psychic": SUPER_EFFECTIVE,
	"Rock": "Normal",
	"Steel": "Normal",
	"Water": "Normal"
}

psychicDefending = {
	"Bug": SUPER_EFFECTIVE,
	"Dark": SUPER_EFFECTIVE,
	"Dragon": "Normal",
	"Electric": "Normal",
	"Fairy": "Normal",
	"Fighting": "Not very effective",
	"Fire": "Normal",
	"Flying": "Normal",
	"Ghost": SUPER_EFFECTIVE,
	"Grass": "Normal",
	"Ground": "Normal",
	"Ice": "Normal",
	"Normal": "Normal",
	"Poison": "Normal",
	"Psychic": "Not very effective",
	"Rock": "Normal",
	"Steel": "Normal",
	"Water": "Normal"
}

rockDefending = {
	"Sandstorm": "Immune",
	"Bug": "Normal",
	"Dark": "Normal",
	"Dragon": "Normal",
	"Electric": "Normal",
	"Fairy": "Normal",
	"Fighting": SUPER_EFFECTIVE,
	"Fire": "Not very effective",
	"Flying": "Not very effective",
	"Ghost": "Normal",
	"Grass": SUPER_EFFECTIVE,
	"Ground": SUPER_EFFECTIVE,
	"Ice": "Normal",
	"Normal": "Not very effective",
	"Poison": "Not very effective",
	"Psychic": "Normal",
	"Rock": "Normal",
	"Steel": SUPER_EFFECTIVE,
	"Water": SUPER_EFFECTIVE
}

steelDefending = {
	"Psn": "Immune",
	"Tox": "Immune",
	"Sandstorm": "Immune",
	"Bug": "Not very effective",
	"Dark": "Normal",
	"Dragon": "Not very effective",
	"Electric": "Normal",
	"Fairy": "Not very effective",
	"Fighting": SUPER_EFFECTIVE,
	"Fire": SUPER_EFFECTIVE,
	"Flying": "Not very effective",
	"Ghost": "Normal",
	"Grass": "Not very effective",
	"Ground": SUPER_EFFECTIVE,
	"Ice": "Not very effective",
	"Normal": "Not very effective",
	"Poison": "Immune",
	"Psychic": "Not very effective",
	"Rock": "Not very effective",
	"Steel": "Not very effective",
	"Water": "Normal"
}

waterDefending = {
	"Bug": "Normal",
	"Dark": "Normal",
	"Dragon": "Normal",
	"Electric": SUPER_EFFECTIVE,
	"Fairy": "Normal",
	"Fighting": "Normal",
	"Fire": "Not very effective",
	"Flying": "Normal",
	"Ghost": "Normal",
	"Grass": SUPER_EFFECTIVE,
	"Ground": "Normal",
	"Ice": "Not very effective",
	"Normal": "Normal",
	"Poison": "Normal",
	"Psychic": "Normal",
	"Rock": "Normal",
	"Steel": "Not very effective",
	"Water": "Not very effective"
}
