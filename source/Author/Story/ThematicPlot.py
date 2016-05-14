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
        antaglist = list(set(self.protag.characters).union(self.start_setting.characters))
        self.antag = random.choice(antaglist)

        self.antagonist.set_protagonist(self.protag)
        self.protagonist.set_antagonist(self.antag)

        #lays out the basic story relations
        for relation_outline in conflict.relation_outlines: 
            self.relation_order.push(initialize_relation_from_outline(relation_outline))

        generate_plot()

    def initialize_relation_from_outline(self, relation_outline)
        """
        Takes a string relation_outline and converts it into a relation class based on the params
        laid out in the outline string. 


        TODO: MOVE TO RELATION.PY AS AN INIT CONSTRUCTOR
        """
        relation_components = relation_outline.split(" ")
        new_relation = Relation()
        new_relation.set_first(self.protag)
        new_relation.set_relation(relation_components[1])
        
        third_component = relation_components[2]

        if third_component == 'character':
            #picks a random character from the associated characters list or the current_setting 
            #character list
            templist = self.current_setting.characters
            char_list = list(set(self.protag.characters).union(templist))
            third_component = random.choice(char_list)

        else if third_component == 'object':
            templist = self.current_setting.things
            thing_list = list(set(self.protag.things).union(templist))
            third_component = random.choice(thing_list)

        else if third_component == 'setting':
            templist = self.current_setting.settings
            setting_list = list(set(self.protag.settings).union(templist))
            third_component = random.choice(setting_list)

        new_relation.set_third(third_component)

        return new_relation

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
        self.current_setting = random.choice(self.current_setting.settings)
        


if __name__ == "__main__":
    plotgen = new ThematicPlot()


