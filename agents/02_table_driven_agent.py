# Table Driven Agent


# Agent Description

# A Table Driven Agent stores all possible percept-action pairs
# in a lookup table. When a percept is received, the agent
# searches the table and performs the corresponding action.
#
# Perception -> Action
# --------------------
# (A, Clean)  -> Right
# (A, Dirty)  -> Suck
# (B, Clean)  -> Left
# (B, Dirty)  -> Suck



import random

table = {
    ('A', 'Clean'): 'Right',
    ('A', 'Dirty'): 'Suck',
    ('B', 'Clean'): 'Left',
    ('B', 'Dirty'): 'Suck'
}


# Stores the history of all perceptions
percepts = []



#Agent Function

def table_driven_agent(percept):

    print('Perception Received: ' + str(percept))

    # Update percept history
    percepts.append(percept)

    # Search the table for the corresponding action
    action = lookup(percept, table)

    return action


#Lookup Function

def lookup(p, t):
    return t[p]


# Initialize Environment


Location = random.choice(['A', 'B'])
Condition = random.choice(['Clean', 'Dirty'])


# Agent Simulation


while True:
    action = table_driven_agent((Location, Condition))
    print('Action Performed: ' + action)
    # Ask whether to continue
    cmd = input('Get Perception (yes/no): ')
    if cmd != 'yes':
        break
    # Update environment according to the action
    if action == 'Right':
        Location = 'B'
        Condition = random.choice(['Clean', 'Dirty'])

    elif action == 'Left':
        Location = 'A'
        Condition = random.choice(['Clean', 'Dirty'])

    else:
        Condition = 'Clean'