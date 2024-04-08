import os
from bs4 import BeautifulSoup
from blog import Blog


with open("../index.html", 'r+') as f:
    file = f.read()

soup = BeautifulSoup(file, 'lxml')

# Archive list generate
# get archive list html
archiveList = soup.tbody

# get ten file
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
blogFiles = blogFiles[0:10]

# set archive list html
archiveList.clear()
for blog in blogFiles:
    tmp = '''<tr>
                <td style=\"padding-right: 10px\">{}:</td>
                <td><a href=\"{}\">{}</a></td>
            </tr>'''.format(blog['date'][0:4] + '.' + blog['date'][4:6] + '.' + blog['date'][6:8],
                            "http://guchongan.github.io/" + blog['url'],
                            blog['name'])
    trSoup = BeautifulSoup(tmp, 'lxml')
    archiveList.append(trSoup)


# Home page's article generate
# get article html
article = soup.article

# article's href, name, time
article.a['href'] = "https://guchongan.github.io/" + blogFiles[0]['url']
article.a.string = blogFiles[0]['name']
tmpDate = blogFiles[0]['date']
article.time.string = tmpDate[0:4] + '.' + tmpDate[4:6] + '.' + tmpDate[6:8]

# article's content
content = article.select('.entry-content')[0]
tmpBlog = Blog(blogFiles[0]['path'])
content.clear()
content.append(BeautifulSoup(tmpBlog.blog, 'lxml'))

# write html
with open("../index.html", 'w') as f:
    f.write(soup.prettify())

print("\033[33m[Generate]\033[0m Home page generated successfully")

