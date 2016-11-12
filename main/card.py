class Card(object):
	"""
	Represents a Card in Poker
	"""
	SUITS = ['S' ,'D', 'C', 'H']
	VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
	HIGH_CARD_NAMES = {
		'T': 'Ten',
		'J': 'Jack',
		'Q': 'Queen',
		'K': 'King',
		'A': 'Ace'
	}

	def __init__(self, value, suit):
		""" Constructor """
		if value not in self.VALUES: 
			raise TypeError('Invalid Card Value')
		if suit not in self.SUITS:
			raise TypeError('Invalid Card Suit')
		self.value = value
		self.suit = suit
		
	def int_value(self):
		""" Return int to represent Card's actual value """
		return self.VALUES.index(self.value) + 1

	def __str__(self):
		""" String representation of the Card object """
		return '{0}{1}'.format(self.value, self.suit)
