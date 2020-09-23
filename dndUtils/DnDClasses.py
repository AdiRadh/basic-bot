from enum import Enum

from pip._internal.utils.misc import enum


class Setting:
    def __init__(self, name, description, races, players, NPC, Location):
        self.name = name
        self.description = description
        self.Races = races
        self.Players = players
        self.NPCs = NPC
        self.Locations = Location

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Alignment(enum):
    NEUTRAL = "Neutral"
    GOOD = "Good"
    EVIL = "Evil"


class Race:
    def __init__(self, name, description, perks):
        self.name = name
        self.description = description
        self.perks = perks


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class NPC:
    def __init__(self, name, description, health, skills, race):
        self.name = name
        self.description = description
        self.health = health
        self.skills = skills

    def takeDamage(self, damage):
        if self.health > 0:
            self.health - damage

    def getHealth(self):
        return self.health

    def getAllSkills(self, skillName):
        return self.skills


class Skill:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Player:
    def __init__(self, name, description, alignment, health, inventory):
        self.name = name
        self.description = description
        self.health = health
        self.alignment = alignment
        self.inventory = inventory
