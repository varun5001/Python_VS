"""
  @author: Varun
"""
import mammoth
import os
from bs4 import BeautifulSoup
import json
import re
#Folder path
path = "D:\\Work\\RnR\\soho_updated\\SOHO_in_R_R - Copy\\SOHO_new\\New folder\\international"
#Extract document file names
docfileNames = os.listdir(path+"\\docFiles")

#method to convert split document into  multiple HTML Files and convert to JSON
def docx2json(fileName):    
    with open(path + "\\docFiles\\" + fileName + ".docx", "rb") as docx_file:
        #convert to HTML
        result = mammoth.convert_to_html(docx_file)
        html = result.value # The generated HTML
        #split each html by heading
        htmlsplit = html.split("<h1>")
        htmlsplit = ["<h1>" + html for html in htmlsplit]
        for unit in htmlsplit[1:]:
            soup = BeautifulSoup(unit, 'html.parser')
            title = soup.h1.string
            data = {}
            #extract h1 text for file name
            cleanh1 = re.sub('[^0-9a-zA-Z]+', ' ', str(soup.h1.string))
            data['title'] = title 
            htmlPath = path + "\\htmlFiles\\" + cleanh1 + ".html"
            with open(htmlPath, "w") as html:
                html.write(str(soup))
            print("Converstion of " + fileName + ".docx completed")
            #remove h1 from json
            for tag in soup.find_all('h1'):
                tag.replaceWith('') 
            data['body'] = str(soup)
            json_data = json.dumps(data)
            print("Converstion of JSON for " + fileName + ".docx started")
            with open(path+"\\jsonFiles\\"+cleanh1+".json", "w") as file:
                file.write(json_data)
            print("Converstion of JSON for " + fileName + ".docx completed")

for fileName in docfileNames:
    fileName = fileName[0:-5] 
    print(".docx to HTML files Converstion in Progress: " + fileName + ".docx")
    #call method for each file
    docx2json(fileName)
    



                
                
           
