"""
Contains our EventHandler class which is used to handle all
events in the event queue
"""


import pygame
import src.events as events
import src.logger as logger

class EventHandler():
    """Handles the setting up, addition, and timing
    of custom events. each event has 3 things associated with it,
    friendly name = A human readable version of the event
    event id = the id of the event
    timer = How often the event should be triggered (in ms)"""

    events_map = {
        pygame.USEREVENT: events.call_bomb_events,
        pygame.USEREVENT + 1: events.animate_particles,
        pygame.USEREVENT + 2: events.animate_lasers,
    }

    def __init__(self, level, player):
        """
        @self.events : An array of our custom events
        """
        self.level = level
        self.player = player

        self.events = [
            (pygame.USEREVENT, 500, 'bomb animation and sound effects'),
            (pygame.USEREVENT + 1, 100, 'particle animation'),
            (pygame.USEREVENT + 2, 100, 'laser animation'),
        ]

        self.set_timers()

    def set_timers(self):
        """Adds all of the events in our events queue to pygames event queue"""
        for event in self.events:
            pygame.time.set_timer(event[0], event[1])

    def handle_events(self, event):
        """Looks at the events coming through the event queue
        and if it's on that is in our events dictionary. It calls
        that events action"""
        for event_id in EventHandler.events_map.keys():
            if event.type == event_id:
                EventHandler.events_map[event_id](self.player, self.level)
