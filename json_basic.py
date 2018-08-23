import json
blackjack_hand = (4, 'yes')
# writing data using dumps / decode to json string
encoded_hand = json.dumps(blackjack_hand)
# loading data to file / encode as python object
decoded_hand = json.loads(encoded_hand)

# check both are of equal type
print(blackjack_hand == decoded_hand)
# is tuple
print(type(blackjack_hand))
# is list
print(type(decoded_hand))
#is string
print(type(encoded_hand))
#prints true
print(blackjack_hand == tuple(decoded_hand))
# output will be same but type differs because of encode and decode
print(blackjack_hand)
print(encoded_hand)
print(decoded_hand)
