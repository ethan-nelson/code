

def ground(albedos):
    """ Calculates the ground albedo as 1 minus the others.

    >>> ground([0.333, 0.514])
    array([ 0.153])
    """
    if len(albedos) == 1:
        ground_albedo = 1.0 -  albedos[0]
    else:
        ground_albedo = 1.0 - sum(albedos)

    return ground_albedo


def planetary(albedos, areas):
    """ Calculates the mean planetary albedo.

    >>> planetary([0.333, 0.514], [0.225, 0.714])
    array([ 0.441921])
    """
    if len(albedos) != len(areas):
        msg = 'You must specify the same number of albedos as areas.'
        raise Exception(msg)
    elif len(albedos) == 1:
        planetary_mean_albedo = albedos[0] * areas[0]
    else:
        planetary_mean_albedo = sum([albedo * area
                                    for albedo, area in zip(albedos, areas)])

    return planetary_mean_albedo
