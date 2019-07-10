import gspread
from oauth2client.service_account import ServiceAccountCredentials
from random import sample


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('Football-6ee6aab5e6fd.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('Football data').sheet1

# print(wks.get_all_records())

# wks.append_row(['secondata1', 'secondata2'])

# wks.update_acell('C1', 'Column 3')

all_row = wks.get_all_values()
del all_row[0]
del all_row[0]

def row_to_dict(row):
	mydict = [(x[0], float(x[7])) for x in row]
	return mydict
row_to_dict(all_row)

random = sample(row_to_dict(all_row), len(row_to_dict(all_row)))

l1 = []
l2 = []
for x, y in random[0:5]:
	l1.append(y)
for i, j in random[5:10]:
	l2.append(j)

if abs(sum(l1) - sum(l2)) < 2:
	print(sum(l1), sum(l2))
	print('First: {}, Second: {}'.format(random[0:5], random[5:10]))
else:
	print('Try again')
