import pygame
class EventHandler():

    def __init__(self):
        self.events = [] 

    def add_event(self, event_name, event_id, time):
        if event_id > 25:
            _event_id = event_id #
        else: 
            print('Event Ids must be greater than 25')
        _time = time
        event = (event_name, event_id, _time)
        self.events.append(event) 

    def handle_events(self):
        for event in self.events:
            pygame.time.set_timer(event[1],event[2])
