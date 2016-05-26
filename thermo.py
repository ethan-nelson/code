sigma = 5.670373E-8


def emissivity(albedo):
    """ Calculates the emissivity given a reflectance or albedo.

    >>> emissivity(0.3)
    0.7
    """
    emissivity = 1.0 - albedo

    return emissivity


def radiance(temperature, *emissivity):
    """ Calculates the total radiance according to the Stefan-Boltzmann law.

    Notes
    -----

    The Stefan-Boltzmann Law dictates the radiance of an object given its
    temperature and optionally emissivity.

    F = sigma * T ** 4

    or

    F = epsilon * sigma * T ** 4

    >>> radiance(5600, 0.3)
    16729578.176102402

    """
    if emissivity:
        radiance = emissivity[0] * sigma * temperature ** 4.0
    else:
        radiance = sigma * temperature ** 4.0

    return radiance


def temperature(radiance, *emissivity):
    """ Calculates the temperature according to the Stefan-Boltzmann law.
    
    Notes
    -----

    The Stefan-Boltzmann Law dictates the temperature of a body given a
    radiance and optionally emissivity.

    F = sigma * T ** 4 => T = (F / sigma) ** 1/4

    or

    F = epsilon * sigma * T ** 4 => T = (F / epsilon / sigma) ** 1/4

    >>> temperature(1.67E7, 0.3)
    5597.523133627065

    """
    if emissivity:
        temperature = (radiance / emissivity[0] / sigma) ** 0.25
    else:
        temperature = (radiance / sigma) ** 0.25

    return temperature


def effective_temperature(insolation, albedo, *emissivity):
    """ Calculates the effective temperature according to radiative balance.

    Notes
    -----

    Insolation intercepts the surface. An initial amount of the insolation,
    albedo, is immediately reflected; 1 - albedo is absorbed by the surface.
    Assuming the surface has a perfect emissivity at its emitting temperature,
    the emission is sigma * temperature to the fourth.

    S * (1 - alpha) = sigma * T ** 4

    If the surface does not perfectly emit, then the emitted radiation is
    scaled by that fraction.

    S * (1 - alpha) = epsilon * sigma * T ** 4

    >>> effective_temperature(1367.0, 0.3, 0.95)
    365.0756190774243

    """
    if emissivity:
        temperature = (insolation * (1.0 - albedo) / emissivity [0] / sigma) ** 0.25
    else:
        temperature = (insolation * (1.0 - albedo) / sigma) ** 0.25

    return temperature


def heat_transfer(transfer_coefficient, albedos, recipient):
    """Calculates the relative transfer of heat within the surface environment.

    >>> heat_transfer(25.175, {'surface': 0.5, 'test': 0.25}, 'test')
    6.29375
    """

    heat = transfer_coefficient * (albedos['surface'] - albedos[recipient])

    return heat
