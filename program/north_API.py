# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 16:13:37 2023

@author: User
"""

import pandas as pd
import os
from datetime import datetime, timedelta

now = datetime.now()
yday = now - timedelta(days = 1)
today = now.strftime("%Y%m%d")
yesterday = yday.strftime("%Y%m%d") 

path = rf"C:\Users\User\Desktop\North_auto\yday_accumulate\{today}"

if os.path.exists(path):
    
    os.chdir(path)

else:
    
    os.mkdir(path)
    os.chdir(path)

url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0002-001?Authorization=rdec-key-123-45678-011121314'

raw_data = pd.read_json(url)
 
station = raw_data.records.Station

station_id = [
    {'stat_id' : 'L1A820', 'precip' : None},  # 石碇(十三股)
    {'stat_id' : 'C0A530', 'precip' : None},  # 坪林-碧湖(坪林)
    {'stat_id' : 'C0A930', 'precip' : None},  # 金山(三和)
    {'stat_id' : 'C0B010', 'precip' : None},  # 七堵(現場監測)
    {'stat_id' : '466940', 'precip' : None},  # 碧砂漁港(基隆)
    {'stat_id' : 'C0A950', 'precip' : None},  # 瑞濱-鼻頭(鼻頭角)
    {'stat_id' : 'C0A970', 'precip' : None},  # 貢寮卯澳(三貂角)
    {'stat_id' : 'C0A890', 'precip' : None},  # 龍門橋(雙溪)
    {'stat_id' : 'C0AC60', 'precip' : None},  # 三峽(三峽)
    {'stat_id' : 'C0A570', 'precip' : None},  # 烏來(桶後)
    {'stat_id' : '01C570', 'precip' : None},  # 桃園迴龍-龜山(龍壽社區)
    {'stat_id' : '21C080', 'precip' : None},  # 羅浮-巴陵(高義)
    {'stat_id' : '21C070', 'precip' : None},  # 巴陵-西村(巴陵)
    {'stat_id' : '01A210', 'precip' : None},  # 新峰(大豹)
    {'stat_id' : 'C0AD10', 'precip' : None},  # 八里(八里)
    {'stat_id' : 'C0C590', 'precip' : None},  # 觀音(觀音)
    {'stat_id' : '01C400', 'precip' : None},  # 溪州(石門後池)
    {'stat_id' : 'C0D700', 'precip' : None}   # 關西(關西)
    ]


for id_s in station_id:
    
    for stat in station:
        
        if id_s["stat_id"] == stat["StationId"]:
            
            now_prep = stat["RainfallElement"]["Now"]["Precipitation"]
            yday_prep = stat["RainfallElement"]["Past2days"]["Precipitation"]
            id_s["precip"] = yday_prep - now_prep
            

road_station = {"L1A820(石碇)" : None,  # 石碇(十三股)
                "C0A530(坪林-碧湖)" : None,  # 坪林-碧湖(坪林)
                "C0A930(金山)" : None,  # 金山(三和)
                "C0B010(七堵)" : None,  # 七堵(現場監測)
                "466940(碧砂漁港)" : None,  # 碧砂漁港(基隆)
                "C0A950(瑞濱-鼻頭)" : None,  # 瑞濱-鼻頭(鼻頭角)
                "C0A970(貢寮卯澳)" : None,  # 貢寮卯澳(三貂角)
                "C0A890(龍門橋)" : None,  # 龍門橋(雙溪)
                "C0AC60(三峽)" : None,  # 三峽(三峽)
                "C0A570(烏來)" : None,  # 烏來(桶後)
                "C0A570(烏來02)" : None,  # 烏來02(桶後)
                "C0A570(上龜山橋)" : None,  # 上龜山橋(桶後)
                "01C570(桃園迴龍-龜山)" : None,  # 桃園迴龍-龜山(龍壽社區)
                "01C570(桃園迴龍-嶺頂)" : None,  # 桃園迴龍-嶺頂(龍壽社區)
                "21C070(羅浮-巴陵)" : None,  # 羅浮-巴陵(巴陵)
                "21C080(羅浮-巴陵)" : None,  # 羅浮-巴陵(高義)
                "21C070(巴陵-西村)" : None,  # 巴陵-西村(巴陵)
                "01A210(新峰)" : None,  # 新峰(大豹)
                "C0A970(浪襲路段)" : None,  # 浪襲路段(三貂角)
                "C0A930(陽明山-金山)" : None,  # 陽明山-金山(三和)
                "C0AD10(八里)" : None,  # 八里(八里)
                "C0C590(草漯)" : None,  # 草漯(觀音)
                "C0C590(觀音)" : None,  # 觀音(觀音)
                "21C070(大曼)" : None,  # 大曼(巴陵)
                "01C400(溪州)" : None,  # 溪州(石門後池)
                "C0D700(關西)" : None   # 關西(關西)
                }


for i in road_station.keys():
    
    for j in station_id:
        
        if j["stat_id"] == i[0:6]:
            
            road_station[i] = j["precip"]
            
            
data_list = []
index_list = []

for i in road_station:
    
    index_list.append(i)
    data_list.append(road_station[i])


data = pd.DataFrame(data_list, index = index_list, columns = ["昨日累積雨量"])

data.to_csv(f"{yesterday}_累積雨量.csv", encoding = "big5")




