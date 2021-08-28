import requests, sys, bs4, os
print('May the Force be with you')

def getContentFromCodeforces(url):
    response = requests.get(url)
    response.raise_for_status()
    return response

def copyTemplate(copy_to_file, template_file):
    with open(template_file, 'r') as firstFile:
        with open(copy_to_file, 'w') as secondFile:
            for line in firstFile:
                secondFile.write(line)

def createProblemFiles(contest_url, problem_id, template_file_dir):
    problem_url = contest_url + "/problem/" + problem_id
    response = getContentFromCodeforces(problem_url)
    soup = bs4.BeautifulSoup(response.text, features="html.parser")
    sample_test = soup.find(class_='sample-test').get_text()
    sample_test_file = open(problem_id + '_tests.txt', 'w')
    sample_test_file.write(sample_test)
    sample_test_file.close()
    copyTemplate(problem_id+'.cpp', template_file_dir)
    # linkElems = soup.select('div div[class="sample-tests"]')
    # print(soup.find(class_='sample-test').get_text())
    # print(linkElems)


#taking input
contest_url = ''.join(sys.argv[1])
template_file_dir = ''.join(sys.argv[2])
#extracting contest id for folder name from url
folder_name = contest_url[contest_url.rindex("/")+1:]

current_dir = os.getcwd()
final_dir = os.path.join(current_dir, folder_name)
if not os.path.exists(final_dir):
    os.makedirs(final_dir)
os.chdir(final_dir)

response = getContentFromCodeforces(contest_url)

soup = bs4.BeautifulSoup(response.text, features="html.parser")
linkElems = soup.select('div[class="datatable"]')
links = linkElems[0].findAll('a')
previous_id = ''
# cf = open(template_file_dir, 'r')
createProblemFiles(contest_url, 'A', template_file_dir)

for link in links:
    problem_url = link.get('href')
    problem_id = problem_url[problem_url.rindex("/")+1:]
    if(previous_id != problem_id):
        createProblemFiles(contest_url, problem_id, template_file_dir)

    # print(s)
# print(links)