from datetime import date as date_lib
from datetime import datetime
import pandas as pd
from pandas import DataFrame
from xlrd import open_workbook
from xlutils.copy import copy


def main(filename, big_sheet, company_sheet, result_filename):
    # считываем книгу
    xl = pd.ExcelFile(filename)

    # получаем список фирм
    companies_df = xl.parse(company_sheet)  # лист с наименованием фирм
    companies = [i.strip() for i in list(companies_df['Примечание'])]

    # большой файл
    big_df = xl.parse(big_sheet, skiprows=2)

    # получим конечные даты для команий из списка (для формирования столбцов итговой таблицы)
    big_df['Примечание'] = big_df['Примечание'].apply(lambda x: x.strip())
    orig = big_df.loc[big_df['Примечание'].isin(companies)]
    date = list(pd.unique(orig['Дата кон.']))
    date = [pd.to_datetime(x) for x in date]
    date.sort()

    # формирование выходного файла
    # для начала сформируем пустую строку (кличи - это имена столбцов)
    columns = {"id": None, "Наименование": None}
    for d in date:
        columns[d] = 0
    columns['итог'] = 0
    columns['план'] = 0

    Global_GF = DataFrame()
    for company in companies:
        # для каждой комании получаем id товаров без повторений
        new_table_data = []
        data_df = big_df.loc[big_df['Примечание'].isin([company])]
        ids = list(pd.unique(data_df['Id_125']))

        # далее формируем строки (один товар - одна строка)
        for id in ids:
            new_row = columns.copy()
            data_df_by_id = data_df[data_df['Id_125'] == id]
            summ = 0
            summ_plan = 0
            for ind in range(len(data_df_by_id)):
                x = data_df_by_id.iloc[ind]
                new_row[x['Дата кон.']] += int(x['Остаток'])
                summ += int(x['Остаток'])
                summ_plan += int(x['План'])
                if not new_row['Наименование']:
                    new_row['Наименование'] = x['Наименование']
            new_row['id'] = id
            new_row['итог'] = summ
            new_row['план'] = summ_plan
            new_table_data.append(new_row.copy())

        # получившийся массив строк засовываем в локальную табличку (одна локальная табличка - одна комания)
        local_DF = DataFrame(new_table_data.copy())

        # формируем строку итоговых результатов на компании
        new_row = columns.copy()
        summ = 0
        for d in date:
            new_row[d] = local_DF[d].sum()
            summ += local_DF[d].sum()
        new_row['план'] = local_DF['план'].sum()
        new_row['id'] = company + ' План ' + str(local_DF['план'].sum()) + "              Итог осталось"
        new_row['итог'] = summ
        local_DF = local_DF.append(new_row.copy(), ignore_index=True)   # добавляем итоговую строчку в локальную табличку

        # локальную таблицу дописываем к глобальной
        Global_GF = Global_GF.append(local_DF.copy())

    # Переименовываем столбцы
    new_column_names = []
    for i in columns:
        if i in date:
            new_column_names.append(date_lib(i.year, i.month, i.day))
        else:
            new_column_names.append(i)
    Global_GF.columns = new_column_names
    print(Global_GF.columns)
    
    # Замена нулевых значений на пустоту
    Global_GF = Global_GF.replace(0, "")
    with pd.ExcelWriter(result_filename) as writer:
        Global_GF.to_excel(writer, index=False, startrow=1)
    
    # текущую дату добавляем на первую строку во вторую ячейку
    rb = open_workbook(result_filename)
    wb = copy(rb)
    s = wb.get_sheet(0)
    s.write(0, 1, datetime.now().strftime("%d.%m.%Y"))
    wb.save(result_filename)

if __name__ == '__main__':
    filename = "6vip.xls"   # имя входного файла или путь
    big_sheet_name = "13 09"    # имя листа с большой таблицей
    company_sheet_name = "Sheet2"   # имя , где лежат имена фирм
    result_filename = "output.xls"
    main(filename, big_sheet_name, company_sheet_name, result_filename)
