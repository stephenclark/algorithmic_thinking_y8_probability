from numpy import random
import numpy as np
import time

number_of_simulations=10000  # <-- change this number to change the number of simulations  

def monty_hall_simulation (number_of_simulations):
    choice_unchanged=[]
    choice_changed=[]
    NN=1
    for i in range(0,number_of_simulations):
        
        # 1) The car is placed behind a random door.
        winning_door=random.choice(['Door 1', 'Door 2', 'Door 3'])

        # 2) The contestant selects a random door.
        first_selection=random.choice(['Door 1', 'Door 2', 'Door 3'])
        
        # 3) The host opens a door that is different than the contestants choice 
        #    and not the door with the car.
        host_opens=list(set(['Door 1', 'Door 2', 'Door 3'])-set([first_selection,winning_door]))[0]
        
        # 4) The other door is not the participant's selected door and not the opened door. 
        other_door=list(set(['Door 1', 'Door 2', 'Door 3'])-set([first_selection,host_opens]))[0]
        
        # 5) Add "True" to a list where the participant DOES NOT change their selection AND their 
        #    selection identified the door with the car. 
        choice_unchanged.append(first_selection==winning_door)
        
        # 6) Add "True" to a list where the participant DOES change their selection and their 
        #    new selected door has the car behind it.
        choice_changed.append(other_door==winning_door)
        
    # NOTE: The boolean object "TRUE" is equal to 1 and "False" is equal to 0.
    #       As such, we can use the "sum" function to get the total number of wins
    #       for each strategy.
    print(f'\n\
    {number_of_simulations:,} games were played \n\
    Chances of winning the car based on the following strategies:\n\
    Remaining with initial selection: {"{:.1%}".format(sum(choice_unchanged)/float(number_of_simulations))}\n\
    Switching doors: {"{:.1%}".format(sum(choice_changed)/float(number_of_simulations))}')
            
###############################            
###### Run the Simulation######
###############################
start_time = time.time()
monty_hall_simulation(number_of_simulations)       
print(f'\nSimulation Completed in: {round(time.time()-start_time,2)} Seconds')
