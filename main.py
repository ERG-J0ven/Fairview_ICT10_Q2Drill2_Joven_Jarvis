from pyscript import display, document

somemath7 = {"Jibril Abdul", "Lucas Ladion", "Emmanuel Correa", "Lorissa Paragas", "Maria Bamba", "Zander Mirza"}
somemath8 = {"Rayne Maniago", "Yanis Concepcion", "Rafael De Castro", "Orange Mendoza", "Krishna Pascua","Kian Ang", "Khadija Lucman", "Hannah Galapon", "Georgina Gamponia", "Francesca Daquigan", "Anya Basuil"}
somemath9 = {"Cheree Mendoza", "Jarvis Joven", "Edrian Correa", "Francis Fernandez", "Gabrielle De Jesus", "Rohan Tabasan", "Tyler Sales"}
somemath10= {"Cheree Mendoza", "Jericho Magsalin", "Edrian Correa", "Francis Fernandez", "Phillip Ponce", "Jarvis Joven"} #the 4 sets 
mathclubavengers = somemath7 | somemath8 | somemath9 | somemath10 #union them so that duplicate elements are excluded
mathclubber = sorted(mathclubavengers) #sorts them alphabetically
totalmembercounts = len(mathclubavengers) #gets the total number of people
display(f"Total Members: {totalmembercounts}\n{'\n'.join(mathclubber)}" , target="listofmathdudes") #displays the initial amount and members before we add a new dude, \n is used to seperate the elements and it also removes the brackets, commas and quotation marks to make it more aesthetically pleasing

def goinnow(e):
    document.getElementById("listofmathdudes").innerHTML = "" #clears the previous result
    ffname = document.getElementById("fname").value
    llname = document.getElementById("lname").value #grabs the value of what the user typed in the textbox
    adddude = {f"{ffname} {llname}"} #f string combines these 2 variables into 1
    ultimatemathclub = somemath7 | somemath8 | somemath9 | somemath10 | adddude #same as line 7 but union the new dude along with it
    coolultimatemathclub = sorted(ultimatemathclub) 
    totalmembercount = len(ultimatemathclub) #gets the new amount
    waitthisalmostwork = '\n'.join(coolultimatemathclub) #\n is just <br> but for strings (https://www.geeksforgeeks.org/python/python-line-break-in-string/) and because doing <br> didnt work i had to do \n.join(coolultimatemathclub) so that it can add new lines
    display(f"Total Members: {totalmembercount}\n{waitthisalmostwork}" , target="listofmathdudes") #displays the output, again using \n as a br.



