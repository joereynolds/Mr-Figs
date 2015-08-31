import pygame
class EventHandler():

    def __init__(self):
        """
        @self.events : An array of our custom events        
        """
        self.events = [] 
        self.add_event('laser_anim', 27, 2000)
        self.add_event('bomb_anim', 28, 500)
        self.add_event('particle_anim', 29, 100)
        self.handle_events()

    def add_event(self, event_name, event_id, time):
        """Adds an event to the events array"""
        if event_id > 25:
            _event_id = event_id #
        else: 
            print('Event Ids must be greater than 25')
        _time = time
        event = (event_name, event_id, _time)
        self.events.append(event) 

    def handle_events(self):
        """Adds all of the events in our events queue to pygames event queue"""
        for event in self.events:
            pygame.time.set_timer(event[1],event[2])
