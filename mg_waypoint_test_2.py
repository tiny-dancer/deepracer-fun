def reward_function(params):
    ###############################################################################
    '''
    Emphasizing speed and optimal based on evaluating all upcoming waypoints 
    '''

    import math
    import copy
    import json
    import os
    import time

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

    optimal_track_direction = 0.0
    distance = 0
    optimal_direction_diff = 10000.0
    optimal_waypoint_selected = -1
    optimal_waypoint_distance = -1
    DIRECTION_THRESHOLD = 10.0

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) 
    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    for x in range(closest_waypoints[0], waypoint_count):

        if x == waypoint_count:
            break

        loop_next_point = waypoints[x]

        # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
        loop_track_direction = math.atan2(loop_next_point[1] - prev_point[1], loop_next_point[0] - prev_point[0]) 
        # Convert to degree
        loop_track_direction = math.degrees(loop_track_direction)

        # Calculate the difference between the track direction and the heading direction of the car
        loop_direction_diff = abs(loop_track_direction - heading)
        if loop_direction_diff > 180:
            loop_direction_diff = 360 - loop_direction_diff

        loop_distance = math.hypot(next_point[0] - current_point[0], next_point[1] - current_point[1])
        
        if local_testing:
            print("[waypoint_{}] distance: {} track_direction: {} direction_diff: {}".format(x, loop_distance, loop_track_direction, loop_direction_diff))

        if loop_direction_diff < DIRECTION_THRESHOLD:
            if loop_distance > distance:
                optimal_direction_diff = loop_direction_diff
                optimal_track_direction = track_direction 
                optimal_waypoint_selected = x
                optimal_waypoint_distance = loop_distance

    # Penalize the reward if the difference is below optimal
    if direction_diff > optimal_direction_diff:
        reward = 0

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
    x["optimal_direction_diff"] = optimal_direction_diff
    x["optimal_track_direction"] = optimal_track_direction
    x["optimal_waypoint_distance"] = optimal_waypoint_distance
    x["optimal_waypoint_selected"] = optimal_waypoint_selected
    x["track_direction"] = track_direction
    x["reward"] = reward
    x["model"] = "mg-optimal-waypoint1"
    x["unixTimestamp"] = time.time()
        
    print(json.dumps(x))

    return reward