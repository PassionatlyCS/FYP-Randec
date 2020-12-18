import json
import pandas as pd
import csv
import os
import sys
import codecs #open and write multiple 

# Load the Drive helper and mount
from google.colab import drive

# This will prompt for authorization.
#drive.mount('/content/drive/MyDrive/ColabNotebooks/FYPTestingFolder/FinalFolder/DataSet/')


#print("Loaded 1st box")

#tokanized paramters/features
token_feat = ["behavior.processes.modules.basename","signatures.marks.call.api","signatures.marks.ioc","network.domains.domain"]

#print("loaded 2nd box")

#features per report
def feat_extract(json_var, feat_Array_key):
  for i in range (1,4):
    #nonempty values
    if feat_Array_key:
        indiviual_keyIndex = 0
        indiviual_key = feat_Array_key[0]
        if type( json_var ) is dict:
            print("Haan bhai scene hai")
            #no values loaded in dictionary
            if not json_var:
                print( "Empty json dictionary being sent, correct the path" )
                return
            print("Current json variables", json_var )
            if indiviual_key in json_var.keys():
                print("key value hai")
                json_var =  json_var[indiviual_key]
            else:
                print( "Koi value nahin hai" )
                return

            print("json_var", str(json_var) )
            print("feature arrays", feat_Array_key[indiviual_keyIndex+1:] )
            if not ( ( type( json_var ) is dict ) or ( type( json_var ) is list ) ) and bool(json_var):
                    feat_extract_array.append(json_var)
            else: 
                feat_extract( json_var, feat_Array_key[indiviual_keyIndex+1:] )

        #For a list
        elif type( json_var ) is list:
            # return from function if list is empty
            if not json_var:

                print( "Json list -> dictionary empty" )
                return
            for index, value in enumerate( json_var ):
                print( "List values yeh hain afaq, yeh wali save horahi hain: ",value )
                if not value:
                    print( "No nested list -.-" )
                    continue
                print( "index", index )
                print( "Value", value )
                feat_extract( value, feat_Array_key[indiviual_keyIndex:] )
            print("save ho gayi list")
            # check if feature accessor has only one value left
            if not json_var:
                    print("Empty json, go back")
                    return
            feat_extract( json_var, feat_Array_key[indiviual_keyIndex+1:] )
        else:
            print(json_var)
            #print("Should be a single value")

feature_file = pd.DataFrame()
datapath = "/contents/19.json"
#datapath = "/contents/benign_report.json"
unique_features = []
unique_features.clear()

feat_extract_array = []
feat_extract_array.clear()

unique_features = []
unique_features.clear()

feat_extract_array = []
feat_extract_array.clear()

#print(datapath)
cuckoo_report =  datapath

#multiple or nested tokenized features/
for indiviual_required_feature in  token_feat:

    tryout = indiviual_required_feature.split(".")
    print(tryout)
    feat_extract( cuckoo_report, tryout )
    print( "feat_extract_array after populating: ", feat_extract_array  )
        #feature_file.at[datapath, "class"] = 1 (uncomment this or next line other depending on the dataset being prepared)
        #feature_file.at[datapath, "class"] = 0

    # loop over all the fetures extracted
    for item in feat_extract_array:
        save_feature = indiviual_required_feature + "." + item
        unique_features.append( save_feature )
        feature_file.at[ datapath, save_feature] = 1

print("Unique Features: ", unique_features)
print( feature_file.head() )
#print("Box 7")
result= '/content/feature_file.csv'
feature_file.to_csv('feature_file.csv')
