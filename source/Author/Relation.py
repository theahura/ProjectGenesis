"""
@date: 5-14-16
Description: Relation. Defines the relation class as <cluster> <relation term> <cluster>. Acts as 
the bread and butter of the author's development.

Description: Subsection. Child of Relation. Defines relation class for subsections as Protag 
<relation term> <cluster2>, where cluster2 is related to the protag or the current setting. Used 
for major plot outlines. 
"""

class Relation:

    def __init__(self, cluster1=None, relation=None, cluster2=None):
        self.cluster1 = cluster1
        self.relation = relation
        self.cluster2 = cluster2

    def create_relation_outline(self):
        type1 = self.cluster1.type
        type2 = self.cluster2.type
        return type1 + " " + self.relation + " " + type2

    def __str__(self):
        return create_relation_outline()


class Subsection(Relation):

    def __init__(self, cluster1=None, relation=None, cluster2=None):
        super(Subsection, self).__init__(cluster1, relation, cluster2)

    def get_setting(self):
        return self.cluster2.start_setting
    
    def init_from_outline(self, relation_outline, protag, current_setting):
        """
        Takes a string relation_outline and converts it into a relation class based on the params
        laid out in the outline string. 

        relation_outline: string in the form cluster1type1 relationterm clustertype2, e.g. 
        Character in Setting, Character has Object, etc.
        """
        relation_components = relation_outline.split(" ")
        self.cluster1 = self.protag
        self.relation = relation_components[1]
        
        third_component = relation_components[2]

        if third_component == 'character':
            #picks a random character from the associated characters list or the current_setting 
            #character list
            templist = self.current_setting.characters
            char_list = list(set(self.protag.characters).union(templist))
            third_component = random.choice(char_list)

        elif third_component == 'object':
            templist = self.current_setting.things
            thing_list = list(set(self.protag.things).union(templist))
            third_component = random.choice(thing_list)

        elif third_component == 'setting':
            templist = self.current_setting.settings
            setting_list = list(set(self.protag.settings).union(templist))
            third_component = random.choice(setting_list)

        self.cluster2 = third_component

class GenericRelation(Relation):

    def __init__(self, cluster1=None, cluster2=None):
        super(GenericRelation, self).__init__(cluster1, "***", cluster2)

