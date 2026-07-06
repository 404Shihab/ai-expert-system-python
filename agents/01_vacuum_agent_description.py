# Vacuum Cleaning Agent with Locations A and B


# 1. Agent Description

# The aim of the agent is to keep both locations (A and B)
# clean by sensing the environment and performing the
# appropriate action.


# 2. Sensors
# The agent uses two sensors:
#   - Location
#   - Status


# 3. Sensor Values

# Location -> {A, B}
# Status   -> {Dirty, Clean}


# 4. Actions

# The agent can perform the following actions:
#   - Suck
#   - Right
#   - Left

# 5. Agent Function (Perception -> Action)

#
# [A, Clean]  -> Right
# [A, Dirty]  -> Suck
# [B, Clean]  -> Left
# [B, Dirty]  -> Suck
#


print("Vacuum Cleaning Agent")
print("-" * 35)

print("\nAgent Description:")
print("The aim of the agent is to clean both locations (A and B).")

print("\nSensors:")
print("1. Location")
print("2. Status")

print("\nSensor Values:")
print("Location -> {A, B}")
print("Status   -> {Dirty, Clean}")

print("\nPossible Actions:")
print("1. Suck")
print("2. Right")
print("3. Left")

print("\nAgent Function:")
print("[A, Clean]  -> Right")
print("[A, Dirty]  -> Suck")
print("[B, Clean]  -> Left")
print("[B, Dirty]  -> Suck")