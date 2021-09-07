import requests
from termcolor import colored

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

def subdomains(target_url):
    with open('subdomains.txt', 'r') as subdomains_list:
        for line in subdomains_list:
            word = line.strip()
            test_url = word + "." + target_url
            ressponse = request(test_url)
            if ressponse:
                print(colored("[+] Subdomain URL --> " + test_url + " [+]", 'green'))
                response_list.append(test_url)

def directories(target_url):
    with open('dirs.txt', 'r') as dirs_list:
        for line in dirs_list:
            word = line.strip()
            test_url = target_url + "/" + word
            ressponse = request(test_url)
            if ressponse:
                print(colored("[+] Directories URL --> " + test_url + " [+]", 'green'))

response_list = []
def all(target_url):
    subdomains(target_url)
    for urls in response_list:
        directories(urls)

url = input("Enter URL: ")
crawl_type = input("Enter the desired search type or type 'help' for help: ")
if crawl_type == 'help':
    print(colored('''
    \t\tall         ----------------> scans for directories as well as subdomains
    \t\tsubdomains  ----------------> scans for all the subdomains
    \t\tdirectories ----------------> scans for all the directories ''', 'blue'))
    pass
elif crawl_type == 'subdomains':
    subdomains(url)
elif crawl_type == 'all':
    all(url)
elif crawl_type == 'directories':
    directories(url)
else:
    print(colored('[-] Incorrect Parameters!! [-]', 'red'))


