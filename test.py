from pprint import pprint
import hashmap

# test = hashmap.new() # assigns a new list to variable test a list with in a list
# hashmap.set(test, 'a', 1)
# print test # prints contents of test which is [[]] bacause it is empty

print '-' * 10, "Reverse engineer part1", '-' * 10
aMap_bucket = []
aMap_bucket2 = []
aMap = [aMap_bucket]
key = 'key1'
value = 'value1'

print '->' * 5, "def new(num_buckets)", '<-' * 5
print "getting new()"
print "aMap =", aMap
print '=' *50

print '->' * 5, "def hash_key(aMap, key)", '<-' * 5
print "getting hash_key(aMap, key)"
hash_key = hashmap.hash_key(aMap, key)
print "hash('key1') = ", hash(key)
print "len(aMap) = ", len(aMap)
print "returns hash_key =", hash_key
print '=' *50

print '->' * 5, "def get_bucket(aMap, key)", '<-' * 5
print "getting get_bucket(aMap, key)"
get_bucket = hashmap.get_bucket(aMap, key)
bucket_id = hash_key
aMap[bucket_id]
print "get_bucket = ", get_bucket
print "bucket_id = ", bucket_id
print "returns aMap[bucket_id] =", aMap[bucket_id]
print '=' *50

print '->' * 5, "def get_slot(aMap, key, default=None)",'<-' * 5
print "getting get_slot(aMap, key, default=None)"
get_slot = hashmap.get_slot(aMap, key, value) 
# bucket = get_bucket
bucket = get_bucket
print "bucket = ", bucket
print "returns get_slot = ", get_slot
print '=' *50

print '->' * 5, "def set(aMap, key, default=None)",'<-' * 5
print "getting set(aMap, key, value)"
set1 = hashmap.set(aMap, key, value)
i, k, v = get_slot
print "bucket = ", bucket
print "i, k, v = ", i, k, v
print "aMap contents: ",aMap
print '=' *50

print '->' * 5, "def get(aMap, key, default=None)",'<-' * 5
print "getting get(aMap, key, default=None)"
get = hashmap.get(aMap, key)
print "returns v: = ", get

print '-' * 10, "Reverse engineer part 2", '-' * 10
aMap1 = hashmap.new() # creates aMap1 dict
hashmap.set(aMap1, 'key1', 'value1') # sets value for aMap, key, value. 
# bucket gets get_bucket(aMap, key)
# where 
# i, k, v gets get_slot
# where get_slot(aMap, key, default=None) aMap = aMap1, key = 'key1', default=None = 'value1' 
print aMap1
# print "this is hash_key = ", test1
# print "this is the hash(key) '%' len(aMap) = hash_key = ", test1
# test2 = hashmap.get_bucket('a', 1)
# print "this is get_bucket =", test2
# print "this is the hash_key(aMap, key) = bucket_id = ", test1
# print "aMap[bucket_id] = ", test2
# print "this is def get_slot variable bucket =", test2
# test3 = test2
# print "bucket = ", test3

# print list(enumerate(test2))
# for i, kv in enumerate(test2):
# 	k, v = kv
# 	print k
# 	print v

# print hashmap.get_slot('a', 1, [])