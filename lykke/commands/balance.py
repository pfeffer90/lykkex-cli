"""The balance command."""

from .base import Base


class Balance(Base):
    """Get lykkex balance"""

    def run(self):
        print('Getting balance...')