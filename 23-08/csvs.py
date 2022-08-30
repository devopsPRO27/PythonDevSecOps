import csv

# file= open('data.csv','w')
#
# file.close()

# with open('data.csv','w') as file:
#     csv_file_writer = csv.writer(file) # writer is the way to insert values to the file
#     csv_file_writer.writerow(['Movie','len','year'])
#     csv_file_writer.writerow(['Adam project',120,2022])
#     csv_file_writer.writerow(['saw',300,2006])
#     csv_file_writer.writerow(['superman',150,2012])
#
#
# list = [
#     ['superman',150,2012],
#     ['superman',150,2012],
#     ['superman',150,2012],
#     ['superman',150,2012]
#          ]

with open('data.csv','r') as file:
    csv_file_reader = csv.reader(file)
    content_list = list(csv_file_reader)
    for row in content_list:
        print(row)
        for item in row:
            print(item)










