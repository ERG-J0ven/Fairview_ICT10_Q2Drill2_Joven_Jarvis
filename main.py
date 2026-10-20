from pyscript import display, document

somemath7 = {"Jibril Abdul", "Lucas Ladion", "Emmanuel Correa", "Lorissa Paragas", "Maria Bamba", "Zander Mirza"}
somemath8 = {"Rayne Maniago", "Yanis Concepcion", "Rafael De Castro", "Orange Mendoza", "Krishna Pascua","Kian Ang", "Khadija Lucman", "Hannah Galapon", "Georgina Gamponia", "Francesca Daquigan", "Anya Basuil"}
somemath9 = {"Cheree Mendoza", "Jarvis Joven", "Edrian Correa", "Francis Fernandez", "Gabrielle De Jesus", "Rohan Tabasan", "Tyler Sales"}
somemath10= {"Cheree Mendoza", "Jericho Magsalin", "Edrian Correa", "Francis Fernandez", "Phillip Ponce", "Jarvis Joven"}
mathclubavengers = somemath7 | somemath8 | somemath9 | somemath10 
mathclubber = sorted(mathclubavengers)
totalmembercounts = len(mathclubavengers)
display(f"Total Members: {totalmembercounts}\n{'\n'.join(mathclubber)}" , target="listofmathdudes")

def goinnow(e):
    document.getElementById("listofmathdudes").innerHTML = ""
    ffname = document.getElementById("fname").value
    llname = document.getElementById("lname").value
    adddude = {f"{ffname} {llname}"}
    ultimatemathclub = somemath7 | somemath8 | somemath9 | somemath10 | adddude
    coolultimatemathclub = sorted(ultimatemathclub)
    totalmembercount = len(ultimatemathclub)
    waitthisalmostwork = '\n'.join(coolultimatemathclub)
    display(f"Total Members: {totalmembercount}\n{waitthisalmostwork}" , target="listofmathdudes")



