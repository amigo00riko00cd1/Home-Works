from django.shortcuts import render, redirect

strings = {
    "EN" : "We are the champions, my friends And we'll keep on fighting till the end",
    "FR" : "Nous sommes les champions, mes amis, et nous continuerons à nous battre jusqu'au bout.",
    "DE" : "Wir sind die Champions, meine Freunde, und wir werden bis zum Ende weiterkämpfen.",
    "ES" : "Somos los campeones, amigos míos, y seguiremos luchando hasta el final."
}

def index(request, language = "EN"):

    
    string = strings.get(str.upper(language))
    if string == None:
        return redirect("/string")

    return render(request, 'index/index.html', {"string" : string})


