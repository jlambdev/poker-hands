from card import Card
from hand import Hand

class Game(object):
	"""
	Represents a game of Poker (as a comparison of 2 poker Hands)
	"""
	def __init__(self, p1_name, p2_name, p1_hand, p2_hand):
		""" Constructor """
		self.p1_name = p1_name
		self.p2_name = p2_name
		self.p1_hand = p1_hand
		self.p2_hand = p2_hand
		self.winner, self.winning_card = self._winning_hand()
		
	@staticmethod
	def build(strrep):
		""" Construct game based on a string representation of players and hands """
		terms = strrep.replace(':', '').split(' ')
		terms = filter(None, terms)
		return Game(terms[0], 
					terms[6],
					Hand(Card(terms[1][0], terms[1][1]),
						 Card(terms[2][0], terms[2][1]),
						 Card(terms[3][0], terms[3][1]),
						 Card(terms[4][0], terms[4][1]),
						 Card(terms[5][0], terms[5][1])),
					Hand(Card(terms[7][0], terms[7][1]),
						 Card(terms[8][0], terms[8][1]),
						 Card(terms[9][0], terms[9][1]),
						 Card(terms[10][0], terms[10][1]),
						 Card(terms[11][0], terms[11][1])))
						 
	def result(self):
		""" Get a string representation of the result of the Game """
		if not self.winner:
			return 'Tie.'
		winning_hand_type = self.p1_hand.type if self.winner == self.p1_name \
							else self.p2_hand.type
		if not self.winning_card:
			return '{0} wins. - with {1}'.format(self.winner, winning_hand_type)
		return '{0} wins. - with {1}: {2}'.format(self.winner, 
												  winning_hand_type,
												  self.winning_card)

	def _winning_hand(self):
		""" Compare Poker Hands and determine which is the winner """
		if self.p1_hand.value > self.p2_hand.value:
			return self.p1_name, None
		elif self.p1_hand.value < self.p2_hand.value:
			return self.p2_name, None
		else:
			return self._compare_card_values()

	def _compare_card_values(self):
		""" Compare highest value cards of Hands, depending on Hand types """
		matching_vals = ['four of a kind', 'full house','three of a kind', 'two pairs', 'pair']
		if self.p1_hand.type in matching_vals:
		
			def get_sorted_value_list(value_count):
				single_list = sorted([int(Card.VALUES.index(key)) for key 
							  in value_count if value_count[key] == 1])
				pair_list = sorted([int(Card.VALUES.index(key)) for key 
							in value_count if value_count[key] == 2])
				triple_list = sorted([int(Card.VALUES.index(key)) for key 
							  in value_count if value_count[key] == 3])
				quad_list = sorted([int(Card.VALUES.index(key)) for key 
							in value_count if value_count[key] == 4])
				return single_list + pair_list + triple_list + quad_list
						
			p1_hand_values = get_sorted_value_list(self.p1_hand.value_count.copy())
			p2_hand_values = get_sorted_value_list(self.p2_hand.value_count.copy())
			
		else:
			p1_hand_values = sorted([int(Card.VALUES.index(card.value)) 
									for card in self.p1_hand.cards])
			p2_hand_values = sorted([int(Card.VALUES.index(card.value)) 
									for card in self.p2_hand.cards])

		for hand_1_value in reversed(p1_hand_values):
			hand_2_value = p2_hand_values[p1_hand_values.index(hand_1_value)]
			if hand_1_value > hand_2_value:
				return self.p1_name, self._card_value_to_string(hand_1_value)
			if hand_1_value < hand_2_value:
				return self.p2_name, self._card_value_to_string(hand_2_value)
		
		return None, None
				
	def _card_value_to_string(self, int_value):
		""" Return the human readable string for a given integer card value """
		short_str_rep = Card.VALUES[int_value]
		if short_str_rep in Card.HIGH_CARD_NAMES:
			return Card.HIGH_CARD_NAMES[short_str_rep]
		return short_str_rep