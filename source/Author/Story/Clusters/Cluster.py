"""
@date: 5-13-16

Description: Defines the cluster parent class
"""


class Cluster: 
    """Defines the cluster parent class, which contains basic methods common to
    all character, setting, thing clusters"""
    
    def __init__(self, name, type, characters=None, settings=None, things=None):
        """
        @param: name; string; the name of the cluster
        @param: type; string; the type of the cluster (THING, SETTING, CHARACTER)
        @param: characters; [Character]; a list of related characters
        @param: settings; [Setting]; a list of related settings
        @param: things; [Thing]; a list of related things
        """
        self.name = name
        self.type = type

        self.characters = characters
        self.settings = settings
        self.things = things
        self.start_setting = None


