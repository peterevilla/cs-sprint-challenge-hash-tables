#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    route = [None] * length    #Create route list 
    dictionary = {}  # a hash table to store flights to easy access

    for ticket in tickets:
        dictionary[ticket.source] = ticket.destination

    next_destination = dictionary["NONE"]  # First Flight is where source is NONE, start point

    for i in range(0, length):
        route[i] = next_destination
        next_destination = dictionary[next_destination]

    return route
