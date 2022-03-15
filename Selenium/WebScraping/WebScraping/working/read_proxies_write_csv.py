from common.beautifulsoup_operations import beautifulsoup_operations
from common.file.csv_operations import csv_operations

bs = beautifulsoup_operations()

list_of_proxyies = bs.read_proxies_sslproxies_org()

csv = csv_operations()

csv.write_csvfile("ListofProxy", list_of_proxyies)

print("file written!")
