# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:48:41 2022

@author: hp
"""

#Problem Set 2
#This problem set is based on lectures 4,5 and 6. For a complete list of topics please consult page 2 of the course syllabus. Please consult the “Instructions for Problem Set Submissions” document under course information before submitting your assignment.


print(" Question 1")
a = 0
def b():
    global a
    a = c(a)
    
def c(a):
    return a + 2

b()
b()
b()
a

## in every iteration the value of variable 'a' is being incremented by 2. Initallly, the value is 0 but after three calls of a(), it turns to 6. 

## Question 2
print("****************************************")
print("\n Question 2")
def file_length(file_name):
    try:
        file = open(file_name)
        contents = file.read()
        file.close()
        print(len(contents))
    except:
        print("File " +file_name + " not found.")
        
    
file_length('idterm.py')    



## Question 3
print("****************************************")
print("\n Question 3")

class Marsupial:
    def __init__(self):
         self.pouch = []
    def put_in_pouch(self,name):
          self.pouch.append(name)
    def pouch_contents(self):
          print(self.pouch)

m = Marsupial()
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
m.pouch_contents()

class Kangaroo(Marsupial):
  def __init__(self,x,y):
    super().__init__()
    self.x = x
    self.y = y
  
  def jump(self,dx,dy):
    self.x += dx
    self.y += dy
  
  def __str__(self):
    return f"I am kangaroo located at coordinates ({self.x},{self.y})"

k = Kangaroo(0,0)
print(k)
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
k.pouch_contents()
k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)



## Question 4
print("****************************************")
print("\n Question 4")

def collatz(n):
  print(n)
  if n==1:
    return
  if n%2==0:
    collatz(n//2)
  else:
    collatz((n*3)+1)
collatz(10)



## Question 5
print("****************************************")
print("\n Question 5")

def binary(n):
  if n == 0:
    return 0
  no = binary(n//2)
  return n % 2 + 10 * no
   

print(binary(0))
print(binary(1))
print(binary(3))  
print(binary(9))


## Question 6
print("****************************************")
print("\n Question 6")

from html.parser import HTMLParser
from bs4 import BeautifulSoup
infile = open("D:/BDAT/1004/problem 2/w3c.html")
content = infile.read()
infile.close()
hp = HTMLParser()
hp.feed(content)

# Creating a BeautifulSoup object and specifying the parser
Parse = BeautifulSoup(content, 'lxml')
  
# Printing the name
heading_tags = ["h1", "h2"]
for tags in Parse.find_all(heading_tags):
    print(tags.text.strip(),end='\n ')
    
    
    
## Question 7
print("****************************************")
print("\n Question 7")
        
from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup
def webdir(url,depth,indent):
  if depth ==0:
    return 
  print(" "*indent+ f"{url}")
  req = Request(url)
  html_page = urlopen(req)
  soup = BeautifulSoup(html_page, "lxml")
  links = []
  for link in soup.findAll('a'):
    #print(link,type(link))
    if link.get('href') and 'https' ==  link.get('href')[:5]:
      links.append(link.get('href'))
  #print(links)
  for link in links:
    webdir(link,depth-1,indent+1)

#webdir('https://www.webscraper.io/test-sites/e-commerce/static', 3, 0)





## Question 8
print("****************************************")
print("\n Question 8")



## Question 9
print("****************************************")
print("\n Question 9")

words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print([word.upper() for word in words ])
print([word.lower() for word in words ])
print([len(word) for word in words ])
print([[word.upper(),word.lower(),len(word)] for word in words ])
print([word for word in words if len(word)>=4])  

