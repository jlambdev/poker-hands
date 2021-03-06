# Description of each step taken

0. 	Before programming, read spec and came up with an initial design
1.	Created test module with a simple assertion to get up and running
2. 	Added CardTest to create a card with a given suit and value
3. 	Created Card class and made the test pass
4. 	Added CardTest for invalid cards, assert exceptions thrown for invalid suits and values
5. 	Updated Card class with recognised suits and values to make tests pass
6. 	Added CardTest to get an integer value for all card values (so we can compare cards later)
7. 	Updated Card class with int_value() method to make tests pass
8. 	Added HandTest to create a hand of Cards
9. 	Created Hand class, realised a __str__ method was required for Card class, so test was written
10. Implemented __str__ for Card class, Hand class updated
11.	Updated HandTest for recognised hand types
12. Implemented types for Hand class
13. Updated HandTest for High Card rule
	Hand should identify itself as high card and return hand value
14. Updated Hand class with crude implementation to pass (no logic implemented, only code to pass test)
15. HandTest updated for Pair rule
16. Hand Cards now in an array
	Used Python at command line to see if defaultdict from collections would be useful here
	Implemented logic to detect pairs, default Hand type set to 'high card'
17. HandTest updated for Two Pairs rule
18. Hand _get_type updated to set boolean flags for single and double pairs detected
19. HandTest updated for Three of a Kind rule
20. Implemented boolean solution for Three of a Kind test
21. HandTest updated for Straight rule (2x cases)
22. Python at command line to check how to create an ordered list of values
	Implemented straight check using ordered int values of cards
23. HandTest updated for Flush rule
24. Implemented check to see if the set of suits of all Cards is 1 (i.e. all are the same suit)
25. HandTest updated for Full House rule
26.	Added check on the length of the value_count list if Three of a Kind found to determine full house
27. HandTest updated for Four of a Kind rule
28.	Added check for 4x occurences of the same value to satisfy Four of a Kind test
29. HandTest updated for Straight Flush rule (2x cases)
30. Added simple conditional boolean check to satisfy test
31. HandTest updated to reject duplicate cards
32. Created _duplicate_cards() check in constructor to satisfy test
33. Revealed duplicate cards in 4x other tests!
	Card samples for Hand tests updated to remove duplicates
34. GameTest created with 2x high card games as a sample (identify players, hands and winner)
35. Game class created, implemented winning hand and high value card comparison
36.	GameTest updated for high card game with all cards compared
	Included test to identify the responsible winning card
37. Updated Game class to make test pass & parse card value to human readable string
38. Updated initial GameTest sample to check if 'Ace' and 'Queen' are returned as winning card 
39.	Created _card_value_to_string to return 'Ace' if card value is 'A' etc.
40. Updated GameTest for Pair winning scenarios (including high card comparisons) 3x cases
41. No code changes required for tests to pass
42.	Updated Pair scenario with higher value card than pair value to break test
43. Exposed Hand's value_count and ordered_int_values so they may be used by the Game class
44. Refactored value comparison in Game class to satisfy tests
45. Updated GameTest for Two Pair winning scenarios, 4x cases
46. Noticed need to use T instead of 10 for a card value, Card test updated
47. Updated code to make all existing tests pass 
48. Returned to GameTest for Two Pair scenarios, updated Game class to make test pass
49. GameTest updated for Three of a Kind scenarios
50.	Updated Game to prioritise Three of a Kind for card comparison
51. GameTest updated for Straight scenarios, tests pass with no code changes 
52. GameTest updated for Flush scenarios, tests pass with no code changes 
53. GameTest updated for Full House scenarios
54. Updated Game to include full house in comparison
55. GameTest updated for Four of a Kind scenarios
56. Updated Game to include four of a kind in comparison
57. GameTest updated for Straight Flush scenarios, tests pass with no code changes
58. Created AcceptanceTest to meet success criteria
59. Added test for alternate Game construction based on String input
60. Implemented builder for game strings
61. Added acceptence test based on sample games and expected string results
62. Create result() method for game to get string representation of results
