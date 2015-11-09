"""
The container reader is an XML parser for all XML
files in the /scenes/layouts directory.

It takes an xml_file and returns a pygame sprite group of
all of the components within that xml_file.

See the XML file for how to implement a new layout 
"""

import pygame
import config
import gui_base
import xml.etree.ElementTree as etree 

class ContainerReader():
    """Takes an XML file for a layout and returns
    a pygame sprite group of layered updates when you
    call get_components()"""

    def __init__(self, xml_file):
        """
        @xml_file = The xml_data for a scene(layout)
        @xml_components = An array of all <component>'s
        @self.components = A LayeredUpdates array of all component objects
        @self.component_dict = A key value pair of components where the key
        is the name of the component and the value is the component
        """

        self.xml_file = config.layout_location + xml_file
        self.tree = etree.parse(self.xml_file)
        self.root = self.tree.getroot()
        self.xml_components = self.root.find('components').findall('component')
        self.component_dict = self.get_components()
        self.components = self.component_dict['components']

    def get_components(self):
        """
        Returns a dictionary AND array of components within that dictionary.
        The dictionary's structure is as follow

        {
            'component-name' : 'component-type',
            'component-name' : 'component-type',
            'component-name' : 'component-type',
            'components' : [list of all components]
        }

        This means we can access individual components like this
            component_dict['start-game']
        Or if we just need to iterate through them, we can do this:
            [x for x in component_dict['components']]
        """
        component_objects = pygame.sprite.LayeredUpdates()

        component_dict = {}
        for component in self.xml_components:
            obj_component = eval(component.attrib['type'])(
                int(component.attrib['x']),
                int(component.attrib['y']),
                int(component.attrib['width']),
                int(component.attrib['height']),
                string=component.find('text').text
            )
            component_dict[component.attrib['name']] = obj_component
            component_objects.add(obj_component)
        component_dict['components'] = component_objects
        return component_dict
