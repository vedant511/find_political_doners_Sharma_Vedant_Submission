#!/usr/bin/env python

###################################################################################################
# Run-time complexity of my code is O(n). It will run efficiently even for very large input files #
###################################################################################################

# First we will import the libraries which are used in the code
import numpy as np
import pandas as pd
import sys


# This function will take in the path to the input file, convert it into a dataframe, and return it.
def load_file(path):
    ip_file = pd.read_table(path, header=None, sep='|', dtype='str')
    return ip_file


# This function does the major job in creating the medianvals_by_zip.txt output file.
# It takes in the input dataframe returned by above load_file() method and two dictionaries which will get filled up
# by this method according to the contraints. It returns the medianvals_by_zip dataframe.
def parse_input(inp, by_zip_dict, by_date_dict):
    medianvals_by_zip = pd.DataFrame()
    zip_update_list = []
    for i in xrange(len(inp)):
        # Entering input data line by line into two dictionaries
        CMTE_ID = inp.iloc[i][0]
        TRANSACTION_DT = inp.iloc[i][13]
        TRANSACTION_AMT = float(inp.iloc[i][14])
        OTHER_ID = inp.iloc[i][15]
        zip_c = 0
        date = 0
        # First we will check if the required fields are correct
        if (len(CMTE_ID) == 9) and (CMTE_ID.isalnum()) and (not isinstance(OTHER_ID, str)) and \
                (TRANSACTION_AMT is not None) and (TRANSACTION_AMT >= 0):
            # Now we will check which fileds among zip and date are correct
            if (inp.iloc[i][10] is not None) and (len(inp.iloc[i][10]) >= 5) and (len(inp.iloc[i][10]) <= 9):
                ZIP_CODE = inp.iloc[i][10][:5]
                zip_c = 1

            if (TRANSACTION_DT is not None) and (len(TRANSACTION_DT) == 8):
                date = 1

            if zip_c and date:
                if CMTE_ID not in by_zip_dict:
                    by_zip_dict[CMTE_ID] = {ZIP_CODE:
                                                {'transaction': [TRANSACTION_AMT],
                                                 'num_transaction': 1,
                                                 'median_transaction': int(round(TRANSACTION_AMT)),
                                                 'total_amt': TRANSACTION_AMT
                                                 }
                                            }

                else:
                    if ZIP_CODE not in by_zip_dict[CMTE_ID]:
                        by_zip_dict[CMTE_ID][ZIP_CODE] = {'transaction': [TRANSACTION_AMT],
                                                          'num_transaction': 1,
                                                          'median_transaction': int(round(TRANSACTION_AMT)),
                                                          'total_amt': TRANSACTION_AMT
                                                          }

                    else:
                        by_zip_dict[CMTE_ID][ZIP_CODE]['transaction'].append(TRANSACTION_AMT)
                        by_zip_dict[CMTE_ID][ZIP_CODE]['num_transaction'] += 1
                        by_zip_dict[CMTE_ID][ZIP_CODE]['median_transaction'] = \
                            int(round(np.median(by_zip_dict[CMTE_ID][ZIP_CODE]['transaction'])))
                        by_zip_dict[CMTE_ID][ZIP_CODE]['total_amt'] += TRANSACTION_AMT

                if CMTE_ID not in by_date_dict:
                    by_date_dict[CMTE_ID] = {TRANSACTION_DT:
                                                 {'transaction': [TRANSACTION_AMT],
                                                  'num_transaction': 1,
                                                  'median_transaction': int(round(TRANSACTION_AMT)),
                                                  'total_amt': TRANSACTION_AMT
                                                  }
                                             }

                else:
                    if TRANSACTION_DT not in by_date_dict[CMTE_ID]:
                        by_date_dict[CMTE_ID][TRANSACTION_DT] = {'transaction': [TRANSACTION_AMT],
                                                                 'num_transaction': 1,
                                                                 'median_transaction': int(round(TRANSACTION_AMT)),
                                                                 'total_amt': TRANSACTION_AMT
                                                                 }

                    else:
                        by_date_dict[CMTE_ID][TRANSACTION_DT]['transaction'].append(TRANSACTION_AMT)
                        by_date_dict[CMTE_ID][TRANSACTION_DT]['num_transaction'] += 1
                        by_date_dict[CMTE_ID][TRANSACTION_DT]['median_transaction'] = \
                            int(round(np.median(by_date_dict[CMTE_ID][TRANSACTION_DT]['transaction'])))
                        by_date_dict[CMTE_ID][TRANSACTION_DT]['total_amt'] += TRANSACTION_AMT

                # Appending line to output dataframe medianvals_by_zip so that order remains intact
                new_entry = []
                new_entry.append(CMTE_ID)
                new_entry.append(ZIP_CODE)
                new_entry.append(by_zip_dict[CMTE_ID][ZIP_CODE]['median_transaction'])
                new_entry.append(by_zip_dict[CMTE_ID][ZIP_CODE]['num_transaction'])
                new_entry.append(int(by_zip_dict[CMTE_ID][ZIP_CODE]['total_amt']))
                zip_update_list.append(new_entry)

            elif zip_c and not date:
                if CMTE_ID not in by_zip_dict:
                    by_zip_dict[CMTE_ID] = {ZIP_CODE:
                                                {'transaction': [TRANSACTION_AMT],
                                                 'num_transaction': 1,
                                                 'median_transaction': int(round(TRANSACTION_AMT)),
                                                 'total_amt': TRANSACTION_AMT
                                                 }
                                            }

                else:
                    if ZIP_CODE not in by_zip_dict[CMTE_ID]:
                        by_zip_dict[CMTE_ID][ZIP_CODE] = {'transaction': [TRANSACTION_AMT],
                                                          'num_transaction': 1,
                                                          'median_transaction': int(round(TRANSACTION_AMT)),
                                                          'total_amt': TRANSACTION_AMT
                                                          }

                    else:
                        by_zip_dict[CMTE_ID][ZIP_CODE]['transaction'].append(TRANSACTION_AMT)
                        by_zip_dict[CMTE_ID][ZIP_CODE]['num_transaction'] += 1
                        by_zip_dict[CMTE_ID][ZIP_CODE]['median_transaction'] = \
                            int(round(
                                np.median(by_zip_dict[CMTE_ID][ZIP_CODE]['transaction'])))
                        by_zip_dict[CMTE_ID][ZIP_CODE]['total_amt'] += TRANSACTION_AMT

                # Appending line to output dataframe medianvals_by_zip so that order remains intact
                new_entry = []
                new_entry.append(CMTE_ID)
                new_entry.append(ZIP_CODE)
                new_entry.append(by_zip_dict[CMTE_ID][ZIP_CODE]['median_transaction'])
                new_entry.append(by_zip_dict[CMTE_ID][ZIP_CODE]['num_transaction'])
                new_entry.append(int(by_zip_dict[CMTE_ID][ZIP_CODE]['total_amt']))
                zip_update_list.append(new_entry)

            elif not zip_c and date:
                if CMTE_ID not in by_date_dict:
                    by_date_dict[CMTE_ID] = {TRANSACTION_DT:
                                                 {'transaction': [TRANSACTION_AMT],
                                                  'num_transaction': 1,
                                                  'median_transaction': int(round(TRANSACTION_AMT)),
                                                  'total_amt': TRANSACTION_AMT
                                                  }
                                             }

                else:
                    if TRANSACTION_DT not in by_date_dict[CMTE_ID]:
                        by_date_dict[CMTE_ID][TRANSACTION_DT] = {'transaction': [TRANSACTION_AMT],
                                                                 'num_transaction': 1,
                                                                 'median_transaction': int(round(TRANSACTION_AMT)),
                                                                 'total_amt': TRANSACTION_AMT
                                                                 }

                    else:
                        by_date_dict[CMTE_ID][TRANSACTION_DT]['transaction'].append(TRANSACTION_AMT)
                        by_date_dict[CMTE_ID][TRANSACTION_DT]['num_transaction'] += 1
                        by_date_dict[CMTE_ID][TRANSACTION_DT]['median_transaction'] = \
                            int(round(
                                np.median(by_date_dict[CMTE_ID][TRANSACTION_DT]['transaction'])))
                        by_date_dict[CMTE_ID][TRANSACTION_DT]['total_amt'] += TRANSACTION_AMT

    medianvals_by_zip = medianvals_by_zip.append(zip_update_list)
    return medianvals_by_zip


