import numpy as np

iterations = 10000
stay = False
n_doors = 3

wins = 0.0

for i in range(iterations):
    # place car in random position
    car_position = np.random.randint(n_doors)
    # contestant's door choice
    choice = np.random.randint(n_doors)
    
    # status of door:
    # 0 = closed
    # 1 = open
    # 2 = chosen
    status = np.zeros(n_doors)
    status[choice] = 2
    
    final_choice = choice
    
    # shuffle door order to prevent choice bias
    rand_arr = np.arange(n_doors)
    np.random.shuffle(rand_arr)
    
    # open each door that is not the chosen door or the door with the car
    for j in range(n_doors):
        if rand_arr[j] != choice and rand_arr[j] != car_position:
            status[rand_arr[j]] = 1
            
    if stay == False:
        closed_door = np.where(status == 0)
        final_choice = closed_door[0]
    

    if final_choice == car_position:
        wins = wins + 1.0
    
print('Win percentage = ' + str(round(100 * wins/iterations)) + '%')
        
    


