import csv

DIODE_CURVE = 'Meta,TestnameAgain,01.Diode_Drain'

file = open('data-test.csv','r')
list_of_list = file.readlines()
file.close()

fourth_element_in_array = list_of_list[3].strip()

def csv_from_diode(list_arr):
    with open('temp.csv','w') as f:
        # writer = csv.writer(f)
        for i in range(6, len(list_arr)):
            f.writelines(list_arr[i])
    f.close()

if DIODE_CURVE == fourth_element_in_array:
    csv_from_diode(list_of_list)