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
# - [OpenPrescribing trimethoprim BNF codes](#OPTRIM)
# - [OpenPrescribing nitrofurantoin BNF codes](#OPNITRO)
# - [OpenPrescribing final data](#OPFULL)
# - [Study trimethoprim BNF codes](#STUDYTRIM)
# - [Study co-trimoxazole BNF codes](#STUDYCOTRIM)
# - [Study nitrofurantoin BNF codes](#STUDYNITRO)
# - [Study final data](#STUDYFULL)
# - [OpenPrescribing vs Study](#OPvsSTUDY)
# -


from ebmdatalab import bq
import os
import pandas as pd
pd.set_option('display.max_rows', None)

# <a id=’OPTRIM’></a>
# ### OpenPrescribing Trimethoprim BNF codes

# +
#OpenPrescribing Trimethoprim BNF codes
sql = '''
SELECT
     CAST(month AS DATE) AS month,
     SUM(items) AS OPtrimethoprim
 FROM hscic.normalised_prescribing
 WHERE bnf_code IN ("0501080W0AAADAD", "0501080W0AAAEAE", "0501080W0AAAIAI", "0501080W0AAAMAM", "0501080W0AAANAN", "0501080W0BCACAI", "0501080W0BGABAE", "0501080W0BHAAAD", "0501080W0BHABAE")
 AND month >= '2019-01-01'
 GROUP BY month
 ORDER BY month'''

OPtrim = bq.cached_read(sql, csv_path=os.path.join('..','data','OPtrim.csv'))
OPtrim
# -
# <a id=’OPNITRO’></a>
# ### OpenPrescribing nitrofurantoin BNF codes

# +
#OpenPrescribing nitrofurantoin BNF codes
sql = '''
SELECT
     CAST(month AS DATE) AS month,
     SUM(items) AS OPnitrofurantoin
 FROM hscic.normalised_prescribing
 WHERE bnf_code IN ("0501130R0AAAAAA", "0501130R0AAABAB", "0501130R0AAACAC", "0501130R0AAADAD", "0501130R0AAAEAE", "0501130R0AAAGAG", "0501130R0AAAJAJ", "0501130R0AAAMAM", "0501130R0AAANAN", "0501130R0AAATAT", "0501130R0AAAUAU", "0501130R0AAAVAV", "0501130R0AABDBD", "0501130R0AABEBE", "0501130R0AABNBN", "0501130R0AABSBS", "0501130R0AACGCG", "0501130R0BBAAAD", "0501130R0BBABAE", "0501130R0BBACAC", "0501130R0BCAAAA", "0501130R0BCABAB", "0501130R0BGAAAG", "0501130R0BHAAAE", "0501130R0BHABAD")
 AND month >= '2019-01-01'
 GROUP BY month
 ORDER BY month'''

OPnitro = bq.cached_read(sql, csv_path=os.path.join('..','data','OPnitro.csv'))
OPnitro
# -


# <a id=’OPFULL’></a>
# ### OpenPrescribing final data

OP_DF = pd.merge(OPtrim,OPnitro,on='month',how='left')
OP_DF['OPtrim+OPnitro'] = OP_DF['OPtrimethoprim'] + OP_DF['OPnitrofurantoin']
OP_DF['OPtrim_percent'] = OP_DF['OPtrimethoprim'] / OP_DF['OPtrim+OPnitro']
OP_DF

# <a id=’STUDYTRIM’></a>
# ### Study trimethoprim BNF codes

# +
#Study Trimethoprim BNF codes
sql = '''
SELECT
     CAST(month AS DATE) AS month,
     SUM(items) AS Studytrimethoprim
 FROM hscic.normalised_prescribing
 WHERE bnf_code IN ("0501080W0AAAPAP", "0501080W0AAAAAA", "0501080W0BHABAE", "0501080W0AAAEAE", "0501080W0BHAAAD", "0501080W0AAAIAI", "0501080W0BCAAAD", "0501080W0BCACAI", "0501080W0AAADAD", "0501080W0BCABAE", "0501080W0BGABAE", "0501080W0AAANAN", "0501080W0AAAMAM", "0501080W0AAAQAQ", "0501080W0BCADAA", "0501080W0BGAAAD")
 AND month >= '2019-01-01'
 GROUP BY month
 ORDER BY month'''

Studytrim = bq.cached_read(sql, csv_path=os.path.join('..','data','Studytrim.csv'))
Studytrim
# -

# <a id=’STUDYCOTRIM’></a>
# ### Study co-trimoxazole BNF codes

