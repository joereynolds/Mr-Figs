import pygame
import events


class EventHandler():

    events = {
        28 : events.animate_bombs,
        29 : events.animate_particles
    }


    def __init__(self, player):
        """
        @self.events : An array of our custom events        
        """
        self.player = player
        self.events = [] 
        self.add_event('laser_anim', 27, 2000)
        self.add_event('bomb_anim', 28, 500)
        self.add_event('particle_anim', 29, 100)
        self.set_timers()

    def add_event(self, event_name, event_id, time):
        """Adds an event to the events array"""
        if event_id > 25:
            _event_id = event_id #
        else: 
            print('Event Ids must be greater than 25')
        _time = time
        event = (event_name, event_id, _time)
        self.events.append(event) 

    def set_timers(self):
        """Adds all of the events in our events queue to pygames event queue"""
        for event in self.events:
            pygame.time.set_timer(event[1],event[2])

    def handle_events(self, event):
        """Looks at the events coming through the event queue
        and if it's on that is in our events dictionary. It calls
        that events action"""
        for event_id, action in EventHandler.events.items():
            if event.type == event_id:
                EventHandler.events[event_id](self.player)
