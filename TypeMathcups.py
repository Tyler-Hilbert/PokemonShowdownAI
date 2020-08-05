# Data for all type matchups in Python code

NORMAL = "Normal"
SUPER_EFFECTIVE = "Super effective"
NOT_VERY_EFFECTIVE = NOT_VERY_EFFECTIVE
IMMUNE = IMMUNE

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
	"Bug": NORMAL,
	"Dark": NORMAL,
	"Dragon": SUPER_EFFECTIVE,
	"Electric": NOT_VERY_EFFECTIVE,
	"Fairy": SUPER_EFFECTIVE,
	"Fighting": NORMAL,
	"Fire": NOT_VERY_EFFECTIVE,
	"Flying": NORMAL,
	"Ghost": NORMAL,
	"Grass": NOT_VERY_EFFECTIVE,
	"Ground": NORMAL,
	"Ice": SUPER_EFFECTIVE,
	"Normal": NORMAL,
	"Poison": NORMAL,
	"Psychic": NORMAL,
	"Rock": NORMAL,
	"Steel": NORMAL,
	"Water": NOT_VERY_EFFECTIVE
}

electricDefending = {
	"Par": IMMUNE,
	"Bug": NORMAL,
	"Dark": NORMAL,
	"Dragon": NORMAL,
	"Electric": NOT_VERY_EFFECTIVE,
	"Fairy": NORMAL,
	"Fighting": NORMAL,
	"Fire": NORMAL,
	"Flying": NOT_VERY_EFFECTIVE,
	"Ghost": NORMAL,
	"Grass": NORMAL,
	"Ground": SUPER_EFFECTIVE,
	"Ice": NORMAL,
	"Normal": NORMAL,
	"Poison": NORMAL,
	"Psychic": NORMAL,
	"Rock": NORMAL,
	"Steel": NOT_VERY_EFFECTIVE,
	"Water": NORMAL
}

fairyDefending: {
	"Bug": NOT_VERY_EFFECTIVE,
	"Dark": NOT_VERY_EFFECTIVE,
	"Dragon": IMMUNE,
	"Electric": NORMAL,
	"Fairy": NORMAL,
	"Fighting": NOT_VERY_EFFECTIVE,
	"Fire": NORMAL,
	"Flying": NORMAL,
	"Ghost": NORMAL,
	"Grass": NORMAL,
	"Ground": NORMAL,
	"Ice": NORMAL,
	"Normal": NORMAL,
	"Poison": SUPER_EFFECTIVE,
	"Psychic": NORMAL,
	"Rock": NORMAL,
	"Steel": SUPER_EFFECTIVE,
	"Water": NORMAL
}

fightingDefending = {
	"Bug": NOT_VERY_EFFECTIVE,
	"Dark": NOT_VERY_EFFECTIVE,
	"Dragon": NORMAL,
	"Electric": NORMAL,
	"Fairy": SUPER_EFFECTIVE,
	"Fighting": NORMAL,
	"Fire": NORMAL,
	"Flying": SUPER_EFFECTIVE,
	"Ghost": NORMAL,
	"Grass": NORMAL,
	"Ground": NORMAL,
	"Ice": NORMAL,
	"Normal": NORMAL,
	"Poison": NORMAL,
	"Psychic": SUPER_EFFECTIVE,
	"Rock": NOT_VERY_EFFECTIVE,
	"Steel": NORMAL,
	"Water": NORMAL
}


fireDefending = {
	"Brn": IMMUNE,
	"Bug": NOT_VERY_EFFECTIVE,
	"Dark": NORMAL,
	"Dragon": NORMAL,
	"Electric": NORMAL,
	"Fairy": NOT_VERY_EFFECTIVE,
	"Fighting": NORMAL,
	"Fire": NOT_VERY_EFFECTIVE,
	"Flying": NORMAL,
	"Ghost": NORMAL,
	"Grass": NOT_VERY_EFFECTIVE,
	"Ground": SUPER_EFFECTIVE,
	"Ice": NOT_VERY_EFFECTIVE,
	"Normal": NORMAL,
	"Poison": NORMAL,
	"Psychic": NORMAL,
	"Rock": SUPER_EFFECTIVE,
	"Steel": NOT_VERY_EFFECTIVE,
	"Water": SUPER_EFFECTIVE
}

