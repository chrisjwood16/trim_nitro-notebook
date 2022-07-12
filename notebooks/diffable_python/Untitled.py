# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
from ebmdatalab import bq
import os

vendors_path=os.path.join('..','data','vendors.csv')
vendors = pd.read_csv(vendors_path)
vendors

# +
sql = '''
SELECT Date, ODS, TRIM(Principal_Supplier) AS supplier FROM `ebmdatalab.alex.vendors`'''

vendors_DF = bq.cached_read(sql, csv_path=os.path.join('..','data','vendorstest.csv'))
vendors_DF
# -


