import pandas as pd
import numpy as np
from preprocessing import preprocessing
from Exceptions import ValueGreaterThan74
from Exceptions import DuplicatesInColumns
from Exceptions import ColumnsError
from finding_errors import error
#from Exceptions import Error

path = pd.read_excel(r'data_ver3_input.xlsx', engine="openpyxl")

def predict(df_in):
    try:

        #df_in = pd.read_excel(r'data_ver3_input.xlsx', engine="openpyxl")
        df_ref = pd.read_excel(r'Output (1).xlsx', engine="openpyxl")

        #e=Error()

        value=ValueGreaterThan74()
        value.PreProcessing1(df_in,df_ref)

        dup=DuplicatesInColumns()
        dup.PreProcessing2(df_in)

        Columns=ColumnsError()
        Columns.PreProcessing_Checking_Columns(df_in)

       # pre.PreProcessing1(df_in)
       # pre.PreProcessing2(df_in)

        pre = preprocessing()
        df_input,df_refer=pre.PreProcessing(df_in,df_ref)

        err=error()
        combi = err.unique_actual(df_input)

        df_a = combi.loc[combi["Code"] == 9999]
        df_b = combi.loc[combi["Code"] != 9999]

        df_null = err.error_a(df_a)
        df_not_null = err.error_b(df_b)
        df1 = df_null.append(df_not_null, ignore_index=True)
        df_cdef=err.error_cdef(df_refer.head(10),combi.head(20))
        df2=df1.append(df_cdef,ignore_index=True)

        return df2
    except Exception as e:
        print("Error occured in the find_error function in main.py:   "+str(e))


error_ = predict(path)
df_final = error_.drop_duplicates(subset=["row", "col"])
df_final.to_csv("ERROR FILE5", index=False)