"""
@date: 5-13-16

Description: Creates a basic outline of a plot based on a theme file.

Expects a fully fleshed out 'world' in which each cluster is an object with its own description
and its own relations to settings/characters/things. 
"""

import random
from source.Author.Relation import Subsection

class StoryStructure:
    
    def __init__(self, settings, conflict):
        """
        Selects a random setting from the list of given settings and uses the conflict to create
        the basic setup for a story. 
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
        self.details = generate_plot() 

    def generate_plot(self):
        """
        Iterates over relations from conflict.
        At each step, it decides relationships for the protag until the next
        predefined overarching relation is met.         
        """

        detail_list = []

        #for each subsection
        for i, subsection in enumerate(self.subsections):

            detail_list.push(subsection)

            nextsub = self.subsections[i+1]

            #figure out how to get from current setting to the setting for the next subsection
            setting_path = generate_setting_map(self.current_setting, nextsub.get_setting())

            #in each of these settings, generate some random number of relations from 0 to 10
            for setting in setting_path:
                for i in range(random.randint(0, 10)):
                    detail_list.push(generate_generic_relation(self.protag, setting))

        return detail_list

    def generate_generic_relation(protag, setting):
        cluster2_list = list(set().union(setting.characters, setting.things, protag.things))
        return GenericRelation(protag, random.choice(cluster2))

    def generate_setting_map(self, current_setting, next_setting):
        """ 
        Creates a path from current_setting to next_setting by iterating over nearby settings. 
        Implement some search algo here.
        """
        pass


