import memory_profiler as mem_profile
import random
import time

names = ["John", "Jon", "Adam", "Steve", "Rick", "Thomos"]
majors = ["Math", "Engineering", "psychology", "Atrs", "Business"]

# reguler function
print("Memory (Before) : {}Mb" + str(mem_profile.memory_usage()) + 'Mb')

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id ': i,
            "name" : random.choice(names),
            "major " : random.choice(majors)
            }
        result.append(person)
    return result 
t1 = time.process_time()
people = people_list(100000)
t2 = time.process_time()

print("Memory (After) : {}Mb" +  str(mem_profile.memory_usage()) + 'Mb')
print("Took " + str(t2-t1) + "seconds")

# using generatior function:
print("Memory(Before) : Mb" + str(mem_profile.memory_usage() ) + 'Mb')
def gen_people_list(people_num):
    for i in range(people_num):
        person = {
            "id" : i,
            "name" : random.choice(names),
            "major" : random.choice(majors)
            }
        yield person
t3 = time.process_time()
people = gen_people_list(100000)
t4 = time.process_time()

print("Using Generator Function ")
print("Memory(After) : {}mb" + str(mem_profile.memory_usage()) + 'Mb')
print("Took" + str(t4-t3) + "seconds")


        

















        
