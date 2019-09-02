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
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    progress = params['progress']
    current_point = [params["x"], params["y"]]
    local_testing = "LOCAL_TESTING" in os.environ

    # Initialize the reward with typical value 
    reward = 1.0

    waypoint_count = len(waypoints)
    remaining_waypoint_count = waypoint_count - closest_waypoints[0]

    print("waypoint_count: {}".format(waypoint_count))
    print("remaining_waypoint_count: {}".format(remaining_waypoint_count))

    track_direction = 0.0
    direction_diff = 10000.0
    waypoint_selected = -1

    prev_point = waypoints[closest_waypoints[0]]

    for x in range(closest_waypoints[0], waypoint_count):

        if x == waypoint_count:
            break

        next_point = waypoints[x]

        # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
        loop_track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) 
        # Convert to degree
        loop_track_direction = math.degrees(loop_track_direction)

        # Calculate the difference between the track direction and the heading direction of the car
        loop_direction_diff = abs(loop_track_direction - heading)
        if loop_direction_diff > 180:
            loop_direction_diff = 360 - loop_direction_diff

        loop_distance = math.hypot(next_point[0] - current_point[0], next_point[1] - current_point[1])
        
        if local_testing:
            print("[waypoint_{}] distance: {} track_direction: {} direction_diff: {}".format(x, loop_distance, loop_track_direction, loop_direction_diff))

        if loop_direction_diff < direction_diff:
            direction_diff = loop_direction_diff
            track_direction = track_direction 
            waypoint_selected = x

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    # Penalize car for going slower 
    max_speed = 8.0
    speed_marker_2 = 0.25 * max_speed
    speed_marker_3 = 0.5 * max_speed
    
    speed = params['speed']
    if speed <= speed_marker_2:
        reward *= .8
    elif speed <= speed_marker_3:
        reward *= .5
        
    if progress == 100:    
        reward += 100

    x = {} 
    if not local_testing:
        x = copy.deepcopy(params)


    x["direction_diff"] = direction_diff
    x["track_direction"] = track_direction
    x["reward"] = reward
    x["waypoint_selected"] = waypoint_selected
        
    print(json.dumps(x))

    return reward