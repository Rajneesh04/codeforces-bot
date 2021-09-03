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
    #creating a folder with name as that of problem_id
    problem_dir = os.path.join(os.getcwd(), problem_id)
    if not os.path.exists(problem_dir):
        os.makedirs(problem_dir)
    os.chdir(problem_dir)

    problem_url = contest_url + "/problem/" + problem_id
    response = getContentFromCodeforces(problem_url)
    soup = bs4.BeautifulSoup(response.text, features="html.parser")

    #input test file
    sample_input = soup.find(class_='input').get_text()
    #to remove first line
    sample_input = sample_input[6:]
    sample_input_file = open('input.txt', 'w')
    sample_input_file.write(sample_input)
    sample_input_file.close()

    #output test file
    sample_output = soup.find(class_='output').get_text()
    #to remove first line
    sample_output = sample_output[7:]
    sample_output_file = open('out.txt', 'w')
    sample_output_file.write(sample_output)
    sample_output_file.close()

    copyTemplate(problem_id+'.cpp', os.path.join(template_file_dir+'/template.cpp'))
    #back to contest folder
    os.chdir('..')


#taking input
contest_url = ''.join(sys.argv[1])

#extracting contest id for folder name from url
folder_name = contest_url[contest_url.rindex("/")+1:]

current_dir = os.getcwd()
#template.cpp should be present in the directory where python script is present
template_file_dir = current_dir
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
    previous_id = problem_id
