"""We use this file as an example for some module."""


def hello(name: str) -> str:
    """Just an example.

    Args:
        name (str): Name to greet.

    .. code:: python

        >>> hello("Roman")
        "Hello Roman!"

    """
    return f"Hello {name}!"
