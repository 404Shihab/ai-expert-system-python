# Model Based Reflex Agent



# Agent Description
# ------------------
# A Model Based Reflex Agent maintains an internal model
# of the environment.
#
# Unlike a Simple Reflex Agent, it remembers previous
# observations and uses them to determine the world's state.
#
# World State:
#   Good -> Both rooms are clean
#   Bad  -> At least one room is dirty



import random

# Initial Model


# Initially, the agent does not know the condition
# of either location.

model = {
    'A': 'Unknown',
    'B': 'Unknown'
}

world_state = 'Bad'
action = 'Unknown'


# Update the Internal Model


def update_state(action, percept, model):

    location = percept[0]
    status = percept[1]

    # Update the model using the current perception
    model[location] = status

    global world_state

    # If the current location was cleaned,
    # update the model accordingly.
    if action == 'Suck':
        model[location] = 'Clean'

    # Check whether both locations are clean
    if model['A'] == 'Clean' and model['B'] == 'Clean':
        world_state = 'Good'
    else:
        world_state = 'Bad'

    return world_state

#Model Based Reflex Agent


def model_based_reflex_agent(percept):

    location = percept[0]
    status = percept[1]

    global world_state, action, model

    # Stop when the world becomes clean
    if world_state == 'Good':
        action = 'Pause'
        return action

    # Decide the next action
    elif status == 'Dirty':
        action = 'Suck'

    elif location == 'A':
        action = 'Right'

    elif location == 'B':
        action = 'Left'

    # Update the internal model
    world_state = update_state(action, percept, model)

    print("Perception: " + str(percept))
    print("Action Performed: " + action)
    print("Model: " + str(model))
    print("State: " + str(world_state))

    return action


# Initialize Environment

Location = random.choice(['A', 'B'])
Condition = random.choice(['Clean', 'Dirty'])

# Agent Simulation

while True:

    print("*****")

    action = model_based_reflex_agent((Location, Condition))

    if action == 'Right':
        Location = 'B'
        Condition = random.choice(['Clean', 'Dirty'])

    elif action == 'Left':
        Location = 'A'
        Condition = random.choice(['Clean', 'Dirty'])

    elif action == 'Suck':
        Condition = 'Clean'

    elif action == 'Pause':

        cmd = input("Stopped. Do restart? (yes/no): ")

        if(cmd == 'no' or cmd != 'yes'):
            break

        # Reinitialize the environment
        Location = random.choice(['A', 'B'])
        Condition = random.choice(['Clean', 'Dirty'])

        # Reset the model
        model = {
            'A': 'Unknown',
            'B': 'Unknown'
        }

        world_state = 'Bad'
        action = 'Unknown'