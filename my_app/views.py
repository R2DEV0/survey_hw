from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey.html')

def user_info(request):
    print("form submitted")
    name = request.POST['user_name']
    location = request.POST['locations']
    language = request.POST['languages']
    comment = request.POST['comments']

    if len(name) == 0:
        name = "You need to submit a name"
    if len(comment) == 0:
        comment = "NA"
    if location == "select one":
        location = "You didn't select anything"
    if language == "select one":
        language = "You didn't select anything"

    return redirect(f"/results/{name}/{location}/{language}/{comment}")


def results(request, user_name, locations, languages, comments):
    context={
        'submittedname' : user_name,
        'submittedlocation' : locations,
        'submittedlanguage' : languages,
        'submittedcomments' : comments,
    }

    return render(request, 'result.html', context)

def backhome(request):
    return redirect('/')

