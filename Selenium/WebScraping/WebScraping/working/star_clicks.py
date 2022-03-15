from common.beautifulsoup_operations import beautifulsoup_operations
from common.file.csv_operations import csv_operations
from useragent import user_agent
import random
import requests

impressions = random.randint(3, 10)

bs = beautifulsoup_operations()
#list_of_proxyies = bs.read_proxies_sslproxies_org()

csv = csv_operations()
#csv.write_list_to_txt('ListofProxy', list_of_proxyies)

listofips = csv.read_txt_to_list('ListofProxy')

ua = user_agent()

loop_counter = 1
#use request for star-clicks impression
for x in range(impressions):
    proxy = {'https': random.choice(listofips).strip()}
    #print(ua.random_user_agent())
    #header = {'User-Agent':str(ua.random_user_agent())
    user_a = ua.random_user_agent()
    header = {'User-Agent':user_a}
    print(str(loop_counter)+ ': '+ user_a)
    #url = "https://www.hybrid-analysis.com/recent-submissions?filter=file&sort=^timestamp"
    url = "http://ppcwebsite.weebly.com"
    htmlContent = requests.get(url, headers=header, proxies=proxy)
    loop_counter = loop_counter+1

print("file written!")
