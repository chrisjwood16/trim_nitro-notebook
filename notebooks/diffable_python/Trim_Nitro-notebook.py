# -*- coding: utf-8 -*-
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

# + [markdown]
# ### Notebook to check study codelist for trimethoprim and nitrofurantoin data
#
# A notebook to using [English Prescribing Data](https://www.nhsbsa.nhs.uk/prescription-data/prescribing-data/english-prescribing-data-epd) to compare codelists used by OpenPrescribing measure ["Antibiotic stewardship: prescribing of trimethoprim vs nitrofurantoin"](https://openprescribing.net/measure/trimethoprim/national/england/) against codelists being used in OpenSAFELY study.
#
# - [OpenPrescribing BNF codes](#OPBNF)
# - [OpenPrescribing final data](#OPFULL)
# - [Study BNF codes](#STUDYBNF)
# - [Study final data](#STUDYFULL)
# - [OpenPrescribing vs Study](#OPvsSTUDY)
# -


# ### Imports

# +
#import libraries required for analysis
from ebmdatalab import bq
import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#set to display all rows in data
pd.set_option('display.max_rows', None)
# -

# <a id=’OPBNF’></a>
# ### OpenPrescribing BNF codes
# Get [English Prescribing Data](https://www.nhsbsa.nhs.uk/prescription-data/prescribing-data/english-prescribing-data-epd) results for BNF codes as used in OpenPrescribing ["Antibiotic stewardship: prescribing of trimethoprim vs nitrofurantoin"](https://openprescribing.net/measure/trimethoprim/definition/).
#

# +
#OpenPrescribing BNF codes
sql = '''
SELECT
     CAST(month AS DATE) AS month,
     SUM (CASE WHEN bnf_code IN ("0501080W0AAADAD", "0501080W0AAAEAE", "0501080W0AAAIAI", "0501080W0AAAMAM", "0501080W0AAANAN", "0501080W0BCACAI", 
     "0501080W0BGABAE", "0501080W0BHAAAD", "0501080W0BHABAE")  THEN items ELSE 0 END) as OPtrimethoprim,
     SUM (CASE WHEN bnf_code IN ("0501130R0AAAAAA", "0501130R0AAABAB", "0501130R0AAACAC", "0501130R0AAADAD", "0501130R0AAAEAE", "0501130R0AAAGAG", 
     "0501130R0AAAJAJ", "0501130R0AAAMAM", "0501130R0AAANAN", "0501130R0AAATAT", "0501130R0AAAUAU", "0501130R0AAAVAV", "0501130R0AABDBD", 
     "0501130R0AABEBE", "0501130R0AABNBN", "0501130R0AABSBS", "0501130R0AACGCG", "0501130R0BBAAAD", "0501130R0BBABAE", "0501130R0BBACAC",
     "0501130R0BCAAAA", "0501130R0BCABAB", "0501130R0BGAAAG", "0501130R0BHAAAE", "0501130R0BHABAD")  THEN items ELSE 0 END) as OPnitrofurantoin
 FROM hscic.normalised_prescribing
 WHERE month >= '2019-01-01'
 GROUP BY month
 ORDER BY month'''

OP_DF = bq.cached_read(sql, csv_path=os.path.join('..','data','OPbnfcodes.csv'))
OP_DF
# -
# <a id=’OPFULL’></a>
# ### OpenPrescribing data
#
# Using dataframe from above, calculate:
# 1. total trimethoprim and nitrofurantoin data  
# 2. trimethoprim % of total of trimethoprim and nitrofurantoin.

# +
#Create new column - Sum of trimethoprim and nitrofurantoin columns
OP_DF['OPtrim+OPnitro'] = OP_DF['OPtrimethoprim'] + OP_DF['OPnitrofurantoin']

#Create new column - Trimethoprim as a % of trimethoprim + nitrofurantoin
OP_DF['OPtrim_percent'] = OP_DF['OPtrimethoprim'] / OP_DF['OPtrim+OPnitro'] * 100

OP_DF
# -

# <a id=’STUDYBNF’></a>
# ### Study BNF codes
# Get [English Prescribing Data](https://www.nhsbsa.nhs.uk/prescription-data/prescribing-data/english-prescribing-data-epd) results for BNF codes as used in the study definition:
# - [Trimethoprim codelist inc co-trimoxazole](https://www.opencodelists.org/codelist/user/yayang/codes_ab_type_trimethoprimcsv/1653d5a9/)
# - [Nitrofurantoin codelist](https://www.opencodelists.org/codelist/user/yayang/codes_ab_type_nitrofurantoincsv/56b72f70/)

