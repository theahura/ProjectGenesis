"""
@author Amol Kapoor
@date 5-22-16

Description: Takes a storystructure and initializes a basic plot from an attached conflict
"""

from source.Author.Modules.Module import Module


class BasicPlotGen(Module):

    def __init__(self, storystruct):
        storystruct.setdetails(generate_plot())

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

    def generate_generic_relation(self, protag, setting):
        """
        Creates an undefined relation between the protagonist and a thing or character
        """
        cluster2_list = list(set().union(setting.characters, setting.things, protag.things))
        return GenericRelation(protag, random.choice(cluster2))

    def generate_setting_map(self, current_setting, next_setting):
        """ 
        Creates a path from current_setting to next_setting by iterating over nearby settings. 
        """
        traversed_settings = set()
        return generate_setting_map_helper(current_setting, next_setting, traversed_settings) 

    def generate_setting_map_helper(self, current_node, final_node, traversed_settings):
        """ 
        Takes current node, selects a neighbor node that hasn't already been traversed. 
        Randomly decides if it wants to stay at neighbor node or move one level back.
        Marks nodes that have been traversed in passed in dictionary.
        Dictionary stores in form {currentnode.name-nextnode.name} for uniqueness
        Continued until final_node is reached. Assumes there is a possible path.

        Note: can never return immediately to same location. Could be a problem for max dynamic
        story telling.
        """

        if current_node.name == final_node.name:
            return [current_node]
        elif: 
            possible_next_nodes = [x for x in current_node.settings if current_node.name + "-" + x.name not in traversed_settings]

            if not possible_next_nodes:
                return [current_node]
            
            next_node = random.choice(possible_next_nodes)

            return [current_node] + generate_setting_map_helper(next_node, final_node, traversed_settings)
