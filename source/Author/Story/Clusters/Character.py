"""
@author: Amol Kapoor
@date: 5-25-16

Description: Contains the class structure for the character class. Defines character behaviors, and sets out parameters for character 
relations to things (in specific, how the things available affect possible actions)
"""

from source.Author.Clusters.Cluster import Cluster

class Character(Cluster):

    def __init__(self, name, characters=None, settings=None, things=None):
        """
        See super for init param definition.
        """
        super(Character, self).__init__(name, "CHARACTER", characters, settings, things)



