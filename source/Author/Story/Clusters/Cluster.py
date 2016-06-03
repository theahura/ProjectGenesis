"""
@author: Amol Kapoor
@date: 5-13-16

Description: Defines the cluster parent class
"""


class Cluster: 
    """Defines the cluster parent class, which contains basic methods common to
    all character, setting, thing clusters"""
    
    def __init__(self, name, type, characters=None, settings=None, things=None, descriptors=None):
        """
        @param: name; string; the name of the cluster
        @param: type; string; the type of the cluster (THING, SETTING, CHARACTER)
        @param: characters; {Relation <character>}; a set of related characters
        @param: settings; {Relations <settings>}; a set of related settings
        @param: things; {Relations <things>}; a set of related things
        @param: descriptors; {String}; a set of words that describe this object (adj)
        """
        self.name = name
        self.type = type

        self.characters = characters
        self.settings = settings
        self.things = things
        self.start_setting = None

        for(descriptor in descriptors):
            if(descriptor.type != 'adj'):
                raise TypeError(descriptors must be adjectives)

        self.descriptors = descriptors 

     
