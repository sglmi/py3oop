from notebook import Notebook, Note



notebook1 = Notebook()

# Check notes of the notebook object is empty after creation.
assert notebook1.notes == []
print("Notebook object created.")

# Note creation
notebook1.new_note("My first note")
notebook1.new_note("My second note", "tag1,tag2")
print("Notes created successfuly.")

# check id of the first note
assert notebook1.notes[0].id == 1
print("Check id of the first note")

# match against first note
assert notebook1.modify_memo(1, "new note") == True
print("First note modified successfuly.")

assert notebook1.modify_memo(999, "something") == False
print("Return False if note not found.")




