#!/usr/bin/python3
"""representing integer class"""


class MyInt(int):
    def __eq__(self, other):
        """
        Override the == operator.

        Invert the behavior of the == operator.

        Args:
        - other: The object to compare with.

        Returns:
        - True if the objects are not equal.
        - False if the objects are equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator.

        Invert the behavior of the != operator.

        Args:
        - other: The object to compare with.

        Returns:
        - True if the objects are equal.
        - False if the objects are not equal.
        """
        return super().__eq__(other)
