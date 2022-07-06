import json


class Convert:

    def __init__(self):
        self.data_access = open(r'inputData.json')
        self.data = json.load(self.data_access)

    def executor_convert(self):
        data_load = {}
        data_interact = self.data['data_load']
        
        # Mount 'json' to mock payload in unit tests
        print('{')
        for field in data_interact:
            ## rule to manipulate fields ##
            field_with_removed_letter = field.replace(field[0], '')
            new_field = field[0].upper() + field_with_removed_letter
            new_field = new_field.replace('"', '')
            
            if type(self.data['data_load'][field]) == list:
                print(' '+new_field, '=', 'new List'+'<'+new_field+'>()', '[')
                print('    new', new_field, '=', '{')

                count = 0
                for data_array in self.data['data_load'][field]:
                    # List of objects in array
                    for interact_data_array in data_array:
                        ## rule to manipulate fields ##
                        remove_letter_array = interact_data_array.replace(interact_data_array[0], '')
                        new_field_array = interact_data_array[0].upper() + remove_letter_array
                        new_field_array = new_field_array.replace('"', '')
                        if type(data_array[interact_data_array]) == str:
                            print('       '+interact_data_array, '=', '"'+data_array[interact_data_array]+'"')
                        else:
                            print('       '+interact_data_array, '=', data_array[interact_data_array])
                    
                    count+=1
                    if count == len(self.data['data_load'][field]):
                        print('    },')
                        print(' ],')
                        break

                    print('    },')
                    print('    new', new_field, '=', '{')
                    
            if type(self.data['data_load'][field]) == dict:
                print(' '+new_field, '=', 'new', new_field+'()', '{')
                for field2 in self.data['data_load'][field]:
                    ## rule to manipulate fields ##
                    remove_letter = field2.replace(field2[0], '')
                    new_field2 = field2[0].upper() + remove_letter
                    new_field2 = new_field2.replace('"', '')
                    
                    if type(self.data['data_load'][field][field2]) == dict:
                        
                        print('    '+new_field2, '=', 'new', new_field2+'()', '{')

                        for field3 in self.data['data_load'][field][field2]:
                            ## rule to manipulate fields ##
                            remove_letter1 = field3.replace(field3[0], '')
                            new_field3 = field3[0].upper() + remove_letter1
                            new_field3 = new_field3.replace('"', '')
                            print('       '+new_field3, '=', '"'+self.data['data_load'][field][field2][field3]+'"')

                        print('    }')

                    else:
                        if type(self.data['data_load'][field][field2]) == str:
                            print('    '+new_field2, '=', '"'+self.data['data_load'][field][field2]+'"')
                        else:    
                            print('    '+new_field2, '=', self.data['data_load'][field][field2])
            
            if type(self.data['data_load'][field]) == str:
                print('    '+new_field, '=', '"'+self.data['data_load'][field]+'"')
            elif type(self.data['data_load'][field]) == int:    
                print('    '+new_field, '=', self.data['data_load'][field])
            elif type(self.data['data_load'][field]) == float:    
                print('    '+new_field, '=', self.data['data_load'][field])

        print('}')
        new_data_load = data_load
        return json.dumps(new_data_load, indent=4)

    def manipulate_data_to_rule_csharp():
        print('work in progress')