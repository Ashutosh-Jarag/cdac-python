import pickle


d = {"name":"Raj", "marks":90,"subject":["a","b","c"]}



with open("file1.pkl","wb") as f:
    pickle.dump(d,f)
    
    
print("Picked Successfully...")



with open("file1.pkl","rb") as f:
    result = pickle.load(f)
    print("Unpickled successfully")
    
    
    
    
print(result)