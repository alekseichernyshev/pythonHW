
import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
# pd.get_dummies(data['whoAmI'])
def get_column(person, data_who_am_i):
    person_list = []
    for val in data_who_am_i:
        if val == person:
            person_list.append(1)
        else:
            person_list.append(0)
    return pd.Series(person_list, name=person)

data_one_hot = pd.concat([
    get_column('robot', data['whoAmI']),
    get_column('human', data['whoAmI'])
    ], axis=1)
data_one_hot.head(20)