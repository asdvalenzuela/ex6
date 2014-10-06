
ratings = open("scores.txt")
ratings_as_dict = {}
for line in ratings:
    line = line.rstrip()
    key_value_pair = line.split(":")
    name = key_value_pair[0]
    rating = int(key_value_pair[1])
    ratings_as_dict[name] = rating

names = ratings_as_dict.keys()
names.sort()
for name in names:
    print "Restaurant '%s' is rated %d" % (name, rating)


