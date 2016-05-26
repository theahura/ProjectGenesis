"""
@author: Amol Kapoor
@date: 5-25-16

Description: Contains the class structure for the thing class. Sets out params for actions and how characters relate to those actions.
"""

from source.Author.Clusters.Cluster import Cluster

class Thing(Cluster):

    def __init__(self, name, characters=None, settings=None, things=None):
        """
        See super for init param definition.
        """
        super(Character, self).__init__(name, "CHARACTER", characters, settings, things)



