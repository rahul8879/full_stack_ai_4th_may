import math
customer_data = [[12,15,13],[3,5,18],[5,6,21],[18,22,22]]
new_customer = [20,30,33]

# distance = {}

# for i in customer_data:
#     dist = math.sqrt((i[0]-new_customer[0])**2 + (i[1]-new_customer[1])**2)
#     distance[str(i)] = round(dist,2) # round(dist


# # sort the dict based on value
# distance = dict(sorted(distance.items(), key=lambda item: item[1]))
# # pick up the first key
# distance = list(distance.keys())[0]
# print(distance)


def distance(data,new_customer):
    distance = {}
    for i in data: 
        dist = math.sqrt((i[0]-new_customer[0])**2 + (i[1]-new_customer[1])**2)
        distance[str(i)] = round(dist,2) # round(dist
    # sorting the dict based on value
    distance = dict(sorted(distance.items(), key=lambda item: item[1]))
    # pick up the first key
    distance = list(distance.keys())[0]
    return distance


result = distance(customer_data,new_customer)
print(result)

def haversine(lat1, lon1, lat2, lon2):
    
    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) + 
         pow(math.sin(dLon / 2), 2) * 
             math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c


lat1 = 51.5007
lon1 = 0.1246
lat2 = 40.6892
lon2 = 74.0445
    
print(haversine(lat1, lon1,lat2, lon2), "K.M.")

# compare the distance : Hvaersine vs Euclidean??
dist = math.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)
print(dist)



# numpy, pandas ==> maths ( LA ---> search  engine --> cosine similarity)
# stats
# Ml ==> LA, stats
loan = [[2,3]]
branch = [[-1,2]]
penality =[ [3,4]]

from sklearn.metrics.pairwise import cosine_similarity

print(cosine_similarity(loan,branch))
print(cosine_similarity(loan,penality))