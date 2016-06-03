"""
@author: Amol Kapoor
@date: 5-25-16

Description: Contains the class structure for the character class. Defines character behaviors, and sets out parameters for character 
relations to things (in specific, how the things available affect possible actions)
"""

import random

from source.Author.Clusters.Cluster import Cluster

class Character(Cluster):

    def __init__(self, name, characters=None, settings=None, things=None, setting_container=None, held_things=None, descriptors=None):
        """
        See super for init param definitions not listed here.

        @param: setting_container; Setting; the setting that the character is in
        @param: held_things; {Things}; a list of things that the character is holding
        """
        super(Character, self).__init__(name, "CHARACTER", characters, settings, things, descriptors)

        self.setting_container = setting_container if setting_container else random.choice(settings)

        if not self.setting_container:
            raise NameError('No setting container found')

        self.held_things = held_things

        self.character_actions = self.define_character_actions(self.descriptions)

    def hold_thing(self, thing):
        """
        Adds the thing to the character set of held things, 
        and modifies the possible actions available to the character

        @param: thing; Thing; what the character picks up
        """
        self.character_actions.update(thing.thing_actions)
        self.held_things.add(thing)

    def drop_thing(self, thing):
        """
        Drops the thing from the set of held things and modifies available actions.

        @param: thing; Thing; what to drop
        """
        self.held_things.remove(thing)
        self.character_actions.difference_update(thing.thing_actions)

    def move_to_new_setting(self, setting):
        """
        Moves the character to a new place and modifies the container/setting contains

        @param: setting; Setting; where the character is moving to
        """
        self.setting_container = setting
        setting.add_cluster_to_contains(self)
       

    def define_character_actions(descriptors):
        """
        Returns a set of verbs based on describing features.

        @param: descriptors; [Word] of type adj; what to base possible character actions off of
        """
        actions_list = []
        for(adj in descriptors)
            for(verb in adj.verbs)
                actions_list.append(verb)

        return actions_list
