import pickle

my_pickled_object = pickle.dumps(a_number)
print(my_pickled_object)

my_unpickled_object = pickle.loads(my_pickled_object)
print(my_unpickled_object)