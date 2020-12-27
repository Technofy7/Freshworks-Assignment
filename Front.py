import Back as s  #Importing Back file as library in this file


s.create("DarkArt",100,1500)  # Here creating key with key_name, Value and time-to-live property
s.create("Blackburn",50)    # Here creating key with key_name and value since time-to-live is optional so

s.create("DarkArt",30) # Trying to create duplicate entry then following error will pop up
#Error:: Key is already Exists

s.create("Swapnil_Pawar",80) # Trying to create entry having non char value then following error will pop up
#Error:: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers


s.read("Blackburn") # Reading data by providing key and following will be the output
#'Blackburn:50'

s.read("Akshay") # Reading data which is not actually present then following error will pop up
#Error:: Given key does not exist in database. Please enter a valid key

s.delete("Blackburn") # Deleting entry from file
#key is successfully deleted

s.delete("Swapnil") # Deleting entry which is not present then following error will pop up
#Error:: Given key does not exist in database. Please enter a valid key