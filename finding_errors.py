import pandas as pd
import numpy as np
class error:
    def __init__(self):
        pass

    def unique_actual(self,df):
        self.df=df
        try:

            self.df["Code"].replace(np.nan, 9999, inplace=True)
            self.df["Var"].replace(np.nan, 9999, inplace=True)
            self.df["Code"] = self.df["Code"].astype(int)
            self.df["Var"] = self.df["Var"].astype(int)
            self.df["Combi"] = self.df["Assy"].astype(str) + "00" + self.df["Model"].astype(str) + "00" + self.df["Var"].astype(str) + "00" + self.df[
                "Code"].astype(str)
            df2 = self.df["Combi"]
            self.df.insert(0, "Comb_key", df2)
            self.df.drop(columns=["ID", "Combi"], inplace=True, axis=1)
            # df_comb_actual=df.drop_duplicates(subset=["Combination"])
            df_comb_actual = self.df
            return df_comb_actual
        except NameError as N:
            print("Error occured in the unique actual function"+str(N))
        except Exception as E:
            print("Error occured in making the combination key of input excel file unique actual function:   "+str(E))
        finally:
            print("making combination key in input excel file is done")


    def error_a(self,df_a):
        # this checks whether the Code of  null, containing 2 in data columns
        self.df_a=df_a
        try:

            listOfPos1 = []
            df10 = self.df_a.iloc[:, 5:]
            result = df10.isin([2])
            seriesObj = result.any()
            columnNames = list(seriesObj[seriesObj == True].index)
            for col in columnNames:
                rows = list(result[col][result[col] == True].index)
                flag = "type error 'a' "
                for row in rows:
                    listOfPos1.append((row, col, flag))
                    df_samp_null = pd.DataFrame(listOfPos1, columns=["row", "col", "error"])
            return df_samp_null
        except NameError as N:
            print("Error occured in the error_a function"+str(N))
        except Exception as E:
            print("Error occured in the error_a function"+str(E))



    def error_b(self,df_b):
        # this checks whether the Code of not null, containing 0 in in data columns
        self.df_b=df_b
        try:

            listOfPos2 = []
            df11 = self.df_b.iloc[:, 5:]
            result = df11.isin([0])
            seriesObj = result.any()
            columnNames = list(seriesObj[seriesObj == True].index)
            for col in columnNames:
                rows = list(result[col][result[col] == True].index)
                flag = "type error 'b' "
                for row in rows:
                    listOfPos2.append((row, col, flag))
                    df_samp_not_null = pd.DataFrame(listOfPos2, columns=["row", "col", "error"])
            return df_samp_not_null

        except NameError as N:
            print("Error occured in the error_b function"+str(N))
        except Exception as E:
            print("Error occured in the error_b function"+str(E))

    def error_cdef(self,df_actual_comb, df_samp_comb):
        self.df_actual_comb=df_actual_comb
        self.df_samp_comb=df_samp_comb
        try:

            self.df_actual_comb.drop(["Assy", "Model", "Var", "Code"], axis=1, inplace=True)
            self.df_actual_comb.replace(0, 1, inplace=True)
            self.df_actual_comb.replace(np.nan, 0, inplace=True)
            self.df_samp_comb.drop(["Assy", "Model", "Var", "Code"], axis=1, inplace=True)
            self.df_samp_comb.replace(0, 1, inplace=True)
            self.df_samp_comb.replace(np.nan, 0, inplace=True)
            indexs = 0
            lst = []
            for values in self.df_actual_comb["Comb_key"]:


                df_actual_comb_series = self.df_actual_comb.loc[indexs, :]
                df_actuall = pd.DataFrame([df_actual_comb_series])
                df_actuall_ = df_actuall.drop(["Comb_key"], axis=1)
                df_actuall_temp = df_actuall_.astype(float)
                df_int = self.df_samp_comb.loc[self.df_samp_comb["Comb_key"] == values]
                df_int_ = df_int.drop(["Comb_key"], axis=1)
                for i in df_int_.index:
                    df_diff = df_int_.loc[i, :].subtract(df_actuall_temp)
                    for col in df_diff.columns:
                        if 1 in df_diff[col].values:
                            row = i
                            flag = "Error C"
                            lst.append([row, col, flag])
                            df_cdef = pd.DataFrame(lst, columns=["row", "col", "error"])
                        elif -1 in df_diff[col].values:
                            row = i
                            flag = "Error D"
                            lst.append([row, col, flag])
                            df_cdef = pd.DataFrame(lst, columns=["row", "col", "error"])
                        elif 2 in df_diff[col].values:
                            row = i
                            flag = "Error E"
                            lst.append([row, col, flag])
                            df_cdef = pd.DataFrame(lst, columns=["row", "col", "error"])
                        elif -2 in df_diff[col].values:
                            row = i
                            flag = "Error F"
                            lst.append([row, col, flag])
                            df_cdef = pd.DataFrame(lst, columns=["row", "col", "error"])
                        else:
                            pass
                indexs+=1
            return df_cdef

        except Exception as E:
            print("Error occured in the error_cdef function" + str(E))
