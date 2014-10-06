def restaurant_ratings(filename):
    
    ratings = open(filename)
    ratings_dict = {}
    for line in ratings:
        line = line.rstrip()
        key_value_pair = line.split(":")
        name = key_value_pair[0]
        rating = int(key_value_pair[1])
        ratings_dict[name] = rating

    names = ratings_dict.keys()
    names.sort()
    for name in names:
        print "Restaurant '%s' is rated %d." % (name, rating)

def main():

    restaurant_ratings("score.txt")

if __name__ == "__main__":
    main()