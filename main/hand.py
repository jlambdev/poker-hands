from card import Card
import collections

class Hand(object):
	"""
	Represents a Hand in Poker
	"""
	TYPES = [
		'high card',
		'pair',
		'two pairs',
		'three of a kind',
		'straight',
		'flush',
		'full house',
		'four of a kind',
		'straight flush'
	]

	def __init__(self, card1, card2, card3, card4, card5):
		""" Constructor """
		self.cards = [card1, card2, card3, card4, card5]
		if self._duplicate_cards():
			raise TypeError('Invalid Hand')
		self.value_count = collections.defaultdict(int)
		for card in self.cards:
			self.value_count[card.value] += 1
		self.ordered_int_values = sorted([int(Card.VALUES.index(card.value)) 
										 for card in self.cards])
		self.type = self._get_type()
		self.value = self.TYPES.index(self.type) + 1
		
	def __str__(self):
		""" String Representation of the Hand object """
		return '{0} {1} {2} {3} {4}'.format(str(self.cards[0]),
											str(self.cards[1]),
											str(self.cards[2]),
											str(self.cards[3]),
											str(self.cards[4]))

	def _duplicate_cards(self):
		""" Check for the existence of duplicate cards in the Hand """
		card_string_set = set([str(card) for card in self.cards])
		return True if len(card_string_set) < 5 else False

	def _get_type(self):
		""" Determine the type of this Hand """
		four_of_a_kind = False
		full_house = False
		straight = False
		three_of_a_kind = False
		two_pairs = False
		one_pair = False
		
		# Check if all cards belong to the same suit
		all_cards_same_suit = True if len(set([card.suit for card in 
										  self.cards])) == 1 else False

		# Check for a straight
		for count, value in enumerate(self.ordered_int_values):
			if count == 0:
				continue
			if value - self.ordered_int_values[count - 1] == 1:
				if count == 4:
					straight = True
			else:
				break
		
		# Check for four/three of a kind, full house and pairs
		for card_value, occurences in self.value_count.iteritems():
			if occurences == 4:
				four_of_a_kind = True
			elif occurences == 3:
				three_of_a_kind = True
				if len(self.value_count) == 2:
					full_house = True
			elif occurences == 2:
				if one_pair:
					two_pairs = True
				else:
					one_pair = True

		if all_cards_same_suit and straight:
			return self.TYPES[8]		# straight flush
		elif four_of_a_kind:
			return self.TYPES[7]		# four of a kind
		elif full_house:
			return self.TYPES[6]		# full house
		elif all_cards_same_suit:
			return self.TYPES[5]		# flush
		elif straight:
			return self.TYPES[4]		# straight
		elif three_of_a_kind:
			return self.TYPES[3]		# three of a kind
		elif two_pairs:
			return self.TYPES[2]		# two pairs
		elif one_pair:
			return self.TYPES[1]		# one pair
		return self.TYPES[0]			# high card