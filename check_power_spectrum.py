import pandas as pd
import hyperlink
import glob
import os
import numpy as np

file_list = glob.glob('/media3/CRP7/hosts/misc_results/power_spec_output/*_kstest.csv')

names = [item[50:62] for item in file_list]
list_links = ['https://fink-portal.org/' + item for item in names]

fname = '/media/emille/git/COIN/CRP7/hostless/code/power_spectrum_analysis_1.csv'
previous_file = os.path.isfile(fname)

answer = []

if previous_file:
    data_done = pd.read_csv(fname)
    op = open('/media/emille/git/COIN/CRP7/hostless/code/power_spectrum_analysis_1.csv', 'a')
else:
    op = open('/media/emille/git/COIN/CRP7/hostless/code/power_spectrum_analysis_1.csv', 'w')
    op.write('name, answer,ks_sci_stat_7,ks_sci_stat_15,ks_sci_stat_29,ks_temp_stat_7,ks_temp_stat_15,ks_temp_stat_29,' + \
             'ks_sci_pvalue_7,ks_sci_pvalue_15,ks_sci_pvalue_29,ks_temp_pvalue_7,ks_temp_pvalue_15,ks_temp_pvalue_29,'
             'ad_sci_stat_7,ad_sci_stat_15,ad_sci_stat_29,ad_temp_stat_7,ad_temp_stat_15,ad_temp_stat_29,' + \
             'ad_sci_pvalue_7,ad_sci_pvalue_15,ad_sci_pvalue_29,ad_temp_pvalue_7,ad_temp_pvalue_15,ad_temp_pvalue_29\n')
    
for item in range(200, 250):
    name = file_list[item][50:62]
    
    if name not in data_done['name'].values:
        data_ks = pd.read_csv(file_list[item])
        name_ad = '/media3/CRP7/hosts/misc_results/power_spec_output/' + name + '_anderson-darling.csv'
        if os.path.isfile(name_ad):
            data_ad = pd.read_csv(name_ad)
        else:
            data_ad = pd.DataFrame(np.full(data_ks.shape, -99), columns=data_ks.keys())
        url = hyperlink.parse(list_links[item])
        print(url)
        ans = input('what do you think of this one?')

        op.write(names[item][:12] + ',' + ans + ',')
        for i in range(data_ks.shape[0]):
            op.write(str(data_ks.values[i][2]) + ',')
        for i in range(data_ks.shape[0]):
            op.write(str(data_ks.values[i][3]) + ',')
        for i in range(data_ad.shape[0]):
            op.write(str(data_ad.values[i][2]) + ',')
        for i in range(data_ad.shape[0] - 1):
            op.write(str(data_ad.values[i][3]) + ',')
        op.write(str(data_ad.values[-1][3]) + '\n')
op.close()
 