class Error(Exception):
    pass
    """Base class for other exceptions"""
class ValueGreaterThan74(Error):
    pass
    """raised when columns are more than A074"""
    def PreProcessing1(self,df_in,df_ref):
        self.df_in = df_in
        self.df_ref = df_ref
        try:
            for i in self.df_in.iloc[:,5:].columns:
                if i in self.df_ref.iloc[:,5:].columns:
                    pass
                else:
                    raise ValueGreaterThan74

        except ValueGreaterThan74 as V:
            print("columns are more than A074,please check"+str(V))
        except Exception as e:
            print("Error in the ValueGreaterThan74 Class:  "+str(e))

class DuplicatesInColumns(Error):
    pass
    """raised when duplicate columns exist"""

    def PreProcessing2(self,df_in):
        self.df_in=df_in


        try:
            e = self.df_in.columns.tolist()
            for i in e:                 #checking for duplicate columns
                f = e.count(i)
                if f > 1:
                    raise DuplicatesInColumns
                else:
                    pass
        except DuplicatesInColumns as D:
            print(f'{f} has encountered more than one time:  '+str(D))
        except Exception as e:
            print("Error in the DuplicatesInColumns Class:  "+str(e))

class ColumnsError(Error):
    pass
    """Raised when any Assy,Var,Code,Model are missing in the input file"""


    def PreProcessing_Checking_Columns(self, df_in):
        self.df_in = df_in


        try:
            df_in1 = self.df_in.iloc[:, 0:5]
            columns_df_in1 = df_in1.columns.tolist()
            if "Assy" not in columns_df_in1:
                raise ColumnsError
            elif "Model" not in columns_df_in1:
                raise ColumnsError
            elif "Var" not in columns_df_in1:
                raise ColumnsError
            elif "Code" not in columns_df_in1:
                raise ColumnsError
            else:
                pass
        except ColumnsError as C:
            print("Error in PreProcessing_Checking_Columns function i.e column is missing "+str(C))
        except Exception as E:
            print("Error occured in the PreProcessing_Checking_Columns function")
