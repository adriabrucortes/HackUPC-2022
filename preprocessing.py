# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:59:54 2022

@author: berna
"""

import pandas as pd
import numpy as np
from dateutil import rrule
import datetime
from dateutil.relativedelta import relativedelta

sku_dir = '../DATA_sale/sku.csv'
sales_dir = '../DATA_sale/sales.csv'
geo_dir = '../DATA_sale/geo_params.csv'
test_dir = '../DATA_sale/test.csv'

def read (sku_dir,sales_dir,geo_dir,test_dir):
    # Carrega de les taules
    sku = pd.read_csv(sku_dir)
    sales = pd.read_csv(sales_dir)
    geo = pd.read_csv(geo_dir)
    test = pd.read_csv(test_dir)
    
    sales['date'] = pd.to_datetime(sales['date'])
    
    df = sales.reset_index()    
    df["date"] = pd.to_datetime(df["date"])
    
    df["month"] = df["date"].dt.month
    
    mitja_mesos = df.groupby(["month", "SKU"]).mean()
    mitja_sku = df.groupby("SKU").mean()
    
    for month,s in mitja_mesos.index:
        
        if np.isnan(mitja_mesos['price'][month][s]):
            for s2 in mitja_sku.index:
                if s2 == s:
                    mitja_mesos['price'][month][s] = mitja_sku['price'][s2]
                
            
    
    mitja_mesos.fillna(0)
    
    out_group = pd.DataFrame(mitja_mesos)
    
    new_out = out_group.reset_index()
    
    cosa2 = new_out.copy()
    
    cosa2.drop(columns=['geoCluster','sales','index'],inplace=True)
    
    sales['month'] = sales['date'].dt.month
    merge = pd.merge(sales[pd.isnull(sales['price'])],cosa2,how='left',on=['month','SKU'])
    merge['sales'] = 0
    merge = merge.drop("price_x", axis = 1)
    merge=merge.rename({'price_y':'price'},axis=1)
    merge = merge.drop('date',axis=1)
    sales = sales.drop('date',axis=1)
    sales_not_null = pd.concat([sales[pd.notnull(sales['price'])],merge])
    sales_not_null = pd.merge(sales_not_null, geo, how='left', on='geoCluster')
    sku = sku.drop(['Category','Type',"Units","countryOfOrigin"],axis=1)
    sku = pd.get_dummies(sku, columns=["Group"])
    sku = pd.get_dummies(sku, columns=['trademark'])
    sku = sku.drop(['brandId'],axis=1)
    
    taula_final = pd.merge(sku,sales_not_null,how='left',on='SKU')

    taula_final = taula_final.drop(["SKU","geoCluster"], axis = 1)
    taula_final.to_csv('taula_final_sense_brand.csv')
    
read(sku_dir, sales_dir, geo_dir, test_dir)
