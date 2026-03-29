#Filter Strings Longer than 5 Characters.  Return words with length > 5.

s = ["abc","defg","abcdefgh"]

print(list(filter(lambda x: len(x)>5, s)))