import os
import sys
from bs4 import BeautifulSoup
from blog import Blog


def generateOneBlog(fileName):
    # get blog template
    with open("../Template/blog.html", 'r+') as f:
        file = f.read()
    soup = BeautifulSoup(file, 'lxml')

    # get blog information
    blog = Blog(os.path.join("../Blog", fileName))

    # set title
    soup.title.string = blog.info['name'] + " - Chongan's website"

    # set href, title, date and keywords
    content = soup.select("#content")[0]
    tmpHref = "https://guchongan.github.io/" + blog.info['date'][0:4] + "/" + blog.info['name']
    tmpDate = blog.info['date'][0:4] + '.' + blog.info['date'][4:6] + '.' + blog.info['date'][6:8]
    content.a['href'] = tmpHref
    content.a['title'] = blog.info['name']
    content.a.string = blog.info['name']
    content.time.string = tmpDate
    content.footer.append(BeautifulSoup("<a>" + blog.info['keywords'] + "</a>", 'lxml'))

    # set blog content
    content.select(".entry-content")[0].append(BeautifulSoup(blog.blog, 'lxml'))

    # set imag path
    if content.img is not None:
        for image in content.find_all('img'):
            image['src'] = os.path.join("..", image['src'])

    # write html
    tmpPath = os.path.join("..", blog.info['date'][0:4])
    if not os.path.exists(tmpPath):
        os.makedirs(tmpPath)
    tmpPath = os.path.join(tmpPath, fileName.split('.')[0])
    if not os.path.exists(tmpPath):
        os.makedirs(tmpPath)
    with open(os.path.join(tmpPath, "index.html"), 'w') as f:
        f.write(soup.prettify())


# Default generate all else generate one file
all = True
if len(sys.argv) > 1:
    all = False
    fileName = sys.argv[1]

if all:
    for file in os.listdir("../Blog/"):
        generateOneBlog(file)
    print("\033[33m[Generate]\033[0m All blog html generated successfully")
else:
    generateOneBlog(fileName)
    print("\033[33m[Generate]\033[0m {} html generated successfully".format(fileName))


