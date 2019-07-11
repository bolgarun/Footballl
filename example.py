import gspread
from oauth2client.service_account import ServiceAccountCredentials
from random import sample


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('Football-6ee6aab5e6fd.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('Football data').sheet1

all_row = wks.get_all_values()
del all_row[0]
del all_row[0]

def row_to_dict(row):
	mydict = [(x[0], float(x[7])) for x in row if x[14] == '+']
	return mydict
row_to_dict(all_row)

if len(row_to_dict(all_row)) == 10:
	n = 20
	final_list = []
	while n > 0:
		n -= 1
		random = sample(row_to_dict(all_row), len(row_to_dict(all_row)))
		command1 = random[0:5]
		command2 = random[5:10]
		sum_command1 = sum(x[1] for x in command1)
		sum_command2 = sum(x[1] for x in command2)
		different = sum_command1 - sum_command2
		players_command1 = ", ".join(x[0] for x in command1)
		players_command2 = ", ".join(x[0] for x in command2)
		list_command = [different, players_command1, players_command2]
		if list_command[0] > 0 and list_command[0] < 2:
			final_list.append(list_command)

	num = 1.5
	for a in final_list:
		if a[0] < num:
			num = a[0]
		else:
			num = num
	for x in final_list:
		if x[0] == num:
			print(x)
else:
	print('not enough players')