from main.card import Card
from main.hand import Hand
from main.game import Game
import unittest

class CardTest(unittest.TestCase):
	"""
	Test the Card class
	"""
	def test_sample_card(self):
		card = Card('3', 'D')
		self.assertEqual('3', card.value)
		self.assertEqual('D', card.suit)

	def test_invalid_suit(self):
		with self.assertRaises(TypeError) as context:
			Card('3', 'X')
			self.assertTrue('Invalid Card Suit' in context.exception)

	def test_invalid_value(self):
		with self.assertRaises(TypeError) as context:
			Card('0', 'D')
			self.assertTrue('Invalid Card Value' in context.exception)

	def test_card_int_values(self):
		self.assertEqual(1, Card('2', 'D').int_value())
		self.assertEqual(2, Card('3', 'H').int_value())
		self.assertEqual(3, Card('4', 'C').int_value())
		self.assertEqual(4, Card('5', 'S').int_value())
		self.assertEqual(5, Card('6', 'D').int_value())
		self.assertEqual(6, Card('7', 'H').int_value())
		self.assertEqual(7, Card('8', 'C').int_value())
		self.assertEqual(8, Card('9', 'S').int_value())
		self.assertEqual(9, Card('T', 'D').int_value())
		self.assertEqual(10, Card('J', 'H').int_value())
		self.assertEqual(11, Card('Q', 'C').int_value())
		self.assertEqual(12, Card('K', 'S').int_value())
		self.assertEqual(13, Card('A', 'D').int_value())

	def test_card_str(self):
		card = Card('8', 'H')
		self.assertEqual('8H', str(card))


class HandTest(unittest.TestCase):
	"""
	Test the Hand class
	"""
	def test_sample_hand(self):
		hand = Hand(Card('3', 'D'), 
					Card('2', 'H'),
					Card('Q', 'C'),
					Card('K', 'D'),
					Card('7', 'H'))
		self.assertEqual('3D 2H QC KD 7H', str(hand))

	def test_hand_types(self):
		self.assertEqual([
			'high card',
			'pair',
			'two pairs',
			'three of a kind',
			'straight',
			'flush',
			'full house',
			'four of a kind',
			'straight flush'
		], Hand.TYPES)

	def test_duplicate_cards_rejected(self):
		with self.assertRaises(TypeError) as context:
			Hand(Card('3', 'D'), 
				 Card('2', 'H'),
				 Card('5', 'C'),
				 Card('3', 'D'),	# duplicate
				 Card('9', 'H'))
			self.assertTrue('Invalid Hand' in context.exception)

	def test_high_card(self):
		hand = Hand(Card('3', 'D'), 
					Card('2', 'H'),
					Card('5', 'C'),
					Card('6', 'D'),
					Card('9', 'H'))
		self.assertEqual('high card', hand.type)
		self.assertEqual(1, hand.value)

	def test_pair(self):
		hand = Hand(Card('3', 'D'), 
					Card('2', 'H'),
					Card('5', 'C'),
					Card('3', 'C'),
					Card('9', 'H'))
		self.assertEqual('pair', hand.type)
		self.assertEqual(2, hand.value)

	def test_two_pairs(self):
		hand = Hand(Card('3', 'D'), 
					Card('5', 'H'),
					Card('5', 'C'),
					Card('3', 'C'),
					Card('9', 'H'))
		self.assertEqual('two pairs', hand.type)
		self.assertEqual(3, hand.value)

	def test_three_of_a_kind(self):
		hand = Hand(Card('3', 'D'), 
					Card('5', 'H'),
					Card('5', 'C'),
					Card('5', 'D'),
					Card('9', 'H'))
		self.assertEqual('three of a kind', hand.type)
		self.assertEqual(4, hand.value)

	def test_straight(self):
		hand = Hand(Card('2', 'D'), 
					Card('3', 'H'),
					Card('4', 'C'),
					Card('5', 'D'),
					Card('6', 'H'))
		self.assertEqual('straight', hand.type)
		self.assertEqual(5, hand.value)
		hand = Hand(Card('T', 'D'), 
					Card('J', 'H'),
					Card('Q', 'C'),
					Card('K', 'D'),
					Card('A', 'H'))
		self.assertEqual('straight', hand.type)
		self.assertEqual(5, hand.value)

	def test_flush(self):
		hand = Hand(Card('8', 'D'), 
					Card('4', 'D'),
					Card('J', 'D'),
					Card('K', 'D'),
					Card('A', 'D'))
		self.assertEqual('flush', hand.type)
		self.assertEqual(6, hand.value)

	def test_full_house(self):
		hand = Hand(Card('8', 'D'), 
					Card('8', 'H'),
					Card('8', 'C'),
					Card('A', 'C'),
					Card('A', 'D'))
		self.assertEqual('full house', hand.type)
		self.assertEqual(7, hand.value)

	def test_four_of_a_kind(self):
		hand = Hand(Card('T', 'D'), 
					Card('T', 'H'),
					Card('T', 'S'),
					Card('T', 'C'),
					Card('3', 'D'))
		self.assertEqual('four of a kind', hand.type)
		self.assertEqual(8, hand.value)

	def test_straight_flush(self):
		hand = Hand(Card('3', 'C'), 
					Card('4', 'C'),
					Card('5', 'C'),
					Card('6', 'C'),
					Card('7', 'C'))
		self.assertEqual('straight flush', hand.type)
		self.assertEqual(9, hand.value)
		hand = Hand(Card('9', 'H'), 
					Card('T', 'H'),
					Card('J', 'H'),
					Card('Q', 'H'),
					Card('K', 'H'))
		self.assertEqual('straight flush', hand.type)
		self.assertEqual(9, hand.value)


