def restaurant_ratings(filename):
    
    ratings = open(filename)
    ratings_dict = {}
    for line in ratings:
        line = line.rstrip()
        key_value_pair = line.split(":")
        name = key_value_pair[0]
        rating = int(key_value_pair[1])
        ratings_dict[name] = rating

    #the following code will sort alphabetically by name
    #names = ratings_dict.keys()
    #names.sort()
    #for name in names:
     #   print "Restaurant '%s' is rated %d." % (name, rating)

    #the following code will sort by numerical rating
    for key, value in sorted(ratings_dict.items(), key = lambda restaurant: restaurant[1]):
        print "Restaurant '%s' is rated %s." % (key, value)

def main():

    restaurant_ratings("scores.txt")

if __name__ == "__main__":
    main()