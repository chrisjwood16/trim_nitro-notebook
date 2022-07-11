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
0501080D0AAAJAJ
0501080D0AAAJAJ
0501080D0AAAJAJ
0501080D0AAAJAJ
0501080D0AAAJAJ
0501080D0AAAJAJ
0501080D0AAAJAJ
0501080D0AAAJAJ
0501080D0AAAJAJ
0501080D0AAATAT
0501080D0AAATAT
0501080D0AAACAC
0501080D0AAACAC
0501080D0AAACAC
0501080D0AAACAC
0501080D0AAACAC
0501080D0AAACAC
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAHAH
0501080D0AAAEAE
0501080D0AAAEAE
0501080D0AAAEAE
0501080D0AAAEAE
0501080D0AAABAB
0501080D0AAABAB
0501080D0AAABAB
0501080D0AAABAB
0501080D0AAABAB
0501080D0BGAEAE
0501080D0BGAHAB
0501080D0BGACAJ
0501080D0BGAFAC
0501080D0BGAAAH
'''

bnfcodes = SQLformatBNFcodes(bnfcodeslist)
bnfcodes

# -


