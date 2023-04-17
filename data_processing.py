
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
from scipy.interpolate import splrep, splev
def voltage_curve_experiment(nr_cycle,path,theoretical_capacity):
    data1=pd.read_excel(path)
    # j=0
    # while data1['Column1'][j]!='channel_index':
    #     j+=1


    channel_index_row=data1[data1.apply(lambda row:'channel_index' in str(row.values),axis=1)].index[0]
    #data1.columns.values[:]=data1.iloc[6][:]
    data1.columns=data1.iloc[channel_index_row]
    data1=data1.drop(channel_index_row)

    #data1.columns.values[:]=data1.iloc[6][:]
    #df1=pd.DataFrame(data1[10:])
    #for i in range(0,len(data1)):
    df1=data1.loc[data1['cycle_index']==nr_cycle]
    #data1.columns(data1.iloc[6])

    df1['discharge_capacity_Ah']=df1['discharge_capacity_Ah'].astype(float)
    df1['voltage_V']=df1['voltage_V'].astype(float)

    # find the row containing the value 3.8 in any column
    #start = df1.loc[(df1 == 3.8).any(axis=1)]
    # start = df1.loc[(df1['voltage_V'] >= 3.43) & (df1['voltage_V'] <= 3.45)]
    # st=start.index[0]
    df1=df1.loc[df1['voltage_V'] <= 3.45]
    #df1.set_index('channel_index', inplace=True)
    st=0
    
    while (df1['step_name'].iloc[st] != 'rest'):
        st+=1

    end=st


    x=df1['discharge_capacity_Ah'].iloc[0:end]
    y=df1['voltage_V'].iloc[0:end]
    avg_cap=0
    avg_vol=0
    l=0
    cap=[]
    voltage=[]
    for i in range(1,len(x)):
        if x.iloc[i]==x.iloc[i-1]:
            avg_cap=avg_cap+x.iloc[i]
            avg_vol=avg_vol + y.iloc[i]
            l=l+1
        else:
            if l==0:
                cap.append(x.iloc[i])
                voltage.append(y.iloc[i])
            else:
                cap.append(avg_cap/l)
                voltage.append(avg_vol/l)
            avg_cap=0
            avg_vol=0
            l=0



    for i in range(0,len(cap)):
        cap[i]=cap[i]/theoretical_capacity

    cap=np.array(cap)
    voltage=np.array(voltage)
    return cap,voltage

cap, voltage=voltage_curve_experiment('5','C:/Users/dhmht/Desktop/Thesis_files/experiments/data_1st_exp_nogf_1c/DMT_77_EXC.xlsx',0.0025)
cap2, voltage2=voltage_curve_experiment('6','C:/Users/dhmht/Desktop/Thesis_files/experiments/data_1st_exp_nogf_1c/DMT_77_EXC.xlsx',0.0025)
#cap3 , voltage3 = voltage_curve_experiment(5,'C:/Users/dhmht/Desktop/Thesis_files/experiments/DATA_ECDMC_NOGF_10DEGC_2MAH/DMTP_NOGF_cycle5and6_ex.xlsx',0.0025)

# x2=df1['discharge_capacity_Ah'].iloc[2300:2978]
# y2=df1['voltage_V'].iloc[2300:2978]

# avg_cap2=0
# avg_vol2=0
# k2=0
# cap2=[]
# voltage2=[]
# for i in range(1,len(x2)):
#     if x2.iloc[i]==x2.iloc[i-1]:
#         avg_cap2=avg_cap2+x2.iloc[i]
#         avg_vol2=avg_vol2 + y2.iloc[i]
#         k2=k2+1
#     else:
#         if k2==0:
#             cap2.append(x2.iloc[i])
#             voltage2.append(y2.iloc[i])
#         else:
#             cap2.append(avg_cap2/k2)
#             voltage2.append(avg_vol2/k2)

#     avg_cap2=0
#     avg_vol2=0
#     k2=0


# #cap2.insert(0,df1['discharge_capacity_Ah'].iloc[2300])
# for i in range(0,len(cap2)):
#     cap2[i]=cap2[i]/0.0025
# #voltage2.insert(0,df1['voltage_V'].iloc[2301])
# cap2=np.array(cap2)
# voltage2=np.array(voltage2)
#f = interp1d(df1_avg_col9, df1_avg_col8, kind='cubic')
# spl = splrep(x, y, k=2, s=0)
# x_new = np.linspace(0, 0.00025, len(spl[0]))
# y_new=splev(x_new, spl)
#plt.scatter(x, y, label='Data')
#plt.scatter(x2, y2, label='Data2',color='green')

#plt.plot(x_new, y_new, label='Spline fit')
plt.plot(cap,voltage,label='Spline fit',color='red')
plt.plot(cap2,voltage2,label='Spline fit',color='blue')
#plt.plot(cap3,voltage3,label='Spline fit',color='blue')
plt.legend()
plt.show()

#plt.plot(df1['Column9'].iloc[63:740], df1['Column8'].iloc[63:740])
plt.show()
print(voltage3,cap3)




