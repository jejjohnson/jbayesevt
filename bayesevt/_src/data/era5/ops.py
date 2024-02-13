from typing import List, Union
from bayesevt._src.data.era5.variables import SINGLE_LEVEL_TO_ERA5_CODE, SingleLevelCode, PressureLevelCode


def parse_single_levels(channel_names: list[str]) -> list[SingleLevelCode]:
    """
    Parses a list of channel names and returns a list of corresponding SingleLevelCode objects.

    Args:
        channel_names (list[str]): A list of channel names.

    Returns:
        list[SingleLevelCode]: A list of SingleLevelCode objects corresponding to the input channel names.

    Example:
    >>> channels = ["u10m", "v10m", "z100", "u250"]
    >>> parse_single_levels(channels_)
    [SingleLevelCode(id=165, name='u10m'), 
    SingleLevelCode(id=166, name='v10m')]
    """
    # check if name in explicit names
    criteria = lambda x: x in SINGLE_LEVEL_TO_ERA5_CODE
    # filter for criteria
    sl_variables = list(filter(criteria, channel_names))
    # create single level codes
    f = lambda x: SingleLevelCode.from_name(name=x)
    # map list to codes
    return list(map(f, sl_variables))


def parse_pressure_levels(channel_names: list[str]) -> list[PressureLevelCode]:
    """
    Parses a list of channel names and returns a list of corresponding PressureLevelCode objects.

    Args:
        channel_names (list[str]): A list of channel names.

    Returns:
        list[PressureLevelCode]: A list of PressureLevelCode objects corresponding to the channel names.
    
    Example:
    >>> channels = ["u10m", "v10m", "z100", "u250"]
    >>> parse_pressure_levels(channels_)
    [SingleLevelCode(id=165, name='u10m'), SingleLevelCode(id=166, name='v10m')]
    [PressureLevelCode(id=129, level=100, name='z'),
    PressureLevelCode(id=131, level=250, name='u')]
    """
    # check if name in explicit names
    criteria = lambda x: x not in SINGLE_LEVEL_TO_ERA5_CODE
    # filter for criteria
    pl_variables = list(filter(criteria, channel_names))
    # create pressure level codes
    f = lambda x: PressureLevelCode.from_name(name=x)
    # map list to codes
    return list(map(f, pl_variables))


def parse_all_variables(channel_names: list[str]) -> List[Union[SingleLevelCode, PressureLevelCode]]:
    """
    Parses all variables from the given channel names.

    Args:
        channel_names (list[str]): A list of channel names.

    Returns:
        List[Union[SingleLevelCode, PressureLevelCode]]: A list of parsed variables.

    Raises:
        AssertionError: If the length of the parsed variables is not equal to the length of the channel names.
    
    Example:
    >>> channels = ["u10m", "v10m", "z100", "u250"]
    >>> parse_all_variables(channels_)
    [SingleLevelCode(id=165, name='u10m'),
    SingleLevelCode(id=166, name='v10m'),
    PressureLevelCode(id=129, level=100, name='z'),
    PressureLevelCode(id=131, level=250, name='u')]
    """
    all_vars = parse_single_levels(channel_names)
    all_vars += parse_pressure_levels(channel_names)
    assert len(all_vars) == len(channel_names)
    return all_vars

