answer = []
op = open('/media/emille/git/COIN/CRP7/hostless/code/power_spectrum_analysis_1.csv', 'w')
op.write('name, answer, pvalue_template_29\n')
for item in range(50):
    data = pd.read_csv(names[item])
    url = hyperlink.parse(list_links[item])
    print(url)
    ans = input('what do you think of this one?')
    answer.append([names[item][:12], ans, data.iloc[5]])
    op.write(names[item][:12] + ',' + ans + ',' + str(data.iloc[5].values) + '\n')
op.close()