# +
#Study Co-trimoxazole BNF codes
sql = '''
SELECT
     CAST(month AS DATE) AS month,
     SUM(items) AS Studycotrimoxazole
 FROM hscic.normalised_prescribing
 WHERE bnf_code IN ("0501080D0AAABAB", "0501080D0BGACAJ", "0501080D0AAATAT", "0501080D0AAAHAH", "0501080D0BGAAAH", "0501080D0AAAJAJ", "0501080D0BGAHAB", "0501080D0BGAFAC", "0501080D0AAAEAE", "0501080D0AAACAC", "0501080D0BGAEAE")
 AND month >= '2019-01-01'
 GROUP BY month
 ORDER BY month'''

StudyCotrim = bq.cached_read(sql, csv_path=os.path.join('..','data','StudyCotrim.csv'))
StudyCotrim
# -

# <a id=’STUDYNITRO’></a>
# ### Study nitrofurantoin BNF codes

# +
#Study nitrofurantoin BNF codes
sql = '''
SELECT
     CAST(month AS DATE) AS month,
     SUM(items) AS Studynitrofurantoin
 FROM hscic.normalised_prescribing
 WHERE bnf_code IN ("0501130R0BHAAAE", "0501130R0BBABAE", "0501130R0BGAAAG", "0501130R0AACGCG", "0501130R0AAATAT", "0501130R0AABJBJ", "0501130R0AABABA", "0501130R0AAAWAW", "0501130R0BHABAD", "0501130R0AAACAC", "0501130R0AABYBY", "0501130R0AAAUAU", "0501130R0AAAEAE", "0501130R0AABVBV", "0501130R0AABTBT", "0501130R0BCABAB", "0501130R0AAAZAZ", "0501130R0AABUBU", "0501130R0AAALAL", "0501130R0AABCBC", "0501130R0BBACAC", "0501130R0BDABAE", "0501130R0AAARAR", "0501130R0AABGBG", "0501130R0AAAPAP", "0501130R0AAAQAQ", "0501130R0AABWBW", "0501130R0AAAXAX", "0501130R0AACECE", "0501130R0AABSBS", "0501130R0AABDBD", "0501130R0AAADAD", "0501130R0AACJCJ", "0501130R0AABKBK", "0501130R0AABEBE", "0501130R0AAAMAM", "0501130R0AACDCD", "0501130R0AAAAAA", "0501130R0AABLBL", "0501130R0AABIBI", "0501130R0AABXBX", "0501130R0BCAAAA", "0501130R0AAASAS", "0501130R0AABNBN", "0501130R0BBAAAD", "0501130R0AAAVAV", "0501130R0AABRBR", "0501130R0AACICI", "0501130R0AABPBP", "0501130R0AAABAB", "0501130R0AAAGAG", "0501130R0BDAAAD", "0501130R0AAAJAJ", "0501130R0AABBBB", "0501130R0AAANAN", "0501130R0AABQBQ")
 AND month >= '2019-01-01'
 GROUP BY month
 ORDER BY month'''

Studynitro = bq.cached_read(sql, csv_path=os.path.join('..','data','Studynitro.csv'))
Studynitro
# -

# <a id=’STUDYFULL’></a>
# ### Study full data

# +
#Join trim containing study results
STUDY_DF = pd.merge(Studytrim, StudyCotrim ,on='month',how='left')
#Sum all trimethoprim containing
STUDY_DF['StudyTrim+Cotrim'] = STUDY_DF['Studytrimethoprim'] + STUDY_DF['Studycotrimoxazole']

#Join nitrofurantoin results
STUDY_DF = pd.merge(STUDY_DF, Studynitro ,on='month',how='left')

STUDY_DF['StudyTrim+Nitro'] = STUDY_DF['Studytrimethoprim'] + STUDY_DF['Studynitrofurantoin']
STUDY_DF['StudyTrim+Cotrim+Nitro'] = STUDY_DF['Studytrimethoprim'] + STUDY_DF['Studycotrimoxazole'] + STUDY_DF['Studynitrofurantoin']

STUDY_DF['Studytrim_percent'] = STUDY_DF['Studytrimethoprim'] / STUDY_DF['StudyTrim+Nitro']
STUDY_DF['Studytrim+cotrim_percent'] = STUDY_DF['StudyTrim+Cotrim'] / STUDY_DF['StudyTrim+Cotrim+Nitro']

STUDY_DF
# -

# <a id=’OPvsSTUDY’></a>
# ### OpenPrescribing vs Study

FINAL_DF = OP_DF[['month', 'OPtrim_percent']]
FINAL_DF = pd.merge(FINAL_DF, STUDY_DF[['month', 'Studytrim_percent', 'Studytrim+cotrim_percent']] ,on='month',how='left')
FINAL_DF


