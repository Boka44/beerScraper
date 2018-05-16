import requests
from bs4 import BeautifulSoup

print("Enter beer: ")
beer = input()

url = "https://untappd.com/search?q=%s" % (beer)

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")

list = soup.find(class_="results-container")

name = list.find(class_="name")

brewery = list.find(class_="brewery")

style = list.find(class_="style")

textName = name.text.strip()

textBrewery = brewery.text.strip()

textStyle = style.text.strip()
print("Most Popular")
print(textName,textBrewery,textStyle)

def nextBeer(count):

	list = soup.select(".beer-item")

	# print(list[1])

	name = list[count].find(class_="name")

	brewery = list[count].find(class_="brewery")

	style = list[count].find(class_="style")

	textName = name.text.strip()

	textBrewery = brewery.text.strip()

	textStyle = style.text.strip()
	print("Next Most Popular")
	print(textName,textBrewery,textStyle)
	print("Is this what you are looking for?")
	check = input("Y or N: ")
	if check != "Y" and check != "N":
		print("Must be Y or N")
		check = input("Try again: ")
	if check == "Y":
		print("Thanks!")
	if check == "N":
		count += 1
		return nextBeer(count)

count = 1
print("Is this what you are looking for?")
check = input("Y or N: ")
if check != "Y" and check != "N":
	print("Must be Y or N")
	check = input("Try again: ")
if check == "Y":
	print("Thanks!")
if check == "N":
	nextBeer(count)
