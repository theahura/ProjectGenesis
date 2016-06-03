"""
@author: Amol Kapoor
@date: 5-25-16

Description: Contains the class structure for the setting class. Sets out params for environmental actions and structures for 
object/character location
"""

from source.Author.Clusters.Cluster import Cluster

class Setting(Cluster):

    def __init__(self, name, characters=None, settings=None, things=None, descriptors=None):
        """
        See super for init param definition if not listed.
        """
        super(Character, self).__init__(name, "SETTING", characters, settings, things, descriptors)

        self.contains = things

    def add_cluster_to_contains(cluster):
        if cluster.type == 'SETTING':
            raise TypeError('Setting cannot contain a setting')

        self.contains.add(cluster)
