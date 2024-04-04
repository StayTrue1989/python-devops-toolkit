import os


def get_variable(
    name: str, required: bool = False, default: str | None = None
) -> str | None:
    """
    Fetch the value of an environment variable.

    This function retrieves the value of an environment variable, with options to
    specify if it is required and to provide a default value if it is not set or only
    contains whitespace.

    Args:
        name: Environment variable name.
        required: If True, raises KeyError for unset or whitespace-only values.
        default: Default value if variable is unset or only whitespace.

    Returns:
        Variable's value, or default if provided, otherwise None.

    Raises:
        KeyError: If `required` is True and variable is unset or whitespace-only.
    """
    value = os.getenv(name)
    if required and (not value or value.isspace()):
        raise KeyError(f"{name} variable missing.")
    return value or default


def required(name: str) -> str:
    """
    Fetch the value of a required environment variable.

    This is a convenience function for `get_variable`, set to require the specified
    environment variable.

    Args:
        name: Environment variable name.

    Returns:
        Non-empty variable's value.

    Raises:
        KeyError: If variable is unset or whitespace-only.
    """
    return get_variable(name, required=True)
