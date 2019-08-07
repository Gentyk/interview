import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel(
    r'./v1.xls',
    skiprows=1  # пишем сюда сколько строк всерху пропускаем. В данном случае - только первую, т.к.
                # на второй строке имена столцов
)


# имена столбцов
print("Column headings:")
print(df.columns)

# пусть нам столбец не нужен - удаляем
del df['Tab']
print(df)


# приводим все столбцы, кроме "Наименование" к числовому виду
for i in df.columns:
    if i != "Наименование":
        try:
            pd.to_numeric(df[i])
        except:
            pass

# примерно так выглядит вычетание
df['diff']=df.Gr36-df.Gr39
print(df[["diff"]])
