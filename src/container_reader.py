import pygame
import gui_base
import xml.etree.ElementTree as etree 


class ContainerReader():

    def __init__(self, xml_file):

        #maybe create a config file for all of these
        #various paths to go into?
        self.xml_file = 'scenes\layouts\\' + xml_file
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
        component_objects = pygame.sprite.Group()
        component_dict = {}
        for component in self.xml_components:
            obj_component = eval(component.attrib['type'])(
                int(component.attrib['x']),
                int(component.attrib['y']),
                int(component.attrib['width']),
                int(component.attrib['height'])
            )
            component_dict[component.attrib['name']] = obj_component
            component_objects.add(obj_component)
        component_dict['components'] = component_objects
        return component_dict
