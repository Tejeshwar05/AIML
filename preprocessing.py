import pandas as pd
import numpy as np



class preprocessing:
    def __init__(self):
        pass


    def PreProcessing(self,df_in,df_rf):
        self.df_in=df_in
        self.df_ref=df_rf

        try:

            df_in1 = self.df_in.iloc[:, 5:]
            df_ref2 = self.df_ref.iloc[:, 5:]
            # df_in1.drop(["A004"],axis=1,inplace=True)
            columns_df_in1 = df_in1.columns.tolist()
            df_ref3 = df_ref2[columns_df_in1] # keeping input and ref columns same
            # df_ref3
            df_ref_first_half = self.df_ref.iloc[:, :5]
            # final=df_first_half+df_ref3
            df_ref_final = pd.concat([df_ref_first_half, df_ref3], axis=1)
            # df_ref_final
            df_in_first_half = self.df_in.iloc[:, :5]
            # final_in=df_in7+df_in1
            df_in_final = pd.concat([df_in_first_half, df_in1], axis=1)
            # df_in_final
            index_Assy = df_in_final.loc[df_in_final["Assy"].isna()].index #droping the rows where NaN are present in Assy and Model
            df_in_final.drop(index_Assy, inplace=True)
            index_Model = df_in_final.loc[df_in_final["Model"].isna()].index
            df_in_final.drop(index_Model, inplace=True)


            df_input = df_in_final.copy()
            df_ref = df_ref_final.copy()

            return df_input,df_ref
        except FileNotFoundError as F:
            print("Error in reading the file in PreProcessing function:   "+str(F))
        except Exception as e:
            print("Error occured in the PreProcessing function:  "+str(e))
        finally:
            print("preprcoessing completed")



