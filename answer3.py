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


a = top_200_university_dict.keys()
s = list(top_200_university_dict)
def university_list(s):
    r = []
    for i in range(len(s)):
        if i == 0:
            r.append(s[i])
        elif s[i] != s[i-1]:
            r.append(s[i])
    return r

university_list(s)

def university_set(a):
    a = top_200_university_dict
    b = top_200_university_dict.keys()
    c = set(b)
   return list(b)

"""

def check_ranking(dictionary, name, year):
	pass

def average_ranking(dictionary, name):
        
	pass


"""
