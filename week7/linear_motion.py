def calc_free_fall_height(time, gravity = 9.8):
    """
    Calculates the height fallen by an object 
    under the principles of linear motion

    Args:
        time (_type_): time in seconds for object to reach the ground
        gravity (float, optional): the value of gravity on earth. 
        Defaults to 9.8.

    Returns:
        _type_: height an object fell to reach its destination in metres.
    """    
    # Linear motion calculation
    height_fallen = ((1 / 2) * gravity) * (time * time)

    # returns height fallen in metres
    return height_fallen

# calling the calc_free_fall_method with 3.375
# for testing to esnure correct working.
height_fallen = calc_free_fall_height(3.375)
