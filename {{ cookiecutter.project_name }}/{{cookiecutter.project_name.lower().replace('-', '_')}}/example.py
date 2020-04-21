"""We use this file as an example for some module."""


def hello(name: str) -> str:
    """Just an example.

    Args:
        name (str): Name to greet.

    Returns:
        str: greeting message

    Examples:
        .. code:: python

            >>> hello("Roman")
            "Hello Roman!"

            >>> hello("Taylor")
            "Hello Taylor!"
    """
    return f"Hello {name}!"


__all__ = ["hello"]
