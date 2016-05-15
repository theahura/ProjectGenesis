"""
@date: 5-13-16

Description: Defines the cluster parent class
"""


class Cluster: 
    """Defines the cluster parent class, which contains basic methods common to
    all character, setting, thing clusters"""
    
    def __init__(self, name, type, characters=None, settings=None, things=None):
        self.name = name
        self.type = type

        self.characters = characters
        self.settings = settings
        self.things = things

