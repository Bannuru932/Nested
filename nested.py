#!/usr/bin/env python
# encoding: utf-8

#object = raw_input("Please enter the object:")
key = input("Please enter the key in the form x/y/z:")
key_new = key.replace('/','')
key_final=list(key_new)
print(key_final)
def nested(inp_dict, nes_key):
    int_dict_val = inp_dict
    for k in nes_key:
        int_dict_val = int_dict_val.get(k, None)
        if int_dict_val is None:
            return None
    return int_dict_val
#print nested(object,list(key.replace('/','')))
print (nested({"a":{"b":{"c":1}}},list(key.replace('/',''))))
print (nested({"a":{"e":{"c":1}}},list(key.replace('/',''))))
#print nested({"a":{"b":{"c":1}}},list(key.replace('/','')))