flyingDefending = {
	"Bug": NOT_VERY_EFFECTIVE,
	"Dark": NORMAL,
	"Dragon": NORMAL,
	"Electric": SUPER_EFFECTIVE,
	"Fairy": NORMAL,
	"Fighting": NOT_VERY_EFFECTIVE,
	"Fire": NORMAL,
	"Flying": NORMAL,
	"Ghost": NORMAL,
	"Grass": NOT_VERY_EFFECTIVE,
	"Ground": IMMUNE,
	"Ice": SUPER_EFFECTIVE,
	"Normal": NORMAL,
	"Poison": NORMAL,
	"Psychic": NORMAL,
	"Rock": SUPER_EFFECTIVE,
	"Steel": NORMAL,
	"Water": NORMAL
}

ghostDefending = {
	"Trapped": IMMUNE,
	"Bug": NOT_VERY_EFFECTIVE,
	"Dark": SUPER_EFFECTIVE,
	"Dragon": NORMAL,
	"Electric": NORMAL,
	"Fairy": NORMAL,
	"Fighting": IMMUNE,
	"Fire": NORMAL,
	"Flying": NORMAL,
	"Ghost": SUPER_EFFECTIVE,
	"Grass": NORMAL,
	"Ground": NORMAL,
	"Ice": NORMAL,
	"Normal": IMMUNE,
	"Poison": NOT_VERY_EFFECTIVE,
	"Psychic": NORMAL,
	"Rock": NORMAL,
	"Steel": NORMAL,
	"Water": NORMAL
}

grassDefending = {
	"Powder": IMMUNE,
	"Bug": SUPER_EFFECTIVE,
	"Dark": NORMAL,
	"Dragon": NORMAL,
	"Electric": NOT_VERY_EFFECTIVE,
	"Fairy": NORMAL,
	"Fighting": NORMAL,
	"Fire": SUPER_EFFECTIVE,
	"Flying": SUPER_EFFECTIVE,
	"Ghost": NORMAL,
	"Grass": NOT_VERY_EFFECTIVE,
	"Ground": NOT_VERY_EFFECTIVE,
	"Ice": SUPER_EFFECTIVE,
	"Normal": NORMAL,
	"Poison": SUPER_EFFECTIVE,
	"Psychic": NORMAL,
	"Rock": NORMAL,
	"Steel": NORMAL,
	"Water": NOT_VERY_EFFECTIVE
}

groundDefending = {
	"Sandstorm": IMMUNE,
	"Bug": NORMAL,
	"Dark": NORMAL,
	"Dragon": NORMAL,
	"Electric": IMMUNE,
	"Fairy": NORMAL,
	"Fighting": NORMAL,
	"Fire": NORMAL,
	"Flying": NORMAL,
	"Ghost": NORMAL,
	"Grass": SUPER_EFFECTIVE,
	"Ground": NORMAL,
	"Ice": SUPER_EFFECTIVE,
	"Normal": NORMAL,
	"Poison": NOT_VERY_EFFECTIVE,
	"Psychic": NORMAL,
	"Rock": NOT_VERY_EFFECTIVE,
	"Steel": NORMAL,
	"Water": SUPER_EFFECTIVE
}

iceDefending = {
	"Hail": IMMUNE,
	"Frz": IMMUNE,
	"Bug": NORMAL,
	"Dark": NORMAL,
	"Dragon": NORMAL,
	"Electric": NORMAL,
	"Fairy": NORMAL,
	"Fighting": SUPER_EFFECTIVE,
	"Fire": SUPER_EFFECTIVE,
	"Flying": NORMAL,
	"Ghost": NORMAL,
	"Grass": NORMAL,
	"Ground": NORMAL,
	"Ice": NOT_VERY_EFFECTIVE,
	"Normal": NORMAL,
	"Poison": NORMAL,
	"Psychic": NORMAL,
	"Rock": SUPER_EFFECTIVE,
	"Steel": SUPER_EFFECTIVE,
	"Water": NORMAL
}

normalDefending = {
	"Bug": NORMAL,
	"Dark": NORMAL,
	"Dragon": NORMAL,
	"Electric": NORMAL,
	"Fairy": NORMAL,
	"Fighting": SUPER_EFFECTIVE,
	"Fire": NORMAL,
	"Flying": NORMAL,
	"Ghost": IMMUNE,
	"Grass": NORMAL,
	"Ground": NORMAL,
	"Ice": NORMAL,
	"Normal": NORMAL,
	"Poison": NORMAL,
	"Psychic": NORMAL,
	"Rock": NORMAL,
	"Steel": NORMAL,
	"Water": NORMAL
}