class GameTest(unittest.TestCase):
	"""
	Test the Game class
	"""
	def _create_hand(self, compressed_hand):
		return Hand(Card(compressed_hand[0], compressed_hand[1]), 
					Card(compressed_hand[2], compressed_hand[3]),
					Card(compressed_hand[4], compressed_hand[5]),
					Card(compressed_hand[6], compressed_hand[7]),
					Card(compressed_hand[8], compressed_hand[9]))
					
	def test_sample_games(self):
		game = Game('Player One',
					'Player Two',
					self._create_hand('3DJCAS4H2C'),
					self._create_hand('3HQSAC4D2H'))	# high card: Queen
		self.assertEqual('Player One', game.p1_name)
		self.assertEqual('Player Two', game.p2_name)
		self.assertEqual('3D JC AS 4H 2C', str(game.p1_hand))
		self.assertEqual('3H QS AC 4D 2H', str(game.p2_hand))
		self.assertEqual('Player Two', game.winner)
		self.assertEqual('Queen', game.winning_card)
		game = Game('Player One',
					'Player Two',
					self._create_hand('AC3C4H7D5C'),	# high card: Ace
					self._create_hand('KC3D4S7C5S'))
		self.assertEqual('Player One', game.p1_name)
		self.assertEqual('Player Two', game.p2_name)
		self.assertEqual('AC 3C 4H 7D 5C', str(game.p1_hand))
		self.assertEqual('KC 3D 4S 7C 5S', str(game.p2_hand))
		self.assertEqual('Player One', game.winner)
		self.assertEqual('Ace', game.winning_card)

	def test_high_card_cascade_game(self):
		game = Game('Jim',
					'Bob',
					self._create_hand('ADKCQS5H2C'),
					self._create_hand('AHKSQC5D3H'))	# high card: 3
		self.assertEqual('high card', game.p1_hand.type)
		self.assertEqual('high card', game.p2_hand.type)
		self.assertEqual('Bob', game.winner)
		self.assertEqual('3', game.winning_card)
		
	def test_pair_games(self):
		# pair beats high card
		game = Game('Jim',
					'Bob',
					self._create_hand('ADKCQS2H2C'),	# pair
					self._create_hand('AHKSQC5D3H'))	
		self.assertEqual('pair', game.p1_hand.type)
		self.assertEqual('high card', game.p2_hand.type)
		self.assertEqual('Jim', game.winner)
		self.assertIsNone(game.winning_card)
		# pair tie, winner has highest pair card
		game = Game('Jim',
					'Bob',
					self._create_hand('2D3CQS5H5C'),	
					self._create_hand('2H3SKC6D6H'))	# pair + high card: 3
		self.assertEqual('pair', game.p1_hand.type)
		self.assertEqual('pair', game.p2_hand.type)
		self.assertEqual('Bob', game.winner)
		self.assertEqual('6', game.winning_card)
		# pair tie, pair card values match, winner has highest remaining card
		game = Game('Jim',
					'Bob',
					self._create_hand('4D3CQS6S6C'),	# pair + high card: 4
					self._create_hand('2H3SQC6D6H'))	
		self.assertEqual('pair', game.p1_hand.type)
		self.assertEqual('pair', game.p2_hand.type)
		self.assertEqual('Jim', game.winner)
		self.assertEqual('4', game.winning_card)
		
	def test_two_pair_games(self):
		# two pairs beats pair
		game = Game('Dave',
					'Rob',
					self._create_hand('5H5S2C9STD'),	
					self._create_hand('6C6D4S4DJD'))	# two pairs
		self.assertEqual('pair', game.p1_hand.type)
		self.assertEqual('two pairs', game.p2_hand.type)
		self.assertEqual('Rob', game.winner)
		self.assertIsNone(game.winning_card)
		# two pair tie, winner has highest card for highest pair
		game = Game('Dave',
					'Rob',
					self._create_hand('5H5S3C3STD'),	# two pairs + high card: 6
					self._create_hand('6C6D4S4DJD'))	
		self.assertEqual('two pairs', game.p1_hand.type)
		self.assertEqual('two pairs', game.p2_hand.type)
		self.assertEqual('Rob', game.winner)
		self.assertEqual('6', game.winning_card)
		# two pair tie, winner has highest card for 2nd highest pair
		game = Game('Dave',
					'Rob',
					self._create_hand('6H6S4C4HTD'),	# two pairs + high card: 4
					self._create_hand('6C6D3S3DJD'))	
		self.assertEqual('two pairs', game.p1_hand.type)
		self.assertEqual('two pairs', game.p2_hand.type)
		self.assertEqual('Dave', game.winner)
		self.assertEqual('4', game.winning_card)
		# two pair tie, winner has highest card for unpaired card
		game = Game('Dave',
					'Rob',
					self._create_hand('6H6S4C4HTD'),	
					self._create_hand('6C6D4S4DJD'))	# two pairs + high card: Jack
		self.assertEqual('two pairs', game.p1_hand.type)
		self.assertEqual('two pairs', game.p2_hand.type)
		self.assertEqual('Rob', game.winner)
		self.assertEqual('Jack', game.winning_card)
		
	def test_three_of_a_kind_games(self):
		# three of a kind beats two pairs
		game = Game('Alan',
					'Steve',
					self._create_hand('6C6D6S2DJD'), 	# three oa. kind
					self._create_hand('6H9S9C4H4D'))	
		self.assertEqual('three of a kind', game.p1_hand.type)
		self.assertEqual('two pairs', game.p2_hand.type)
		self.assertEqual('Alan', game.winner)
		self.assertIsNone(game.winning_card)
		# three of a kind tie, winner has highest card in three of a kind
		game = Game('Alan',
					'Steve',
					self._create_hand('6C6D6S2DJD'), 	
					self._create_hand('7H7S7C4H2D'))	# three oa. kind + high card: 7
		self.assertEqual('three of a kind', game.p1_hand.type)
		self.assertEqual('three of a kind', game.p2_hand.type)
		self.assertEqual('Steve', game.winner)
		self.assertEqual('7', game.winning_card)
		
	def test_straight_games(self):
		# straight beats three of a kind 
		game = Game('Rupert',
					'Audrey',
					self._create_hand('5C6D8D7C4H'), 	# straight
					self._create_hand('8C8S8H6C3H'))	
		self.assertEqual('straight', game.p1_hand.type)
		self.assertEqual('three of a kind', game.p2_hand.type)
		self.assertEqual('Rupert', game.winner)
		self.assertIsNone(game.winning_card)
		# straight tie, winner has highest card 
		game = Game('Rupert',
					'Audrey',
					self._create_hand('5C6D8D7C4H'), 	
					self._create_hand('TDJS8H7D9C'))	# straight + high card: Jack
		self.assertEqual('straight', game.p1_hand.type)
		self.assertEqual('straight', game.p2_hand.type)
		self.assertEqual('Audrey', game.winner)
		self.assertEqual('Jack', game.winning_card)
		
	def test_flush_games(self):
		# flush beats straight
		game = Game('Gavin',
					'Nicky',
					self._create_hand('5C6D8D7C4H'), 	
					self._create_hand('2C6C8CQCJC'))	# flush
		self.assertEqual('straight', game.p1_hand.type)
		self.assertEqual('flush', game.p2_hand.type)
		self.assertEqual('Nicky', game.winner)
		self.assertIsNone(game.winning_card)
		# flush tie, winner has highest card
		game = Game('Gavin',
					'Nicky',
					self._create_hand('2D6D8DKDJD'), 	# flush + high card: King
					self._create_hand('2C6C8CQCJC'))	
		self.assertEqual('flush', game.p1_hand.type)
		self.assertEqual('flush', game.p2_hand.type)
		self.assertEqual('Gavin', game.winner)
		self.assertEqual('King', game.winning_card)
		
	def test_full_house_games(self):
		# full house beats flush
		game = Game('Oscar',
					'Gerome',
					self._create_hand('7C7D7S4H4C'), 	# full house
					self._create_hand('2C6C8CQCJC'))	
		self.assertEqual('full house', game.p1_hand.type)
		self.assertEqual('flush', game.p2_hand.type)
		self.assertEqual('Oscar', game.winner)
		self.assertIsNone(game.winning_card)
		# full house tie, winner has highest card from three of a kind
		game = Game('Oscar',
					'Gerome',
					self._create_hand('7C7D7SQHQC'), 	
					self._create_hand('TCTDTS3H3C'))	# full house + high card: Ten
		self.assertEqual('full house', game.p1_hand.type)
		self.assertEqual('full house', game.p2_hand.type)
		self.assertEqual('Gerome', game.winner)
		self.assertEqual('Ten', game.winning_card)
		
	def test_four_of_a_kind_games(self):
		# four of a kind beats full house
		game = Game('Sam',
					'Tom',
					self._create_hand('7C7D7S4H4C'), 	
					self._create_hand('2C2D2S2HJC'))	# four of a kind
		self.assertEqual('full house', game.p1_hand.type)
		self.assertEqual('four of a kind', game.p2_hand.type)
		self.assertEqual('Tom', game.winner)
		self.assertIsNone(game.winning_card)
		# four of a kind tie, winner has highest card from four of a kind
		game = Game('Sam',
					'Tom',
					self._create_hand('6C6D6S6H3C'), 	
					self._create_hand('2C2D2S2HAC'))	# four of a kind + high card: 6
		self.assertEqual('four of a kind', game.p1_hand.type)
		self.assertEqual('four of a kind', game.p2_hand.type)
		self.assertEqual('Sam', game.winner)
		self.assertEqual('6', game.winning_card)
		game = Game('Sam',
					'Tom',
					self._create_hand('6C6D6S6H3C'), 	
					self._create_hand('8C8D8S8H2C'))	# four of a kind + high card: 8
		self.assertEqual('four of a kind', game.p1_hand.type)
		self.assertEqual('four of a kind', game.p2_hand.type)
		self.assertEqual('Tom', game.winner)
		self.assertEqual('8', game.winning_card)
		
	def test_straight_flush_games(self):
		# straight flush beats four of a kind
		game = Game('Jeremy',
					'John',
					self._create_hand('8D6D7D9DTD'), 	# straight flush
					self._create_hand('2C2D2S2HJC'))	
		self.assertEqual('straight flush', game.p1_hand.type)
		self.assertEqual('four of a kind', game.p2_hand.type)
		self.assertEqual('Jeremy', game.winner)
		self.assertIsNone(game.winning_card)
		# straight flush tie, winner has highest card
		game = Game('Jeremy',
					'John',
					self._create_hand('8D6D7D9DTD'), 	
					self._create_hand('ASKSJSQSTS'))	# straight flush + high card: Ace
		self.assertEqual('straight flush', game.p1_hand.type)
		self.assertEqual('straight flush', game.p2_hand.type)
		self.assertEqual('John', game.winner)
		self.assertEqual('Ace', game.winning_card)


class AcceptanceTest(unittest.TestCase):
	"""
	Acceptance test for the TDD exercise
	"""
	def test_string_game_builer(self):
		game = Game.build('One: 3D JC AS 4H 2C  Two: 3H QS AC 4D 2H')
		self.assertEqual('One', game.p1_name)
		self.assertEqual('Two', game.p2_name)
		self.assertEqual('3D JC AS 4H 2C', str(game.p1_hand))
		self.assertEqual('3H QS AC 4D 2H', str(game.p2_hand))
		self.assertEqual('Two', game.winner)
		self.assertEqual('Queen', game.winning_card)
	
	def test_acceptance_criteria(self):
		game = Game.build('Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH')
		self.assertEqual('White wins. - with high card: Ace', game.result())
		game = Game.build('Black: 2H 4S 4C 2D 4H  White: 2S 8S AS QS 3S')
		self.assertEqual('Black wins. - with full house', game.result())
		game = Game.build('Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C KH')
		self.assertEqual('Black wins. - with high card: 9', game.result())
		game = Game.build('Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 9S KH')
		self.assertEqual('Tie.', game.result())
		
if __name__ == '__main__':
	unittest.main()





