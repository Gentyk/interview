import pandas as pd
import re

df = pd.read_excel(
    r'./v1.xls',
    skiprows=1  # пишем сюда сколько строк всерху пропускаем. В данном случае - только первую, т.к.
                # на второй строке имена столцов
)

# имена столбцов
print("Column headings:")
print(df.columns)

# удаление ненужных столбцов
exclude_columns = ['CC', 'Наименование', 'Tab', 'Пр.пл.', 'Ned1', 'Ned2', 'Ned3', 'Ned4', 'Ned5', 'Изб']
for name in exclude_columns:
    del df[name]

# выделение недель
columns = list(df.columns).copy()
del columns[columns.index(' ID_125 ')]
weeks = set([int(re.findall('\d+', name)[0]) for name in columns if re.findall('\d+', name)])
print(weeks)

# переименование столбцов
rename_dict = {'Gr'+str(i): 100+i for i in weeks}
rename_dict.update({'Pl'+str(i): 200+i for i in weeks})
df = df.rename(columns=rename_dict)

# приводим все столбцы к числовому виду
for i in df.columns:
    try:
        pd.to_numeric(df[i])
    except:
        pass
df = df.fillna(0)

# добавление новых столбцов
for i in weeks:
    df[300 + i] = df[200+i] - df[100+i]
    df[400 + i] = pd.Series(0, index=df.index)  # не посню, что ты хотел тут видеть

# упорядычивание столбцов
new_columns = []
for week in weeks:
    new_columns.extend([100+week, 200+week, 300+week, 400+week])
new_columns = [' ID_125 '] + new_columns

df = df[new_columns]
with pd.ExcelWriter('./output.xls') as writer:
    df.to_excel(writer)
# Если они напишут типа: ModuleNotFoundError: No module named 'xlwt' , то просто сделай pip install этот модуль


