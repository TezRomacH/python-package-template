"""Example of code."""


def hello(name: str) -> str:
    """Just an greetings example.

    Args:
        name (str): Name to greet.

    Returns:
        str: greeting message

    Examples:
        .. code:: python

            >>> hello("Jens")
            'Hello Jens!'
    """
    return f"Hello {name}!"
