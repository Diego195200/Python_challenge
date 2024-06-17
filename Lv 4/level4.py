import urllib.request as req

# open the first link with the first nothing
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579"  # we start with this url
old_nothing = '63579'  # a variable to track the number
for _ in range(400):  # simulates the enter of a link
    url_access = req.urlopen(url)  # open the page
    text = str(url_access.read())  # get the text in that page
    new_nothing = ''.join(filter(str.isdigit, text))  # here we are searching just for numbers in the text
    url = url.replace(old_nothing, new_nothing)
    old_nothing = new_nothing
    print(f'number {_}')
    print(url)
    print(text)
    print(new_nothing)



# answer: peak.html

