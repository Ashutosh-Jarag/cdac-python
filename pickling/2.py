import pickle
l = [(1,"AA",2000),(2,"BB",3000),(3,"CC",4000)]


with open("file2.pkl","wb") as f:
    pickle.dump(l,f)
    
    
print("Picked Successfully...")



with open("file2.pkl","rb") as f:
    result = pickle.load(f)


print("Unpickled successfully")
    
for id, name, sal in result:
    print(f"id:{id} | name::{name} | sal:{sal}")
    
       
    
print(result)