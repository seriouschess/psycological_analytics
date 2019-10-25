from django.shortcuts import render, redirect
from .models import Survey
from django.contrib import messages
from apps.login_app.models import User

def index(request):
    if "user_id" in request.session:
        context={
            "user":User.objects.get(id=request.session["user_id"])
        }
        return render(request, 'survey_app/index.html', context)
    else:
        return redirect("/")

def disclaimer(request):
    return render(request, 'survey_app/disclaimer.html')

def newSurveyA(request):
    if "user_id" in request.session:
        try:
            del request.session["anxiety_int"]
            del request.session["lifestyle_int"]
            del request.session["confidence_int"]
            del request.session["happy_int"]
            del request.session["time"]
            del request.session["clicks"]
            del request.session["keys_pressed"]
        except:
            pass

        if request.method == "POST":
            request.session["anxiety_int"] = request.POST["anxiety_int"]
            request.session["lifestyle_int"] = request.POST["lifestyle_int"]
            request.session["confidence_int"] = request.POST["confidence_int"]
            request.session["happy_int"] = request.POST["happy_int"]
            request.session["time"] = int(request.POST["time"])
            request.session["clicks"] = int(request.POST["clicks"])
            request.session["keys_pressed"] = int(request.POST["keys_pressed"])
            return redirect("/survey/new/b")
        context = {
            "ten":[1,2,3,4,5,6,7,8,9,10], #you impress me django
            "user":User.objects.get(id=request.session["user_id"])
        }
        return render(request, 'survey_app/new_survey_a.html', context)
    else:
        return redirect("/")

def newSurveyB(request):
    if "user_id" in request.session:
        if "anxiety_int" not in request.session: #no cutting in line omg
            return redirect("/survey/new/a")
        if request.method =="POST":
            if int(request.POST["keys_pressed"]) < 20: #bad copy-paster
                messages.error(request, "Do actually type the message instead of using copy-paste.")
                return redirect("/survey/new/b")
            current_user = User.objects.get(id=request.session["user_id"])

            if current_user.surveyed:
                pass #don't clog my database!
            else:
                current_user.surveyed = True;
                current_user.save()
                Survey.objects.create(user = current_user,anxiety_rating = request.session["anxiety_int"], lifestyle_rating= request.session["lifestyle_int"], confidence_rating=request.session["confidence_int"], happy_rating=request.session["happy_int"], survey_time= request.session["time"]+int(request.POST["time"]), survey_clicks= request.session["clicks"]+int(request.POST["clicks"]), survey_keypress=request.session["keys_pressed"]+int(request.POST["keys_pressed"]), quote_replication=request.POST["text_test"], survey_backspaces=int(request.POST["backspaces"]))

            return redirect("/survey/summary/{}".format(request.session["user_id"]))
        context = {
            "ten":[1,2,3,4,5,6,7,8,9,10], #you impress me django
            "user":User.objects.get(id=request.session["user_id"]),
            "blarg":[request.session["anxiety_int"], request.session["lifestyle_int"], request.session["confidence_int"], request.session["happy_int"], request.session["time"], request.session["clicks"], request.session["keys_pressed"]]
        }
        return render(request, 'survey_app/new_survey_b.html', context)
    else:
        return redirect("/")

def user_summary(request, user_id): #one user's data
    if "user_id" in request.session:
        current_user = User.objects.get(id=user_id)
        survey = Survey.objects.filter(user=current_user)[0] #no double dips!

        #calculate number of mismatched characters
        mismatched_characters = 0;
        tyson = "Knowing how to think empowers you far beyond those who know only what to think."
        for x in range(0, len(tyson)):
            try:
                if str(survey.quote_replication[x]) == tyson[x]:
                    pass
                else:
                    mismatched_characters += 1
            except:
                mismatched_characters += 1

        context={
            "mismatched_characters": mismatched_characters,
            "user": current_user,
            "survey": survey #last value instead?
        }
        return render(request, 'survey_app/user_summary.html', context)
    else:
        return redirect("/")

def dataSummary(request): # after action report of user data
    context={
        "surveys": Survey.objects.all()
    }
    return render(request, 'survey_app/data_summary.html', context)

def analytics(request):
    surveys = Survey.objects.all()
    anxiety_happiness = [] #x left y right
    fitness_happiness = []
    confidence_happiness = []
    confidence_anxiety = []
    confidence_fitness = []
    anxiety_fitness = []
    backspaces_anxiety = []
    time_fitness = []
    clicks_confidence = []

    total_time = 0 #total time to take the survey
    total_clicks = 0
    total_keypress = 0
    total_backspaces = 0
    survey_counter = 0

    for survey in surveys:
        survey_counter += 1
        anxiety_happiness.append(survey.happy_rating) #x
        anxiety_happiness.append(survey.anxiety_rating) #y
        fitness_happiness.append(survey.lifestyle_rating)
        fitness_happiness.append(survey.happy_rating)
        confidence_happiness.append(survey.confidence_rating)
        confidence_happiness.append(survey.happy_rating)
        confidence_anxiety.append(survey.confidence_rating)
        confidence_anxiety.append(survey.anxiety_rating)
        confidence_fitness.append(survey.confidence_rating)
        confidence_fitness.append(survey.lifestyle_rating)
        anxiety_fitness.append(survey.anxiety_rating)
        anxiety_fitness.append(survey.lifestyle_rating)
        backspaces_anxiety.append(survey.survey_backspaces)
        backspaces_anxiety.append(survey.anxiety_rating)
        clicks_confidence.append(survey.survey_clicks)
        clicks_confidence.append(survey.confidence_rating)
        time_fitness.append(survey.survey_time)
        time_fitness.append(survey.lifestyle_rating)
        total_time += survey.survey_time
        total_clicks += survey.survey_clicks
        total_keypress += survey.survey_keypress
        total_backspaces += survey.survey_backspaces


    context={
        "anxiety_happiness": anxiety_happiness,
        "fitness_happiness": fitness_happiness,
        "confidence_happiness": confidence_happiness,
        "confidence_anxiety": confidence_anxiety,
        "confidence_fitness": confidence_fitness,
        "anxiety_fitness": anxiety_fitness,
        "backspaces_anxiety": backspaces_anxiety,
        "average_time": round(total_time/survey_counter,1),
        "average_clicks": round(total_clicks/survey_counter,1),
        "average_keypress": round(total_keypress/survey_counter,1),
        "average_backspaces": round(total_backspaces/survey_counter,1),
        "time_fitness": time_fitness,
        "clicks_confidence": clicks_confidence
    }
    return render(request, 'survey_app/analytics.html', context)
