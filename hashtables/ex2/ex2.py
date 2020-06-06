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

    # Hash Tickets
    hashtable = {}

    for ticket in tickets:
        hashtable[ticket.source]=ticket.destination
    
    # Add Origin ticket
    route.append(hashtable["NONE"])

    # Add ticket to route according to value of last ticket
    for ticket in hashtable:
        if ticket == "NONE":
            continue
        route.append(hashtable[route[-1]])   
    return route