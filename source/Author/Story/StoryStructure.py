"""
@date: 5-13-16

Description: Creates a basic outline of a plot based on a theme file.

Expects a fully fleshed out 'world' in which each cluster is an object with its own description
and its own relations to settings/characters/things. 
"""

import random
from source.Author.Relation import Subsection
from source.Author.Relation import GenericRelation


class StoryStructure:

    def __init__(self, settings, conflict):
        """
        Selects a random setting from the list of given settings and uses the conflict to create
        the basic setup for a story. 

        @param: settings; [Setting]; a list of all possible settings, already initialized and related to each other
        @param: conflict; Conflict; a conflict class detailing the story being followed
        """
        #generates the initial setting
        self.start_setting = random.choice(settings)
        self.current_setting = self.start_setting

        #gets a random character from possible setting characters as protagonist
        self.protag = random.choice(self.start_setting.characters)

        #selects as antagonist a random character that either the protagonist knows or is related
        #to the setting
        antaglist = list(set(self.protag.characters).union(self.start_setting.characters))
        self.antag = random.choice(antaglist)

        self.antag.set_protagonist(self.protag)
        self.protag.set_antagonist(self.antag)

        #lays out the basic story relations
        self.subsections = []

        for relation_outline in conflict.conflict_outline: 
            subsection = Subsection() 
            subsection.init_from_outline(relation_outline, self.protag, self.current_setting)
            self.subsections.push(subsection)

        #connects the rest of the story together
        self.details = [] 

    def set_details(details_list):
        self.details = details_list
