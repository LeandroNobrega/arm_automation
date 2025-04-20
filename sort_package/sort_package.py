from .constants import VOLUME_THRESHOLD, DIMENSION_THRESHOLD, MASS_THRESHOLD, REJECTED, SPECIAL, STANDARD

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Classify the package into the correct stack
    """
    def validate_dimensions(width, height, length):
        volume = width * height * length
        if volume >= VOLUME_THRESHOLD:
            return True
        else:
            return width >= DIMENSION_THRESHOLD or height >= DIMENSION_THRESHOLD or length >= DIMENSION_THRESHOLD
    
    def validate_mass(mass):
        return mass >= MASS_THRESHOLD
    
    # Input validation
    for name, value in {"width": width, "height": height, "length": length}.items():
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number (int or float), got {type(value)}")
        if value <= 0:
            raise ValueError(f"{name} must be non-negative and not 0, got {value}")
    
    # Rule calculation
    bulky = validate_dimensions(width, height, length)
    heavy = validate_mass(mass)

    if bulky and heavy:
        return REJECTED
    elif bulky or heavy:
        return SPECIAL
    else:
        return STANDARD
