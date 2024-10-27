frnd_lst=["Angelo", "Anagan", "Noosh", "leo", "Finn", "leo" ]  

# total iteams in list  
print(f"Tot no.of items : {len(frnd_lst)}\n") 

# How many items "leo" occurs in list 
print(f" No. of times leo occors : {frnd_lst. count("leo")}\n") 

# add item. using append() only one time can be added at a time 
frnd_lst.append("Finn") 
print(frnd_lst,"\n") 

# delete an item by item name 
frnd_lst.remove("leo") 
print(frnd_lst,"\n") 

# delete an item by item index, use pop(). 
frnd_lst.pop(1) 
print(frnd_lst,"\n") 

frnd_lst.pop() 
print(frnd_lst,"\n") 
