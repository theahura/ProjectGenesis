"""
@date 5-14-16

Description: Subsection defines relations that make up the core acts of a story
"""

class Subsection(Relation):

    def __init__(self):
        super()

    
    def initialize_relation_from_outline(self, relation_outline, protag, current_setting):
        """
        Takes a string relation_outline and converts it into a relation class based on the params
        laid out in the outline string. 

        relation_outline: string in the form cluster1type1 relationterm clustertype2, e.g. 
        Character in Setting, Character has Object, etc.
        """
        relation_components = relation_outline.split(" ")
        set_first(self.protag)
        set_relation(relation_components[1])
        
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

        set_third(third_component)


