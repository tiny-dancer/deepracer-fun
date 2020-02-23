def reward_function(params):
    ###############################################################################
    '''
    Emphasizing speed and optimal based on evaluating all upcoming waypoints 
    '''

    import math
    import copy
    import json
    import os

    # Read input variables
    progress = params['progress']
    local_testing = "LOCAL_TESTING" in os.environ

    # Initialize the reward with typical value 

    reward = (progress/100)**.4

    x = {} 
    if not local_testing:
        x = copy.deepcopy(params)

    x["progress"] = progress 
    x["reward"] = reward
        
    print(json.dumps(x))

    return reward