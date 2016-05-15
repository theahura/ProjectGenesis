"""
@date: 5-13-16

Description: Creates a basic outline of a plot based on a theme file
"""

import random
from source.Author.Relation import Subsection

class ThematicPlot:
    
    def __init__(self, settings, conflict):

        self.start_setting = random.choice(settings)
        self.current_setting = self.start_setting

        #gets a random character from possible setting characters as protagonist
        self.protag = random.choice(self.start_setting.characters)

        #selects as antagonist a random character that either the protagonist knows or is related
        #to the setting
        antaglist = list(set(self.protag.characters).union(self.start_setting.characters))
        self.antag = random.choice(antaglist)

        self.antagonist.set_protagonist(self.protag)
        self.protagonist.set_antagonist(self.antag)

        #lays out the basic story relations
        for relation_outline in conflict.conflict_outline: 
            subsection = Subsection() 
            subsection.init_from_outline(relation_outline, self.protag, self.current_setting)
            self.subsections.push(subsection)

        generate_plot() 

    def generate_plot():
        """
        Iterates over relations from conflict_beginning to conflict_resolution to conflict_ending
        At each step, it decides relationships for the protag and antag characters until the next
        predefined overarching relation is met. At each step it decides whether or not to discard
        the current new relation based on how many relations have already occurred since not 
        last hitting a major relation.
        """
        pass

    def generate_next_setting(self):
        self.current_setting = random.choice(self.current_setting.settings)
        
