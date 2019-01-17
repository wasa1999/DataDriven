import numpy as np
import pandas as pd
import math


#データフレームの作成

data_all = pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/dd_hw/original.csv')
data_days = pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/dd_hw/ele_days.csv')
data_holi = pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/dd_hw/ele_holi.csv')


##各党の検索数をを平日、休日、両方で分ける
df_all = pd.DataFrame(data_all);
df_days = pd.DataFrame(data_days)
df_holi = pd.DataFrame(data_holi)

df_zimin_days = df_days.query('政党 == "自由民主党"')
df_minshu_days = df_days.query('政党 == "民主党"')
df_komei_days = df_days.query('政党 == "公明党"')
df_isin_days = df_days.query('政党 == "維新の党"')
df_kyosan_days = df_days.query('政党 == "日本共産党"')
df_shamin_days = df_days.query('政党 == "社会民主党"')


df_zimin_holi = df_holi.query('政党 == "自由民主党"')
df_minshu_holi = df_holi.query('政党 == "民主党"')
df_komei_holi = df_holi.query('政党 == "公明党"')
df_isin_holi = df_holi.query('政党 == "維新の党"')
df_kyosan_holi = df_holi.query('政党 == "日本共産党"')
df_shamin_holi = df_holi.query('政党 == "社会民主党"')


df_zimin_all = df_all.query('政党 == "自由民主党"')
df_minshu_all = df_all.query('政党 == "民主党"')
df_komei_all = df_all.query('政党 == "公明党"')
df_isin_all = df_all.query('政党 == "維新の党"')
df_kyosan_all = df_all.query('政党 == "日本共産党"')
df_shamin_all = df_all.query('政党 == "社会民主党"')


row = ['A1','A2','A3','A4','A5','A6','A7','B1','B2','B3','B4','B5','B6','B7','C1','C2','C3','C4','C5','C6','C7','C8','D1','D2','D3','D4','D5','D6','D7','E1','E2','E3','E4','E5','E6','E7','E8','E9','F1','F2','F3','F4','F5','F6','F7']
col = ['自由民主党','民主党','公明党','維新の党','日本共産党','社会民主党']
final_df = pd.DataFrame(0, index=row, columns = col);
final_holi_df = pd.DataFrame(0, index=row, columns = col);
final_all_df = pd.DataFrame(0, index=row, columns = col);


days_list = [df_zimin_days, df_minshu_days, df_komei_days, df_isin_days, df_kyosan_days, df_shamin_days];
holi_list = [df_zimin_holi, df_minshu_holi, df_komei_holi, df_isin_holi, df_kyosan_holi, df_shamin_holi]
all_list = [df_zimin_all, df_minshu_all, df_komei_all, df_isin_all, df_kyosan_all, df_shamin_all]


# 選挙区別の各党の検索数を抽出する関数

def extractDayData(df, key):
    keysum = 0;
    for i in range(len(df['日付'])):
        if( df.at[df.index[i], '選挙区'] == key ):
            keysum += df.at[df.index[i], '検索数']
    return keysum;


for i in range(len(col)):
    for j in range(len(row)):
        final_df.iloc[j,i] = extractDayData(days_list[i], row[j])

for i in range(len(col)):
    for j in range(len(row)):
        final_holi_df.iloc[j,i] = extractDayData(holi_list[i], row[j])

for i in range(len(col)):
    for j in range(len(row)):
        final_all_df.iloc[j,i] = extractDayData(all_list[i], row[j])



#csvファイルにしておく
data_res = pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/dd_hw/res.csv')
final_df.to_csv('/Users/Tomoya_Iwasaki/Desktop/final_df_latest.csv')
data_res.to_csv('/Users/Tomoya_Iwasaki/Desktop/data_res_latest.csv')
final_holi_df.to_csv('/Users/Tomoya_Iwasaki/Desktop/final_holi_df_latest.csv')
final_all_df.to_csv('/Users/Tomoya_Iwasaki/Desktop/final_all_df_latest.csv')


#　エクセルで編集したデータ（選挙区別の各党の検索数と得票数）
data_cor = pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/cor.csv')

# 選挙区ごとに検索数を合計する関数

def exRegion(df):
    searchSum = [0,0,0,0,0,0,0];
    for i in range(len(df['選挙区'])):
        region = df.at[df.index[i], '選挙区'] ;
        if (region == 'B1'):
            searchSum[0] += df.at[df.index[i], '検索数'] ;
        elif (region == 'B2'):
            searchSum[1] += df.at[df.index[i], '検索数'] ;
        elif (region == 'B3'):
            searchSum[2] += df.at[df.index[i], '検索数'] ;
        elif (region == 'B4'):
            searchSum[3] += df.at[df.index[i], '検索数'] ;
        elif (region == 'B5'):
            searchSum[4] += df.at[df.index[i], '検索数'] ;
        elif (region == 'B6'):
            searchSum[5] += df.at[df.index[i], '検索数'] ;
        elif (region == 'B7'):
            searchSum[6] += df.at[df.index[i], '検索数'] ;

    return searchSum;

zimin = exRegion(df_f_zimin);
minshu = exRegion(df_f_minshu);
isin = exRegion(df_f_komei) ;
komei = exRegion(df_f_isin);
kyosan = exRegion(df_f_kyosan);
shamin = exRegion(df_f_shamin);

df_predict = pd.DataFrame({ '自由民主党' : zimin,
                        '民主党' : minshu,
                        '維新の党' : isin,
                        '公明党' : komei,
                        '日本共産党' : kyosan,
                        '社会民主党' : shamin })


# 各政党の得票数予測に用いる回帰式の定義（回帰式の導出はエクセル）

def zimin_cal(x):
    answer = 447548 * math.log(x) - 4000000
    return answer

def minshu_cal(x):
    answer = 221670 * math.log(x) - 2000000
    return answer

def isin_cal(x):
    answer = 111730 * math.log(x) - 873432
    return answer

def kyosan_cal(x):
    answer = 160563 * math.log(x) - 1000000
    return answer

def other_cal(x):
    answer = 12628 * math.exp(0.0001 * x)
    return answer


for i in range(len(zimin)):
    zimin[i] = zimin_cal(zimin[i])

print("zimin")
print(zimin)


for i in range(len(minshu)):
    minshu[i] = minshu_cal(minshu[i])

print("minshu")
print(minshu)

for i in range(len(isin)):
    isin[i] = isin_cal(isin[i])


print("isin")
print(isin)

for i in range(len(komei)):
    komei[i] = other_cal(komei[i])


print("komei")
print(komei)

for i in range(len(kyosan)):
    kyosan[i] = kyosan_cal(kyosan[i])


print("kyosan")

print(kyosan)

for i in range(len(shamin)):
    shamin[i] = other_cal(shamin[i])

print("shamin")

print(shamin)
