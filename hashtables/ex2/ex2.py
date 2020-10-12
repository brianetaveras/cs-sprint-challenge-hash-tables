#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    table = {}

    for ticket in tickets:
        table[ticket.source] = ticket.destination
    
    current = "NONE"
    while table[current] != "NONE":
        route.append(table[current])
        current = table[current]
    route.append(table[current])
    return route


tickets = [
    Ticket("PIT", "ORD" ),
    Ticket("XNA", "CID" ),
    Ticket("SFO", "BHM" ),
    Ticket("FLG", "XNA" ),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO" ),
    Ticket("CID", "SLC" ),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT" ),
    Ticket("BHM", "FLG" )
]

print(reconstruct_trip(tickets, 10))