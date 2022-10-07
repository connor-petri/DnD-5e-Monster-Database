import json 
import textwrap

def load_monster_data():
    with open("./resources/data.json", "r", encoding="utf8") as data_object:
        monster_data = json.load(data_object)
    return monster_data


# Used in parsing methods.
def merge_dict_list(dict_list):
    merged_dict = {}
    for i in dict_list:
        merged_dict.update(i)
    return merged_dict


# Monster dict generator
def monster_generator(data):
    for monster in data["monsters"]:
        yield Monster(monster[1])


# image, name, size, type, alignment, ac, hp, hit_dice, speed, stats, saves, skillsaves, damage_vulnerabilities, damage_resistances, damage_immunities,
# condition_immunities, senses, languages, cr, traits, spells, actions, lengendary_actions, reactions, source


class Monster:
    def __init__(self, monster_dict):
        self._image = monster_dict.get("image", None)
        self._name = monster_dict.get("name", None)
        self._size = monster_dict.get("size", None)
        self._type = monster_dict.get("type", None)
        self._alignment = monster_dict.get("alignment", None)
        self._ac = monster_dict.get("ac", None)
        self._hp = monster_dict.get("hp", None)
        self._hit_dice = monster_dict.get("hit_dice", None)
        self._speed = monster_dict.get("speed", None)
        self._stats = monster_dict.get("stats", None)
        self._saves = monster_dict.get("saves", None)
        self._skillsaves = monster_dict.get("skillsaves", None)
        self._damage_vulnerabilities = monster_dict.get("damage_vulnerabilities", None)
        self._damage_resistances = monster_dict.get("damage_resistances", None)
        self._damage_immunities = monster_dict.get("damage_immunities", None)
        self._condition_immunities = monster_dict.get("condition_immunities", None)
        self._senses = monster_dict.get("senses", None) 
        self._languages = monster_dict.get("languages", None)
        self._cr = monster_dict.get("cr", None)
        self._traits = monster_dict.get("traits", None)
        self._spells = monster_dict.get("spells", None)
        self._actions = monster_dict.get("actions", None)
        self._legendary_actions = monster_dict.get("legendary_actions", None)
        self._reactions = monster_dict.get("reactions", None)
        self._source = monster_dict.get("source", None)

        self.text_wrap_max = 63


    # Getters
    def getImage(self):
        return self._image
    def getName(self):
        return self._name
    def getSize(self):
        return self._size
    def getType(self):
        return self._type
    def getAlignment(self):
        return self._alignment
    def getAc(self):
        return self._ac
    def getHp(self):
        return self._hp
    def getHitDice(self):
        return self._hit_dice
    def getSpeed(self):
        return self._speed
    def getStats(self):
        return self._stats
    def getSaves(self):
        return self._saves
    def getSkillSaves(self):
        return self._skillsaves
    def getDamageVulnerabilities(self):
        return self._damage_vulnerabilities
    def getDamageResistances(self):
        return self._damage_resistances
    def getDamageImmunities(self):
        return self._damage_immunities
    def getConditionImmunities(self):
        return self._condition_immunities
    def getSenses(self):
        return self._senses
    def getLanguages(self):
        return self._languages
    def getCr(self):
        return self._cr
    def getTraits(self):
        return self._traits
    def getSpells(self):
        return self._spells
    def getActions(self):
        return self._actions
    def getLegendaryActions(self):
        return self._legendary_actions
    def getReactions(self):
        return self._reactions
    def getSource(self):
        return self._source


    def add_stat_modifier(self, stat):

        modifier = stat - 10

        if modifier % 2 != 0:
            modifier -= 1

        modifier /= 2

        if modifier >= 0:
            return f'{stat} (+{int(modifier)})'
        else:
            return f'{stat} ({int(modifier)})'


    def parse_saves(self):
        saves_dict = merge_dict_list(self.getSaves())
        output = ""

        for key, value in saves_dict.items():
            if value is None:
                break

            stat = key[:3].upper()
            output += f"{stat}: {value}, "
        
        return output[:-2]


    def parse_skillsaves(self):
        skillsaves_dict = merge_dict_list(self.getSkillSaves())
        output = ""

        for key, value in skillsaves_dict.items():
            if value is None:
                break

            output += f"{key}, {value}, "

        return textwrap.fill(output[:-2], 80)
    

    # used for traits, actions, and legenday actions
    def parse_actions(self, list, header, text_wrap_max):
        output = f'{header}\n\n'

        for action in list:
            name = action["name"]
            desc = action["desc"]
    
            output += textwrap.fill(f'{name}: {desc}', text_wrap_max) + '\n\n'
        
        return output


    def parse_spells(self):
        output = 'Spells:\n\n'
        title = True

        for line in self.getSpells():
            output += line + '\n'

            if title:
                output += '\n'
                title = False

        return output


    def make_stat_block(self, window):

        def update_value(key, value):
            window[key].update(value)


        # If you add a new thing to the stat block or layout that you want updated from this method,
        # include the element key and the value you want passed to it in run_dict as a key: value pair.
        run_dict = {
            '-name-': self.getName(),
            '-size_type_alignment-': f'{self.getSize()} {self.getType()}, {self.getAlignment()}',
            # ----------------------------------------------------------
            '-ac-': self.getAc(),
            '-hp-': f'{self.getHp()} ({self.getHitDice()})',
            '-speed-': self.getSpeed(),
            # ----------------------------------------------------------
            '-str-': self.add_stat_modifier(self.getStats()[0]),
            '-dex-': self.add_stat_modifier(self.getStats()[1]),
            '-con-': self.add_stat_modifier(self.getStats()[2]),
            '-int-': self.add_stat_modifier(self.getStats()[3]),
            '-wis-': self.add_stat_modifier(self.getStats()[4]),
            '-cha-': self.add_stat_modifier(self.getStats()[5]),
            # ----------------------------------------------------------
            '-saving_throws-': self.parse_saves(),
            '-skillsaves-': self.parse_skillsaves(),
            '-d_vulnerabilities-': textwrap.fill(self.getDamageVulnerabilities(), self.text_wrap_max),
            '-d_resistances-': textwrap.fill(self.getDamageResistances(), self.text_wrap_max),
            '-d_immunities-': textwrap.fill(self.getDamageImmunities(), self.text_wrap_max),
            '-c_immunities-': textwrap.fill(self.getConditionImmunities(), self.text_wrap_max),
            '-senses-': textwrap.fill(self.getSenses(), self.text_wrap_max),
            '-languages-': textwrap.fill(self.getLanguages(), self.text_wrap_max),
            '-cr-': self.getCr(),
            # ----------------------------------------------------------
            '-traits-': self.parse_actions(self.getTraits(), 'Traits:', 75),
            # ----------------------------------------------------------
            '-spells-': self.parse_spells(),
            # ----------------------------------------------------------
            '-actions-': self.parse_actions(self.getActions(), 'Actions:', self.text_wrap_max),
            # ----------------------------------------------------------
            '-legendary_actions-': self.parse_actions(self.getLegendaryActions(), 'Legendary Actions:', self.text_wrap_max)
        }


        for key, value in run_dict.items():
            update_value(key, value)
    
    


