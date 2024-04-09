import os
from bs4 import BeautifulSoup
from blog import Blog


with open("../Template/archive.html", 'r+') as f:
    file = f.read()

soup = BeautifulSoup(file, 'lxml')

# get all blog infomation
blogFiles = []
for file in os.listdir("../Blog"):
    tmpBlog = Blog(os.path.join("../Blog", file))
    tmpInfo = {}
    tmpInfo['path'] = os.path.join("../Blog", file)
    tmpInfo['url'] = os.path.join(tmpBlog.info['date'][0:4], file.split('.')[0])
    tmpInfo['name'] = tmpBlog.info['name']
    tmpInfo['date'] = tmpBlog.info['date']
    blogFiles.append(tmpInfo)
blogFiles.sort(reverse=True, key=lambda info: info['date'])

# get years list
years = {}
blogByYears = {}
for blog in blogFiles:
    years[blog['date'][0:4]] = years.get(blog['date'][0:4], 0) + 1
    if blog['date'][0:4] not in blogByYears:
        blogByYears[blog['date'][0:4]] = []
    blogByYears[blog['date'][0:4]].append(blog)

# generate archive html
soup.select("#list")[0].clear()
for year, num in years.items():
    tmp = '''<li>
                <a href=\"{}\"> {} </a>
            </li>'''.format("https://guchongan.github.io/archives/" + year,
                            year + " (" + str(num) + ")")
    tmpSoup = BeautifulSoup(tmp, 'html.parser')
    soup.select("#list")[0].append(tmpSoup)

    tmpPath = os.path.join("../archives/", year)
    if not os.path.exists(tmpPath):
        os.makedirs(tmpPath)

# write html
with open("../archives/index.html", 'w') as f:
    f.write(soup.prettify())

print("\033[33m[Generate]\033[0m Archive page generated successfully")


# generate for year
with open("../Template/archive-page.html", 'r+') as f:
    file = f.read()

soup = BeautifulSoup(file, 'lxml')

for year in blogByYears.keys():
    table = soup.table
    table.clear()
    for blog in blogByYears[year]:
        tmp = '''<tr>
                    <td style=\"padding-right: 10px"> {}: </td>
                    <td> <a href=\"{}\"> xxxx </a> </td>
            </tr>'''.format(blog['date'][0:4] + '.' + blog['date'][4:6] + '.' + blog['date'][6:8],
                            "https://guchongan.github.io/" + blog['url'])
        tmpSoup = BeautifulSoup(tmp, 'html.parser')
        table.append(tmpSoup)
    with open(os.path.join("../archives/", year, 'index.html'), 'w') as f:
        f.write(soup.prettify())

print("\033[33m[Generate]\033[0m Archive page for year generated successfully")
