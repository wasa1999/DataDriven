import numpy as np
import pandas as pd


data1 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_A_1.csv'));
data2 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_A_2.csv'));
data3 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_A_3.csv'));
data4 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_A_4.csv'));
data5 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_A_5.csv'));
data6 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_A_6.csv'));
data7 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_A_7.csv'));
data8 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_A_8.csv'));
data9 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_A_9.csv'));
data10 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_A_10.csv'));
data11 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_B_1.csv'));
data12 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_B_2.csv'));
data13 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_C_1.csv'));
data14 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_C_2.csv'));
data15 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_C_3.csv'));
data16 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_C_4.csv'));
data17 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_C_5.csv'));
data18 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_C_6.csv'));
data19 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_C_7.csv'));
data20 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_C_8.csv'));
data21 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_C_9.csv'));
data22 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_C_10.csv'));
data23 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_C_11.csv'));
data24 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_D_1.csv'));
data25 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_D_2.csv'));
data26 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_D_3.csv'));
data27 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_D_4.csv'));
data28 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_D_5.csv'));
data29 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_D_6.csv'));
data30 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_D_7.csv'));
data31 = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/data_E_1.csv'));

data_all = pd.merge(data1,data2,on=['date','time']);
data_all = pd.merge(data_all,data3,on=['date','time']);
data_all = pd.merge(data_all,data4,on=['date','time']);
data_all = pd.merge(data_all,data5,on=['date','time']);
data_all = pd.merge(data_all,data6,on=['date','time']);
data_all = pd.merge(data_all,data7,on=['date','time']);
data_all = pd.merge(data_all,data8,on=['date','time']);
data_all = pd.merge(data_all,data9,on=['date','time']);
data_all = pd.merge(data_all,data10,on=['date','time']);
data_all = pd.merge(data_all,data11,on=['date','time']);
data_all = pd.merge(data_all,data12,on=['date','time']);
data_all = pd.merge(data_all,data13,on=['date','time']);
data_all = pd.merge(data_all,data14,on=['date','time']);
data_all = pd.merge(data_all,data15,on=['date','time']);
data_all = pd.merge(data_all,data16,on=['date','time']);
data_all = pd.merge(data_all,data17,on=['date','time']);
data_all = pd.merge(data_all,data18,on=['date','time']);
data_all = pd.merge(data_all,data19,on=['date','time']);
data_all = pd.merge(data_all,data20,on=['date','time']);
data_all = pd.merge(data_all,data21,on=['date','time']);
data_all = pd.merge(data_all,data22,on=['date','time']);
data_all = pd.merge(data_all,data23,on=['date','time']);
data_all = pd.merge(data_all,data24,on=['date','time']);
data_all = pd.merge(data_all,data25,on=['date','time']);
data_all = pd.merge(data_all,data26,on=['date','time']);
data_all = pd.merge(data_all,data27,on=['date','time']);
data_all = pd.merge(data_all,data28,on=['date','time']);
data_all = pd.merge(data_all,data29,on=['date','time']);
data_all = pd.merge(data_all,data30,on=['date','time']);
data_all = pd.merge(data_all,data31,on=['date','time']);



df_walkdata = data_all.copy();
df_new = df_walkdata.drop(['date','time'],axis=1);




def makeNdarray(index):
    npdata = df_new.iloc[:,index];
    return npdata;

def calSimilality(data1,data2,ws,contime,bunbosize,limit):
    unsimilality = np.zeros(len(data1) - ws + 1)
    bunshi = (data1-data2)**2
    bunshi_t = np.zeros(len(data1) - ws + 1)
    bunbo = data1**2 + data2**2
    bunbo_t = np.zeros(len(data1) - ws + 1)
    for i in range(0, len(data1) - ws + 1):
        bunbo_t[i] = np.sum(bunbo[i:i+ws])
        if bunbo_t[i] > 0:
            unsimilality[i] = np.sum(bunshi[i:i+ws]) / bunbo_t[i]
            # print("now is " + str(i) + " , unsimilality is " + str(i))
        else:

            unsimilality[i] = 1.0;
            # print("now is " + str(i) + " , unsimilality is " + str(i))

    # print(bunbo_t.size)


    similality = np.zeros(len(unsimilality) - contime + 1)

    for t in range(len(similality)):
        # print("bunbo_t is " + str(bunbo_t))
        if bunbo_t[t] > bunbosize:
            # print(str(t) + " is enough big!")
            buffer = unsimilality[t:t+contime]
            buffer = buffer < 0.05
            # print(buffer)
            if (buffer.all() == True):
                similality[t] = 1;

    return similality;



if __name__ == '__main__':

    res = np.zeros((31,31))
    for i in range(31):
        for j in range(31):
            res[i,j] = np.sum(calSimilality(makeNdarray(i),makeNdarray(j),60,15,10000,0.05))
            print("the similality between " + str(i) + " and " + str(j) + " is " + str(res[i,j]));

    df_res = pd.DataFrame(res);
    print(df_res)




    df_res.to_csv('/Users/Tomoya_Iwasaki/Desktop/data/resultA1_E1.csv');

    # for i in range(len(show)):
    #     print(show[1])
