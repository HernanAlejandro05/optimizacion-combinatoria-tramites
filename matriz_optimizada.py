import pandas as pd


excel_data = pd.read_excel(r'C:\Users\alejo\.spyder-py3\combinaciones_160_filtrados.xlsx')


data = pd.DataFrame(excel_data, columns=[
                    'T5', 'T4', 'T3', 'T2', 'T1'])

#data.head()


matriz = data.to_records()
t=[0.5, 1, 4, 8, 16]

count = 0
for row in matriz:
    _, t5, t4, t3, t2, t1 = row
    
    condicion_1 = (t5 >= 10 and t5 <= 24)
    condicion_2 = (t4 >= 9 and t4 <= 15)
    condicion_3 = (t3 >= 6 and t3 <= 12)
    condicion_4 = (t2 >= 3 and t2 <= 6)
    condicion_5 = (t1 >= 2 and t1 <= 4)
    
    if condicion_1 and condicion_2 and condicion_3 and condicion_4 and condicion_5:
        total = t[0]*t5+t[1]*t4+t[2]*t3+t[3]*t2+t[4]*t1
        print(f'{count}). ', t5, t4, t3, t2, t1, f'={total}')
        count += 1
