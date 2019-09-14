import pandas as pd
from pandas import DataFrame
import re
import numpy as np


xl = pd.ExcelFile(r'./fuck.xls')

sheet_names = xl.sheet_names  # see all sheet names
print(sheet_names)

# КИМПАНИИ
companies_df = xl.parse(sheet_names[sheet_names.index('Sheet2')],
                        skiprows=1)
companies = [i[0].strip() for i in companies_df.values.tolist()]
# print(companies)

# файл
big_df = xl.parse(sheet_names[sheet_names.index('06 09')],
                  skiprows=2)
big_df['Примечание'] = big_df['Примечание'].apply(lambda x: x.strip())
big_df= big_df[big_df["Остаток"] != 0]
orig = big_df.loc[big_df['Примечание'].isin(companies)]
date = list(pd.unique(orig['Дата кон.']))
date = [pd.to_datetime(x) for x in date]
date.sort()
print(type(date[0]))
print(date)

print(big_df.index+1)
#cols = ['Примечание', 'id', 'name']
#cols.extend(date)
#new_df = DataFrame(columns=cols)
#print(new_df.keys())
n = []
for company in companies:
    data_df = big_df.loc[big_df['Примечание'].isin([company])]

    ids = list(pd.unique(data_df['Id_125']))

    # далее формируем строки
    for id in ids:
        print(data_df[data_df['Id_125'] == id], id)
        data_df_by_id = data_df[data_df['Id_125'] == id]
        print(len((data_df_by_id)))
        dates = {d: 0 for d in date}
        for ind in range(len(data_df_by_id)):
            x = data_df_by_id.iloc[ind]
            #print("!!!", x['Дата кон.'], type(x['Дата кон.']))
            dates[x['Дата кон.']] += int(x['Остаток'])
            if 'name' not in dates:
                dates['name'] = x['Наименование']
        dates['id'] = id
        n.append(dates.copy())
 #       new_df.append(dates.copy(), ignore_index=True)

#print(new_df)
new_df = DataFrame(n)
print(new_df)
with pd.ExcelWriter('./output3.xls') as writer:
    new_df.to_excel(writer)


#     print(pd.unique(big_df['Примечание']))
#print(orig)



# orig = xl.parse(sheet_names[0],
#     skiprows=1)
# #orig.drop(orig.index[[0,3]])
# print(orig.keys())
# orig = orig.loc[orig['CC'].isin([3,72])]
# print(orig)