import json

# Create a dictionary object
person_dict = {'first': 'Christopher', 'last':'Harrison'}
# Add additional key pairs to dictionary as needed
person_dict['City']='Seattle'
# Create a list object of programming languages 
languages_list = ['CSharp','Python','JavaScript']

# Add list object to dictionary for the languages key
person_dict['languages']= languages_list

# create a staff dictionary
# assign a person to a staff position of program manager
staff_dict ={}
staff_dict['Program Manager']=person_dict
# Convert dictionary to JSON object
staff_json = json.dumps(staff_dict)

# Print JSON object
print(staff_json)