"""
@author: Amol Kapoor
@date: 5-25-16

Description: Contains the class structure for the setting class. Sets out params for environmental actions and structures for 
object/character location
"""

from source.Author.Clusters.Cluster import Cluster

class Setting(Cluster):

    def __init__(self, name, characters=None, settings=None, things=None):
        """
        See super for init param definition.
        """
        super(Character, self).__init__(name, "CHARACTER", characters, settings, things)



