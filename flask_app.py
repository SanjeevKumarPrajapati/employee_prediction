from flask import Flask,render_template,request
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,classification_report
df=pd.read_csv("data.csv")
y=df["Your profession( 0 for teaching or 1 for Industry)"]
X=df.drop("Your profession( 0 for teaching or 1 for Industry)",axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=53)
rf=RandomForestClassifier(random_state=53,n_estimators=100)
rf.fit(X_train,y_train)
y_pred=rf.predict(X_test)
app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        name=request.form.get("your_name")
        phone_number=request.form.get("phone_number")
        dept=request.form.get("dept")
        number_of_year=request.form.get("number_of_year")
        higest_number_of_year=request.form.get("higest_number_of_year")
        experience_in_year_teaching=request.form.get("experience_in_year_teaching")
        experience_in_year_industry=request.form.get("experience_in_year_industry")
        tenth_percentage=request.form.get("tenth_percentage")
        twelveth_percentage=request.form.get("twelveth_percentage")
        graduation_percentage=request.form.get("graduation_percentage")
        post_graduate_percentage=request.form.get("post_graduate_percentage")
        doctoral_percentage=request.form.get("doctoral_percentage")
        worked_on_any_project=request.form.get("worked_on_any_project")
        how_many_project=request.form.get("how_many_project")
        how_many_years=request.form.get("how_many_years")
        group_discussion=request.form.get("group_discussion")
        team_leader=request.form.get("team_leader")
        read_books=request.form.get("read_books")
        how_many_friends=request.form.get("how_many_friends")
        how_many_members=request.form.get("how_many_members")
        phone_number=request.form.get("phone_number")
        states_you_have=request.form.get("states_you_have")
        countries_you_have=request.form.get("countries_you_have")
        how_many_students=request.form.get("how_many_students")
        how_many_research=request.form.get("how_many_research")
        how_many_conferences=request.form.get("how_many_conferences")
        feedback=request.form.get("feedback")
        think_about_your_family=request.form.get("think_about_your_family")
        how_many_games=request.form.get("how_many_games")
        X_new=pd.DataFrame(columns=["Number of year you have worked in current organization","Highest number of years you have worked in any organization","Experience in year(Teaching)","Experience in year(Industry)","10th percentage","12th percentage","Graduation percentage","Post Graduation percentage","Doctoral percentage","Worked on any project(technical or non-technical) ( 0 for no and 1 for yes)","How many projects you have completed successfully(technical or non-technical)","How many years, you lived outside your house","Participated any group discussion(City, State, National or international level) ( 0 for no and 1 for yes)","Can you became a team leader? ( 0 for no and 1 for yes)","How many hours you read books per day.","How many friends you have.","How many members of your family depends on you(financially)","Tell us count of phone numbers you have saved in your mobile.","How many states you have travelled in India.","How many countries you have visited.","How many students you have guided.","How many research papers you have published.","How many conferences you have attend.","Can you think feedback is necessary against you. ( 0 for no and 1 for yes)","Numbers of times in day, you think about your family.","How many games you have in your phone."],data=[[int(number_of_year),int(higest_number_of_year),int(experience_in_year_teaching),int(experience_in_year_industry),float(tenth_percentage),float(twelveth_percentage),float(graduation_percentage),float(post_graduate_percentage),int(doctoral_percentage),int(worked_on_any_project),int(how_many_project),int(how_many_years),int(group_discussion),int(team_leader),float(read_books),float(how_many_friends),int(how_many_members),int(phone_number),int(states_you_have),int(countries_you_have),float(how_many_students),int(how_many_research),float(how_many_conferences),int(feedback),float(think_about_your_family),int(how_many_games)]])
        a=rf.predict(X_new)
        """
        if a[0]==0:
            message=client.messages.create(
                to='+917900990614',
                from_='+18454078079',
                body="Name :- {} \n Phone Number :- {} \n Department :- {} \n Number of year you have worked in current organization :- {} \n Highest number of years you have worked in any organization :- {} \n Experience in year(Teaching) :- {} \n  Experience in year(Industry) :- {} \n 10th percentage :- {} \n 12th percentage :- {} \n Graduation percentage :- {} \n Post Graduation percentage :- {} \n Doctoral percentage :- {} \n Worked on any project(technical or non-technical) ( 0 for no and 1 for yes) :- {} \n How many projects you have completed successfully(technical or non-technical) :- {} \n How many years, you lived outside your house :- {} \n Participated any group discussion(City, State, National or international level) ( 0 for no and 1 for yes) :- {} \n Can you became a team leader? ( 0 for no and 1 for yes) :- {} \n How many hours you read books per day :- {} \n How many friends you have :- {} \n How many members of your family depends on you(financially) :- {} \n Tell us count of phone numbers you have saved in your mobile :- {} \n How many states you have travelled in India :- {} \n How many countries you have visited :- {} \n How many students you have guided :- {} \n How many research papers you have published :- {} \n How many conferences you have attend :- {} \n Can you think feedback is necessary against you ( 0 for no and 1 for yes) :- {} \n Numbers of times in day, you think about your family :- {} \n How many games you have in your phone :- {} ".format(name,phone_number,dept,int(number_of_year),int(higest_number_of_year),int(experience_in_year_teaching),int(experience_in_year_industry),float(tenth_percentage),float(twelveth_percentage),float(graduation_percentage),float(post_graduate_percentage),int(doctoral_percentage),int(worked_on_any_project),int(how_many_project),int(how_many_years),int(group_discussion),int(team_leader),float(read_books),float(how_many_friends),int(how_many_members),int(phone_number),int(states_you_have),int(countries_you_have),float(how_many_students),int(how_many_research),float(how_many_conferences),int(feedback),float(think_about_your_family),int(how_many_games))
                )
            return render_template("0.html")
        """
        if a[0]==0:
            return render_template("0.html")
        else:
            return render_template("1.html")
        return render_template("prediction.html")
    return render_template("prediction.html")
if __name__=='__main__':
    app.run()

