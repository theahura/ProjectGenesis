"""
@date: 5-13-16

Description: Creates a basic outline of a plot based on a theme file
"""

import random
#import relation

class ThematicPlot:
    
    def __init__(self, settings, conflict):

        self.start_setting = random.choice(settings)
        self.current_setting = self.start_setting

        #gets a random character from possible setting characters as protagonist
        self.protag = random.choice(self.start_setting.characters)

        #selects as antagonist a random character that either the protagonist knows or is related
        #to the setting
        antaglist = list(set(self.protag.related_characters).union(self.start_setting.characters))
        self.antagonist = random.choice(antaglist)

        #lays out the basic story relations
        for relation_outline in conflict.relation_outlines: 
            self.relation_order.push(initialize_relations(relation_outline))

        generate_plot()

    def initialize_relations(self, relation_outline)
        """
        Takes a string relation_outline and converts it into a relation class based on the params
        laid out in the outline string. 
        """
        pass

    def generate_plot()
        """
        Iterates over relations from conflict_beginning to conflict_resolution to conflict_ending
        At each step, it decides relationships for the protag and antag characters until the next
        predefined overarching relation is met. At each step it decides whether or not to discard
        the current new relation based on how many relations have already occurred since not 
        last hitting a major relation.
        """
        pass


    def generate_next_setting(self):
        self.current_setting = random.choice(self.current_setting.nearby_settings)
        


if __name__ == "__main__":
    plotgen = new ThematicPlot()


