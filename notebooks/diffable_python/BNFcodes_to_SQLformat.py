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

# # Plain BNF codes to SQL format conversion
# Enter BNF codes without formatting to return SQL compatible result

def SQLformatBNFcodes(bnfcodeslist):
    #Convert to list
    bnfcodeslist = bnfcodes.split('\n')

    #Remove empty list items
    bnfcodeslist = list(filter(None, bnfcodeslist))

    #Remove duplicate codes
    bnfcodeslist = list(set(bnfcodeslist))

    #Convert to quoted, comma seperated list
    bnfcodesstring = ', '.join(f'"{code}"' for code in bnfcodeslist)

    return bnfcodesstring


# +
bnfcodes = '''
0501130R0BBABAE
0501130R0BBACAC
0501130R0BBAAAD
0501130R0BHAAAE
0501130R0BHABAD
0501130R0BGAAAG
0501130R0BCABAB
0501130R0BCAAAA
0501130R0AAABAB
0501130R0AAABAB
0501130R0AAABAB
0501130R0AAABAB
0501130R0AAABAB
0501130R0AAABAB
0501130R0AAABAB
0501130R0AAABAB
0501130R0AAABAB
0501130R0AAAGAG
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAEAE
0501130R0AAAJAJ
0501130R0AAAJAJ
0501130R0AAAJAJ
0501130R0AAAJAJ
0501130R0AAATAT
0501130R0AAATAT
0501130R0AAATAT
0501130R0AAATAT
0501130R0AACGCG
0501130R0AACGCG
0501130R0AACGCG
0501130R0AACGCG
0501130R0AABEBE
0501130R0AABEBE
0501130R0AABEBE
0501130R0AABEBE
0501130R0AABSBS
0501130R0AABSBS
0501130R0AABSBS
0501130R0AABSBS
0501130R0AAAUAU
0501130R0AAAUAU
0501130R0AAAUAU
0501130R0AAAUAU
0501130R0AACECE
0501130R0AACECE
0501130R0AACECE
0501130R0AACECE
0501130R0AAASAS
0501130R0AAASAS
0501130R0AAASAS
0501130R0AAASAS
0501130R0AABWBW
0501130R0AABWBW
0501130R0AABWBW
0501130R0AABWBW
0501130R0AAALAL
0501130R0AAALAL
0501130R0AAALAL
0501130R0AAALAL
0501130R0AABJBJ
0501130R0AABJBJ
0501130R0AABJBJ
0501130R0AABJBJ
0501130R0AACICI
0501130R0AACICI
0501130R0AACICI
0501130R0AACICI
0501130R0AABIBI
0501130R0AABIBI
0501130R0AABIBI
0501130R0AABIBI
0501130R0AABQBQ
0501130R0AABQBQ
0501130R0AABQBQ
0501130R0AABQBQ
0501130R0AAAQAQ
0501130R0AAAQAQ
0501130R0AAAQAQ
0501130R0AAAQAQ
0501130R0AACDCD
0501130R0AACDCD
0501130R0AACDCD
0501130R0AACDCD
0501130R0AABDBD
0501130R0AABDBD
0501130R0AABDBD
0501130R0AABDBD
0501130R0AAAVAV
0501130R0AAAVAV
0501130R0AAAVAV
0501130R0AAAVAV
0501130R0AABGBG
0501130R0AABGBG
0501130R0AABGBG
0501130R0AABGBG
0501130R0AABYBY
0501130R0AABYBY
0501130R0AABYBY
0501130R0AABYBY
0501130R0AAAMAM
0501130R0AAAMAM
0501130R0AAAMAM
0501130R0AAAMAM
0501130R0AAACAC
0501130R0AAACAC
0501130R0AAACAC
0501130R0AAACAC
0501130R0AAACAC
0501130R0AAACAC
0501130R0AABCBC
0501130R0AABCBC
0501130R0AABCBC
0501130R0AABCBC
0501130R0AAAZAZ
0501130R0AAAZAZ
0501130R0AAAZAZ
0501130R0AAAZAZ
0501130R0AABUBU
0501130R0AABUBU
0501130R0AABUBU
0501130R0AABUBU
0501130R0AABPBP
0501130R0AABPBP
0501130R0AABPBP
0501130R0AABPBP
0501130R0AAAPAP
0501130R0AAAPAP
0501130R0AAAPAP
0501130R0AAAPAP
0501130R0AABXBX
0501130R0AABXBX
0501130R0AABXBX
0501130R0AABXBX
0501130R0AABVBV
0501130R0AABVBV
0501130R0AABVBV
0501130R0AABVBV
0501130R0AABNBN
0501130R0AABNBN
0501130R0AABNBN
0501130R0AABNBN
0501130R0AAAAAA
0501130R0AAAAAA
0501130R0AAAAAA
0501130R0AAAAAA
0501130R0AAAAAA
0501130R0AAAAAA
0501130R0AAAAAA
0501130R0AAAAAA
0501130R0AAAAAA
0501130R0AAAAAA
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAADAD
0501130R0AAANAN
0501130R0AAANAN
0501130R0AAANAN
0501130R0AAANAN
0501130R0AAARAR
0501130R0AAARAR
0501130R0AAARAR
0501130R0AAARAR
0501130R0AAAWAW
0501130R0AAAWAW
0501130R0AAAWAW
0501130R0AAAWAW
0501130R0AABRBR
0501130R0AABRBR
0501130R0AABRBR
0501130R0AABRBR
0501130R0AAAXAX
0501130R0AAAXAX
0501130R0AAAXAX
0501130R0AAAXAX
0501130R0AACJCJ
0501130R0AACJCJ
0501130R0AACJCJ
0501130R0AACJCJ
0501130R0AABKBK
0501130R0AABKBK
0501130R0AABKBK
0501130R0AABKBK
0501130R0AABBBB
0501130R0AABBBB
0501130R0AABBBB
0501130R0AABBBB
0501130R0AABLBL
0501130R0AABLBL
0501130R0AABLBL
0501130R0AABLBL
0501130R0AABTBT
0501130R0AABTBT
0501130R0AABTBT
0501130R0AABTBT
0501130R0AABABA
0501130R0AABABA
0501130R0AABABA
0501130R0AABABA
0501130R0BDABAE
0501130R0BDAAAD
'''

bnfcodes = SQLformatBNFcodes(bnfcodes)
bnfcodes

# -

