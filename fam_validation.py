from yamale import YamaleError
import yamale
import difflib
from deepdiff import DeepDiff
import yaml

"""
Validation function validates the input conditions with schema as the reference.
"""
def validation():
    #Create a schema object
    schema = yamale.make_schema(r'C:\Users\User\OneDrive\Documents\HPE\Task 1\schema.yml', parser='ruamel')
    # Create a Data object
    try:
        data = yamale.make_data(r'C:\Users\User\OneDrive\Documents\HPE\Task 1\tools-main\tools-main\config\fam_memoryserver_config.yaml', parser='ruamel')
        print (data)
    except Exception as s: #This line shows an exception if two memory_server_ids are same.
        print('The error is\n%s' % str(s))
    #To validate
    try:
        yamale.validate(schema, data)
        print('Validation success! 👍')
    except ValueError as e:
        print('Validation failed!\n%s' % str(e))
    
"""
Compare function is created to check the differences between the two memory_server. 
The difference found between the two is printed 
"""

def compare():
    try:
        #creates list
        data= open(r"C:\Users\User\OneDrive\Documents\HPE\Task 1\tools-main\tools-main\config\fam_memoryserver_config.yaml", 'r')
        parsed_yaml=yaml.safe_load(data)
        k=len(parsed_yaml)
        print('The length of list is %d'  %int(k))#Calculates the number of lists(memory_server_id) available
        ls1,ls2=parsed_yaml.values()
        if(ls1==ls2):
            print('All the conditions are the same')
        else:
            #to check differences
            ddiff = DeepDiff(ls1, ls2, ignore_order=True)
            print ('The differnces are:\n %s' %str(ddiff))
    except Exception as exc:
        print('The error is\n%s' % str(exc))


validation()
compare()