poisonDefending = {
	"Psn": IMMUNE,
	"Tox": IMMUNE,
	"Bug": NOT_VERY_EFFECTIVE,
	"Dark": NORMAL,
	"Dragon": NORMAL,
	"Electric": NORMAL,
	"Fairy": NOT_VERY_EFFECTIVE,
	"Fighting": NOT_VERY_EFFECTIVE,
	"Fire": NORMAL,
	"Flying": NORMAL,
	"Ghost": NORMAL,
	"Grass": NOT_VERY_EFFECTIVE,
	"Ground": SUPER_EFFECTIVE,
	"Ice": NORMAL,
	"Normal": NORMAL,
	"Poison": NOT_VERY_EFFECTIVE,
	"Psychic": SUPER_EFFECTIVE,
	"Rock": NORMAL,
	"Steel": NORMAL,
	"Water": NORMAL
}

psychicDefending = {
	"Bug": SUPER_EFFECTIVE,
	"Dark": SUPER_EFFECTIVE,
	"Dragon": NORMAL,
	"Electric": NORMAL,
	"Fairy": NORMAL,
	"Fighting": NOT_VERY_EFFECTIVE,
	"Fire": NORMAL,
	"Flying": NORMAL,
	"Ghost": SUPER_EFFECTIVE,
	"Grass": NORMAL,
	"Ground": NORMAL,
	"Ice": NORMAL,
	"Normal": NORMAL,
	"Poison": NORMAL,
	"Psychic": NOT_VERY_EFFECTIVE,
	"Rock": NORMAL,
	"Steel": NORMAL,
	"Water": NORMAL
}

rockDefending = {
	"Sandstorm": IMMUNE,
	"Bug": NORMAL,
	"Dark": NORMAL,
	"Dragon": NORMAL,
	"Electric": NORMAL,
	"Fairy": NORMAL,
	"Fighting": SUPER_EFFECTIVE,
	"Fire": NOT_VERY_EFFECTIVE,
	"Flying": NOT_VERY_EFFECTIVE,
	"Ghost": NORMAL,
	"Grass": SUPER_EFFECTIVE,
	"Ground": SUPER_EFFECTIVE,
	"Ice": NORMAL,
	"Normal": NOT_VERY_EFFECTIVE,
	"Poison": NOT_VERY_EFFECTIVE,
	"Psychic": NORMAL,
	"Rock": NORMAL,
	"Steel": SUPER_EFFECTIVE,
	"Water": SUPER_EFFECTIVE
}

steelDefending = {
	"Psn": IMMUNE,
	"Tox": IMMUNE,
	"Sandstorm": IMMUNE,
	"Bug": NOT_VERY_EFFECTIVE,
	"Dark": NORMAL,
	"Dragon": NOT_VERY_EFFECTIVE,
	"Electric": NORMAL,
	"Fairy": NOT_VERY_EFFECTIVE,
	"Fighting": SUPER_EFFECTIVE,
	"Fire": SUPER_EFFECTIVE,
	"Flying": NOT_VERY_EFFECTIVE,
	"Ghost": NORMAL,
	"Grass": NOT_VERY_EFFECTIVE,
	"Ground": SUPER_EFFECTIVE,
	"Ice": NOT_VERY_EFFECTIVE,
	"Normal": NOT_VERY_EFFECTIVE,
	"Poison": IMMUNE,
	"Psychic": NOT_VERY_EFFECTIVE,
	"Rock": NOT_VERY_EFFECTIVE,
	"Steel": NOT_VERY_EFFECTIVE,
	"Water": NORMAL
}

waterDefending = {
	"Bug": NORMAL,
	"Dark": NORMAL,
	"Dragon": NORMAL,
	"Electric": SUPER_EFFECTIVE,
	"Fairy": NORMAL,
	"Fighting": NORMAL,
	"Fire": NOT_VERY_EFFECTIVE,
	"Flying": NORMAL,
	"Ghost": NORMAL,
	"Grass": SUPER_EFFECTIVE,
	"Ground": NORMAL,
	"Ice": NOT_VERY_EFFECTIVE,
	"Normal": NORMAL,
	"Poison": NORMAL,
	"Psychic": NORMAL,
	"Rock": NORMAL,
	"Steel": NOT_VERY_EFFECTIVE,
	"Water": NOT_VERY_EFFECTIVE
}
