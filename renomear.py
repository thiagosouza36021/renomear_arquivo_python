import os
from datetime import datetime

folder = r'C:\Users\thiago.thomaz\OneDrive - GRUPOCARD COMERCIO DE CARTOES TELEFONICOS LTDA\Area de Qualidade\PROJETO MELHORIAS NOVO DP\SharePoint\\'
data_atual = datetime.now()
data_dia = data_atual.day
data_mes = data_atual.month
data_ano = data_atual.year

for file_name in os.listdir(folder):
    old_name = folder + file_name
    new_name = folder + str (data_dia)+'_'+str(data_mes)+'_'+str(data_ano) +' '+ file_name
    os.rename(old_name, new_name) 

print(os.listdir(folder))   