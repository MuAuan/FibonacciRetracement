import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import datetime as dt
import statsmodels.api as sm
from statsmodels.tsa.seasonal import STL
import pandas_datareader.data as DataReader

stock0='ZARJPY=X'  #'USDJPY=X' #'EURJPY=X' #AUDJPY=X JPYAUD=X ZARJPY=X GBPJPY=X JPYUSD=X
bunseki = "trend"
start = dt.date(2019,4,1)
end = dt.date(2020,8,14)

df=DataReader.get_data_yahoo("{}".format(stock0),start,end) 
print(df)

series=df['Close']
cycle, trend = sm.tsa.filters.hpfilter(series, 144)
df['trend']=  trend
f_ratio = 0.5 #0.6180339887498949
f_ratio2 = 1/3

def MAX_(x):
    return pd.Series(x).max()
def MIN_(x):
    return pd.Series(x).min()
def M618_(x, n):
    # 下限値と上限値の間のリトレースメントを求める
    f = 1
    for i in range(0,n,1):
        f *= f_ratio
    m618 = pd.Series(x).min() + f*(pd.Series(x).max()-pd.Series(x).min())
    return m618
def M618_2(x, n):
    # 下限値以下のリトレースメントを求める
    f = 1
    for i in range(0,n,1):
        f *= f_ratio
    m618 = pd.Series(x).min() - f*(pd.Series(x).max()-pd.Series(x).min())
    return m618
def M618_1(x, n):
    # 上限値近傍のリトレースメントを求める
    f = 1
    for i in range(0,n,1):
        f *= f_ratio
    m618 = pd.Series(x).max() - f*(pd.Series(x).max()-pd.Series(x).min())
    return m618
def M50_(x, n):
    # 50％のリトレースメントを求める
    f = 1
    for i in range(0,n,1):
        f *= 0.5
    m618 = pd.Series(x).max() - f*(pd.Series(x).max()-pd.Series(x).min())
    return m618
def M50_1(x, n):
    # 下限値以下のさらに50％のリトレースメントを求める
    f = 1
    for i in range(0,n,1):
        f *= 0.5
    m618 = pd.Series(x).min() - f*(pd.Series(x).max()-pd.Series(x).min())
    return m618
def M33_(x, n):
    # 1/3のリトレースメントを求める
    f = 1
    for i in range(0,n,1):
        f *= 1/3
    m618 = pd.Series(x).max() - f*(pd.Series(x).max()-pd.Series(x).min())
    return m618
def M66_(x, n):
    # 2/3のリトレースメントを求める
    f = 1
    for i in range(0,n,1):
        f *= 2/3
    m618 = pd.Series(x).max() - f*(pd.Series(x).max()-pd.Series(x).min())
    return m618
def M33_1(x, n):
    # 下限値以下のさらに1/3リトレースメントを求める
    f = 1
    for i in range(0,n,1):
        f *= 1/3
    m618 = pd.Series(x).min() - f*(pd.Series(x).max()-pd.Series(x).min())
    return m618


series2 = df['trend'].values.tolist()
print(series2[len(series2)-10:len(series2)])
m = 1/2 # 上限値、下限値を求めるデータ範囲；全データ辺りの割合
df['Close']=series  #series" #cycle" #trend
df['Close2']=series2
df['max'] = MAX_(df['Close'][:int(len(series)*m)])
df['min'] = MIN_(df['Close'][:int(len(series)*m)])
print('min',df['min'])
df['m50'] = M50_(df['Close'][:int(len(series)*m)],1)
df['m50_1'] = M50_1(df['Close'][:int(len(series)*m)],1)
print('m50_1',df['m50_1'])

df['m33_'] = M33_(df['Close'][:int(len(series)*m)],1)
df['m66_'] = M66_(df['Close'][:int(len(series)*m)],1)

# 上限値近傍のリトレースメントを求める
df['m618_2'] = M618_1(df['Close'][:int(len(series)*m)],2)
df['m618_3'] = M618_1(df['Close'][:int(len(series)*m)],3)
df['m618_4'] = M618_1(df['Close'][:int(len(series)*m)],4)
df['m618_5'] = M618_1(df['Close'][:int(len(series)*m)],5)

# 下限値以下のリトレースメントを求める
df['m618_20'] = M618_2(df['Close'][:int(len(series)*m)],0)
print(df['m618_20'])
df['m618_21'] = M618_2(df['Close'][:int(len(series)*m)],1)
print(df['m618_21'])
df['m618_22'] = M618_2(df['Close'][:int(len(series)*m)],2)
print(df['m618_22'])
df['m618_23'] = M618_2(df['Close'][:int(len(series)*m)],3)
print(df['m618_23'])
df['m618_24'] = M618_2(df['Close'][:int(len(series)*m)],4)
print(df['m618_24'])

# 下限値と上限値の間のリトレースメントを求める
df['m618'] = M618_(df['Close'][:int(len(series)*m)],1)
df['m618d'] = M618_(df['Close'][:int(len(series)*m)],2)
df['m618t'] = M618_(df['Close'][:int(len(series)*m)],3)
df['m618q'] = M618_(df['Close'][:int(len(series)*m)],4)
df['m618q5'] = M618_(df['Close'][:int(len(series)*m)],5)
df['m618q6'] = M618_(df['Close'][:int(len(series)*m)],6)

date_df=df['Close'].index.tolist()
print(df[len(series)-10:len(series)])

fig, ax1 = plt.subplots(1,1,figsize=(1.6180 * 8, 8*1),dpi=200)
ax1.plot(df['Close'],label="series")
ax1.plot(df['Close2'],label="series2")
ax1.plot(df['max'],label="max")
ax1.plot(df['min'],'black',label="min")

ax1.plot(df['m618_2'],label="m618_2")
ax1.plot(df['m618_3'],label="m618_3")
ax1.plot(df['m618_4'],label="m618_4")
ax1.plot(df['m618_5'],label="m618_5")

ax1.plot(df['m618_20'],label="m618_20")
ax1.plot(df['m618_21'],label="m618_21")
ax1.plot(df['m618_22'],label="m618_22")
ax1.plot(df['m618_23'],label="m618_23")
ax1.plot(df['m618_24'],label="m618_24")

ax1.plot(df['m618'],label="m618")
ax1.plot(df['m618d'],label="m618d")
ax1.plot(df['m618t'],label="m618t")
ax1.plot(df['m618q'],label="m618q")
ax1.plot(df['m618q5'],label="m618q5")
ax1.plot(df['m618q6'],label="m618q6")

ax1.plot(df['m50'],'blue',label="m50")
ax1.plot(df['m50_1'],'blue',label="m50_1")
ax1.plot(df['m33_'],'red',label="m33_")
ax1.plot(df['m66_'],'green',label="m66_")


ax1.set_title("{}".format(stock0))
ax1.legend()
ax1.set_ylim(5,)
#ax1.grid()
plt.savefig("./fx/fx_{}_ema_df_decompose_{}_{}ratio{}.png".format(stock0,start,end,m))
plt.pause(1)
plt.close()