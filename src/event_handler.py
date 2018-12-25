"""
Contains our EventHandler class which is used to handle all
events in the event queue

...By the way, putting this docstring in made my code
10/10 from the linter...ho yeah
"""


import pygame
import events
import logger

class EventHandler(object):
    """Handles the setting up, addition, and timing
    of custom events. each event has 3 things associated with it,
    friendly name = A human readable version of the event
    event id = the id of the event
    timer = How often the event should be triggered (in ms)"""

    events_map = {
        28 : events.call_bomb_events,
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
            _time = time
            event = (event_name, event_id, _time)
            self.events.append(event)
        else:
            logger.LOGGER.info('Event Ids must be greater than 25')

    def set_timers(self):
        """Adds all of the events in our events queue to pygames event queue"""
        for event in self.events:
            pygame.time.set_timer(event[1], event[2])

    def handle_events(self, event):
        """Looks at the events coming through the event queue
        and if it's on that is in our events dictionary. It calls
        that events action"""
        for event_id in EventHandler.events_map.keys():
            if event.type == event_id:
                EventHandler.events_map[event_id](self.player)
