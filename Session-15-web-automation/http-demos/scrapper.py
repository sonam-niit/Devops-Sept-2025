from bs4 import BeautifulSoup

html= """
<!DOCTYPE html>
<html>
    <head>
        <title>Sonam Soni</title>
    </head>
    <body>
        <h1>This is a Heading</h1>
        <p>This is First Paragraph</p>
        <p class="info">This is a paragraph.</p>
    </body>
</html>
"""
# parse in HTML
soup=BeautifulSoup(html,'html.parser')
print("Title: ",soup.title.text)
print("Heading: ",soup.h1.text)
print("Para 1: ",soup.p.text) # it will capture only first para
print("Para: ",soup.find("p",class_="info").text) # capture others by class or id
