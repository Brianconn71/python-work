def calc_mean(numbers):
    """
    Calculates mean of a list of numbers

    Args:
        numbers (int): list of numbers passed to function

    Returns:
        float: returns the average of the list of numbers
    """    
    length_of_list = len(numbers)
    mean = sum(numbers) / length_of_list
    return mean


def calc_median(numbers):
    """
    Calculates median of a list of numbers

    Args:
        numbers (int): list of numbers passed to function

    Returns:
        float: returns the midpoint value of a list of numbers
    """ 
    sorted_list = sorted(numbers)
    middle_num = int(len(sorted_list) / 2)
    if len(sorted_list) % 2 == 1:
        median = sorted_list[middle_num]
    else:
        median = ((sorted_list[middle_num-1] + sorted_list[middle_num])/2)
    return median


def calc_mode(numbers):
    """
    Calculates mode of a list of numbers

    Args:
        numbers (int): list of numbers passed to function

    Returns:
        int: most common occurance in numbers list
    """ 
    unique_values = sorted(set(numbers))
    times_appeared = [numbers.count(value) for value in unique_values]
    max_value = max(times_appeared)
    index_of_max = times_appeared.index(max_value)
    mode_value = unique_values[index_of_max]

    return mode_value

def calc_iqr(numbers):
    """
    Calculates interquartile range of a list of numbers

    Args:
        numbers (int): list of numbers passed to function

    Returns:
        float: returns the interquartile range in the list 
    """
    sorted_list = sorted(numbers)
    middle_num = int(len(sorted_list) / 2)
    if len(sorted_list) % 2 == 1:
        lower_half = sorted_list[:middle_num]
        upper_half = sorted_list[middle_num+1:]
    else:
        lower_half = sorted_list[:middle_num]
        upper_half = sorted_list[middle_num:]
    lower_half_median = calc_median(lower_half)
    upper_half_median = calc_median(upper_half)
    
    iqr = upper_half_median - lower_half_median
    
    return iqr
    


def calc_std_dev(numbers):
    """
    Calculates Standard dev of a list of numbers

    Args:
        numbers (int): list of numbers passed to function

    Returns:
        float: returns the standard deviation of a list of numbers
    """ 
    mean = calc_mean(numbers)
    total = 0
    for num in numbers:
        new_num = num - mean
        new_num_square = new_num * new_num
        total += new_num_square
    divide_by_length = total / (len(numbers) - 1)
    std_dev = divide_by_length ** (1/2)
    
    return std_dev


def calc_median_skewness(numbers):
    """
    Calculates the median skew of a list of numbers

    Args:
        numbers (int): list of numbers passed to function

    Returns:
        float: returns the median skew of a list of numbers
    """ 
    mean = calc_mean(numbers)
    median = calc_median(numbers)
    std_dev = calc_std_dev(numbers)
    
    median_skewness = 3 * (mean - median) / std_dev
    
    return median_skewness


def calc_mode_skewness(numbers):
    """
    Calculates mode shew of a list of numbers

    Args:
        numbers (int): list of numbers passed to function

    Returns:
        float: returns the mode skew of a list of numbers
    """ 
    mean = calc_mean(numbers)
    mode = calc_mode(numbers)
    std_dev = calc_std_dev(numbers)
    
    mode_skewness = (mean - mode) / std_dev
    
    return mode_skewness