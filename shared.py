# shared.py
sensitivity = 2.5  # Default value


def get_sensitivity():
    """Getter for sensitivity value"""
    global sensitivity
    return sensitivity


def set_sensitivity(value):
    """Setter for sensitivity value"""
    global sensitivity
    sensitivity = value