# This method takes in the by_date_dict modified by the "parse_input" method, and makes and returns a dataframe from it
# which contains the fields sorted by recipient ID and date.
def make_date_df(by_date_dict):
    date_update_list = []
    medianvals_by_date = pd.DataFrame()
    for id in by_date_dict:
        for date in by_date_dict[id]:
            temp = [id, date]
            temp.append(by_date_dict[id][date]['median_transaction'])
            temp.append(by_date_dict[id][date]['num_transaction'])
            temp.append(int(by_date_dict[id][date]['total_amt']))
            date_update_list.append(temp)
    medianvals_by_date = medianvals_by_date.append(date_update_list)
    medianvals_by_date.sort([0,1], ascending=True, inplace=True)
    return medianvals_by_date


# This method takes in the two final dataframes for medianvals by zip and dict respectively and makes the required
# output text files from them.
def make_text_files(by_zip_df, by_date_df):
    by_zip_df.to_csv('..\output\medianvals_by_zip.txt', header=None, index=None, sep='|', mode='w')
    by_date_df.to_csv('..\output\medianvals_by_date.txt', header=None, index=None, sep='|', mode='w')


# This is the main method which will be called when this program is run. It will call all the required methods.
# Note that input file's name will be given by the user as an argument to the program when we will run it, and it
# MUST be present in the input directory.
def main():
    by_zip_dict = dict()
    by_date_dict = dict()
    base_input_dir = "../input/"
    if len(sys.argv) == 2:
        user_entered_file = str(sys.argv[1])
    else:
        user_entered_file = "itcont.txt"
    inp = load_file(base_input_dir + user_entered_file)
    medianvals_by_zip = parse_input(inp, by_zip_dict, by_date_dict)
    medianvals_by_date = make_date_df(by_date_dict)
    make_text_files(medianvals_by_zip, medianvals_by_date)


if __name__ == '__main__':
    main()
