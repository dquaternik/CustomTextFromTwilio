def parse(rawphone):
    import re

    #Remove any parentheses
    fixed_phone = "+1" + re.sub("[^\d]+", "", rawphone)

    return fixed_phone