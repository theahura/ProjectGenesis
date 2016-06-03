"""
@author: Amol Kapoor
@date: 5-25-16

Description: Contains the class structure for the thing class. Sets out params for actions and how characters relate to those actions.
"""

import random

from source.Author.Clusters.Cluster import Cluster

class Thing(Cluster):

    def __init__(self, name, characters=None, settings=None, things=None, descriptors=None, container=None, thing_actions=None):
        """
        See super for init param definition.

        @param: container; Cluster type Setting or Character; what is holding this thing
        @param: thing_actions; [Word]; a list of verbs 
        """
        super(Character, self).__init__(name, "CHARACTER", characters, settings, things, descriptors)

        self.thing_actions = thing_actions

        self.container = container if container else random.choice(settings + characters)

        if not self.container or self.container.type == "SETTING":
            raise TypeError("Container must be of type character or setting")

