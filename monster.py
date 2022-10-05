import json 

with open("./data.json", "r", encoding="utf8") as data_object:
    monster_data = json.load(data_object)


# Tools
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


    def parse_saves(self):
        saves_dict = merge_dict_list(self.getSaves())
        output = ""
        for key, value in saves_dict.items():
            stat = key[:3].upper()
            output += f"{stat}: {value}, "
        return output[:-2]

    def parse_skillsaves(self):
        skillsaves_dict = merge_dict_list(self.getSkillSaves())
        output = ""
        for key, value in skillsaves_dict.items():
            output += f"{key}, {value}, "
        return output[:-2]
    
    # used for traits, actions, and legenday actions
    def parse_actions(self, list):

        output = '''
        |'''

        for action in list:
            name = action["name"]
            desc = action["desc"]
            
            new_action = f"""
        |   {name}:
        |   {desc[:120]}"""

            if len(desc) > 120:
                new_action += f'''
        |   {desc[120:240]}'''

            if len(desc) > 240:
                new_action += f'''
        |   {desc[240:360]}'''

            if len(desc) > 360:
                    new_action += f'''
        |   {desc[360:480]}'''

            if len(desc) > 480:
                    new_action += f'''
        |   {desc[480:600]}'''

            new_action += '''
        |'''
            output += new_action
        
        output +='''_______________________________________________________________________________________________________'''

        return output

    def parse_spells(self):

        output = '''
        |
        |'''

        for line in self.getSpells():
            if len(line) > 120:
                split_line = line.split("). ")
                output += f'''  {split_line[0]}).
        |  {split_line[1]}
        |'''

            else:
                output += f'''
        |   {line} '''


        output +='''
        |_______________________________________________________________________________________________________'''

        return output



    def make_stat_block(self):
        main_body = f'''
         _______________________________________________________________________________________________________
        |
        |   {self.getName()}
        |   {self.getSize().title()} {self.getType().title()}, {self.getAlignment().title()}
        |
        |_______________________________________________________________________________________________________
        |
        |   Armor Class: {self.getAc()}
        |   Hit Points: {self.getHp()} ({self.getHitDice()})
        |   Speed: {self.getSpeed()}
        |_______________________________________________________________________________________________________
        |
        |   STR: {self.getStats()[0]}   DEX: {self.getStats()[1]}   CON: {self.getStats()[2]}
        | 
        |   INT: {self.getStats()[3]}   WIS: {self.getStats()[4]}   CHA: {self.getStats()[5]}
        |_______________________________________________________________________________________________________
        |
        |   Saving Throws: {self.parse_saves()}
        |   Skills: {self.parse_skillsaves()}
        |   Damage Vulnerabilities: {self.getDamageVulnerabilities()} 
        |   Damage Resistances: {self.getDamageResistances()}
        |   Damage Immunities: {self.getDamageImmunities()}
        |   Condition Immunities: {self.getConditionImmunities()}
        |   Languages: {self.getLanguages()}
        |   Challenge: {self.getCr()}
        |_______________________________________________________________________________________________________'''
        main_body += self.parse_actions(self.getTraits()) + self.parse_spells() + self.parse_actions(self.getActions()) + self.parse_actions(self.getLegendaryActions())
        return main_body