# +
#Study BNF codes
sql = '''
SELECT
     CAST(month AS DATE) AS month,
     SUM (CASE WHEN bnf_code IN ("0501080W0AAAPAP", "0501080W0AAAAAA", "0501080W0BHABAE", "0501080W0AAAEAE", "0501080W0BHAAAD", "0501080W0AAAIAI",
     "0501080W0BCAAAD", "0501080W0BCACAI", "0501080W0AAADAD", "0501080W0BCABAE", "0501080W0BGABAE", "0501080W0AAANAN", "0501080W0AAAMAM",
     "0501080W0AAAQAQ", "0501080W0BCADAA", "0501080W0BGAAAD") THEN items ELSE 0 END) as Studytrimethoprim,
     SUM (CASE WHEN bnf_code IN ("0501080D0AAABAB", "0501080D0BGACAJ", "0501080D0AAATAT", "0501080D0AAAHAH", "0501080D0BGAAAH", "0501080D0AAAJAJ",
     "0501080D0BGAHAB", "0501080D0BGAFAC", "0501080D0AAAEAE", "0501080D0AAACAC", "0501080D0BGAEAE")  THEN items ELSE 0 END) as Studycotrimoxazole,
     SUM (CASE WHEN bnf_code IN ("0501130R0BHAAAE", "0501130R0BBABAE", "0501130R0BGAAAG", "0501130R0AACGCG", "0501130R0AAATAT", "0501130R0AABJBJ",
     "0501130R0AABABA", "0501130R0AAAWAW", "0501130R0BHABAD", "0501130R0AAACAC", "0501130R0AABYBY", "0501130R0AAAUAU", "0501130R0AAAEAE",
     "0501130R0AABVBV", "0501130R0AABTBT", "0501130R0BCABAB", "0501130R0AAAZAZ", "0501130R0AABUBU", "0501130R0AAALAL", "0501130R0AABCBC",
     "0501130R0BBACAC", "0501130R0BDABAE", "0501130R0AAARAR", "0501130R0AABGBG", "0501130R0AAAPAP", "0501130R0AAAQAQ", "0501130R0AABWBW",
     "0501130R0AAAXAX", "0501130R0AACECE", "0501130R0AABSBS", "0501130R0AABDBD", "0501130R0AAADAD", "0501130R0AACJCJ", "0501130R0AABKBK",
     "0501130R0AABEBE", "0501130R0AAAMAM", "0501130R0AACDCD", "0501130R0AAAAAA", "0501130R0AABLBL", "0501130R0AABIBI", "0501130R0AABXBX",
     "0501130R0BCAAAA", "0501130R0AAASAS", "0501130R0AABNBN", "0501130R0BBAAAD", "0501130R0AAAVAV", "0501130R0AABRBR", "0501130R0AACICI",
     "0501130R0AABPBP", "0501130R0AAABAB", "0501130R0AAAGAG", "0501130R0BDAAAD", "0501130R0AAAJAJ", "0501130R0AABBBB", "0501130R0AAANAN",
     "0501130R0AABQBQ")  THEN items ELSE 0 END) as Studynitrofurantoin
 FROM hscic.normalised_prescribing
 WHERE month >= '2019-01-01'
 GROUP BY month
 ORDER BY month'''

STUDY_DF = bq.cached_read(sql, csv_path=os.path.join('..','data','STUDYbnfcodes.csv'))
STUDY_DF
# -

# <a id=’STUDYFULL’></a>
# ### Study data
#
# Using dataframe from cell above, calculate:
# 1. sum trimethoprim + co-trimoxazole data
# 2. sum trimethoprim + nitrofurantoin data
# 3. sum trimethoprim + co-trimoxazole + nitrofurantoin data
# 4. trimethoprim % of total of trimethoprim and nitrofurantoin.
# 5. trimethoprim + co-trimoxazole % of total of trimethoprim, co-trimoxazole and nitrofurantoin.

# +
#Sum all trimethoprim containing
STUDY_DF['StudyTrim+Cotrim'] = STUDY_DF['Studytrimethoprim'] + STUDY_DF['Studycotrimoxazole']

#Create new column - Sum of trimethoprim and nitrofurantoin columns
STUDY_DF['StudyTrim+Nitro'] = STUDY_DF['Studytrimethoprim'] + STUDY_DF['Studynitrofurantoin']

#Create new column - Sum trimethoprim, co-trimoxazole and nitrofurantoin columns
STUDY_DF['StudyTrim+Cotrim+Nitro'] = STUDY_DF['Studytrimethoprim'] + STUDY_DF['Studycotrimoxazole'] + STUDY_DF['Studynitrofurantoin']

#Create new column - Trimethoprim as a % of trimethoprim + nitrofurantoin
STUDY_DF['Studytrim_percent'] = STUDY_DF['Studytrimethoprim'] / STUDY_DF['StudyTrim+Nitro'] * 100

#Create new column - Trimethoprim + co-trimoxazole as a % of trimethoprim + co-trimoxazole + nitrofurantoin
STUDY_DF['Studytrim+cotrim_percent'] = STUDY_DF['StudyTrim+Cotrim'] / STUDY_DF['StudyTrim+Cotrim+Nitro'] * 100

STUDY_DF
# -

# <a id=’OPvsSTUDY’></a>
# ### OpenPrescribing vs Study
#
# Side by side comparison of % for OpenPrescribing vs Study

# +
#Get OpenPrescribing data for final comparison
FINAL_DF = OP_DF[['month', 'OPtrim_percent']]

#Merge in Study data
FINAL_DF = pd.merge(FINAL_DF, STUDY_DF[['month', 'Studytrim_percent', 'Studytrim+cotrim_percent']] ,on='month',how='left')

FINAL_DF
# -

# ### Chart comparison
#
# Generate charts from data in above cell for comparison
# 1. OpenPrescribing codelists % of trimethoprim of total of trimethoprim + nitrofurantion
# 2. Study codelists % of trimethoprim of total of trimethoprim + nitrofurantion
# 3. Study codelists % of trimethoprim + co-trimoxazole of total of trimethoprim + co-trimoxazole + nitrofurantion

ax = FINAL_DF.groupby(["month"])['OPtrim_percent'].sum().plot(kind='line', title="OpenPrescribing % trimethoprim")
plt.xticks(rotation=90);
plt.ylabel('% of total');

ax = FINAL_DF.groupby(["month"])['Studytrim_percent'].sum().plot(kind='line', title="Study % trimethoprim")
plt.xticks(rotation=90);
plt.ylabel('% of total');

ax = FINAL_DF.groupby(["month"])['Studytrim+cotrim_percent'].sum().plot(kind='line', title="Study % trimethoprim + co-trimoxazole")
plt.xticks(rotation=90);
plt.ylabel('% of total');


