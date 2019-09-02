def reward_function(params):
    ###############################################################################
    '''
    Emphasizing speed and optimal based on evaluating all upcoming waypoints 
    '''

    import copy
    import json
    import os

    # Read input variables
    progress = params['progress']
    local_testing = "LOCAL_TESTING" in os.environ

    # Initialize the reward with typical value 
    reward = 1.0

    if progress == 100:    
        reward *= 10000
    elif progress >= 90:
        reward *= progress
    elif progress >= 80:
        reward *= progress * .1
    elif progress < 80:
        reward *= progress * .01

    x = {} 
    if not local_testing:
        x = copy.deepcopy(params)
    
    x["reward"] = reward
        
    print(json.dumps(x))

    return reward