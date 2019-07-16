f = open("Top200_Times_World_University_Ranking_2011-2016.csv","r")
lines = f.readlines()

top_200_university_dict = dict()

for line in lines:
        line = line.strip()
        line = line.rstrip()

        # tokens list
        tokens = line.split(',')

        # tokens[0~3]

        university = tokens[2]

        if university in top_200_university_dict :
                
                local_dict = top_200_university_dict[university]
                local_dict['Year'].append(tokens[0])
                local_dict['Ranking'].append(tokens[1])
                local_dict['Country'].append(tokens[3])

                print("updated ...")
                
        else :
                local_dict = dict()

                local_dict['Year'] = [tokens[0]]
                local_dict['Ranking'] = [tokens[1]]
                local_dict['Country'] = [tokens[3]]

                top_200_university_dict[university] = local_dict

                print("inserted ...")
        

        

        


                              
top_200_university_dict

              
def university_list(dictionary):
        dictionary = {top_200_university_dict.keys}
        print(top_200_university_dict.keys)
        
        
def university_set(dictionary):
        pass

def check_ranking(dictionary, name, year):
	pass

def average_ranking(dictionary, name):
        pass

