from onedrivedownloader import download
import pandas as pd

ln = "https://purdue0-my.sharepoint.com/:x:/g/personal/yang2309_purdue_edu/EdwNPXrfrhVAg3ucoF5B4GABcBblU_vcfn_V5OKi68Ltiw?e=5YarSL"
irrlog = "Irrlog.xlsx"
download(ln, filename=irrlog, force_download=True)

dfs = pd.read_excel(irrlog, sheet_name='Sheet1',skiprows=1)

# filter if 'Irrig?' column is 'Yes'
CIRRdf = dfs[dfs['Irrig?'] == 'Yes']
SIRRdf = dfs[dfs['Irrig?.1'] == 'Yes']
CFERTdf = dfs[dfs['Fert?'] == 'Yes']
SFERTdf = dfs[dfs['Fert?.1'] == 'Yes']

