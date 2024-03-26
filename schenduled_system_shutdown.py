import os
import time

def shutdown():
    """Shut down the computer."""
    os.system("shutdown /s /t 1")

# Ask the user to input the shutdown time in minutes
set_time = input("Shutdown After (minutes): ")
set_time = int(set_time)

# Convert minutes to seconds
sec = 60

# Display a message about the shutdown time
print('Computer Will Now Shutdown in ' + str(set_time) + ' Minutes')

# Wait for the specified time
time.sleep(set_time * sec)

# Print a message before shutting down
print('\n')
print('Computer Will Now Shutdown!')

# Wait for 3 seconds before initiating shutdown
time.sleep(3)
shutdown()
