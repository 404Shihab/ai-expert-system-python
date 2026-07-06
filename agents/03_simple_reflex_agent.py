# Simple Reflex Agent

# Agent Description
# --------------------
# A Simple Reflex Agent selects an action based only on
# the current percept.
#
# It does not remember previous states or maintain
# any internal model.
#
# Perception -> Action
# --------------------
# (A, Dirty) -> Suck
# (A, Clean) -> Right
# (B, Dirty) -> Suck
# (B, Clean) -> Left



import random

def simple_reflex_agent(percept):

    print('Perception Received: ' + str(percept))

    location = percept[0]
    status = percept[1]

    # If the current location is dirty, clean it
    if status == 'Dirty':
        action = 'Suck'

    # If location A is clean, move to B
    elif location == 'A':
        action = 'Right'

    # If location B is clean, move to A
    elif location == 'B':
        action = 'Left'

    return action


# Initialize Environment

Location = random.choice(['A', 'B'])
Condition = random.choice(['Clean', 'Dirty'])

# Agent Simulation


while True:

    # Agent perceives the environment
    action = simple_reflex_agent((Location, Condition))

    # Agent performs an action
    print('Action Performed: ' + action)

    # Ask whether to continue
    cmd = input('Get Perception (yes/no): ')

    if(cmd == 'no' or cmd != 'yes'):
        break

    # Update the environment based on the action
    if action == 'Right':
        Location = 'B'
        Condition = random.choice(['Clean', 'Dirty'])

    elif action == 'Left':
        Location = 'A'
        Condition = random.choice(['Clean', 'Dirty'])

    else:
        Condition = 'Clean'