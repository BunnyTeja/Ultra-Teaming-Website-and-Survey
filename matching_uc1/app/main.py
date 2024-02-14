# importing module
from pandas import *
import re
import csv

path = "data/names.csv"
names_data = read_csv(path)
# converting column data to list
names = names_data['researcher_name'].tolist()

from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# assume that you have defined the variable `names` somewhere

@app.route('/')
def index():
    return render_template("matching.html", names=names)

@app.route('/', methods=["POST"])
def getValue():
    it = request.form["inputtext"]
    input_method = request.form["methods"]
    input_teams = request.form["teams"]
    input_results = request.form["results"]

    if it in names and input_method == 'M0: Random Matching':
        with open('data/teaming_uc1_m0.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
 
            # initialize an empty list to store proposal IDs
            proposal_ids_for_it = []
            proposal_titles_for_it = []
            proposal_links_for_it = []
            proposal_years_for_it = []
            proposal_teams_for_it = []
            goodness_score_for_it = []
            temp_team = []
            # proposal_skills_for_it = []
            print(input_results)
            print(type(input_results))
            print(input_teams)
            print(type(input_teams))
            # loop through each row in the CSV file
            for row in reader:
                # check if the value in the 'researcher_name' column matches the desired value
                if row['researcher_name'] == it:
                    # add the proposal ID to the list
                  if len(proposal_ids_for_it) < int(input_results): # extracts top 5 results
                    proposal_ids_for_it.append(row['proposal_id'])
                    proposal_titles_for_it.append(row['title'])
                    proposal_links_for_it.append(row['proposal_link'])
                    proposal_years_for_it.append(row['year'])
                    proposal_teams_for_it.append(row['team'])
                    goodness_score_for_it.append(row['goodness'])
                    proposal_skills_for_it = (row['skills'])
                  else:
                    # stop the loop if the list has at least 3 IDs for this researcher
                    break
            
            
            proposal_teams_for_it = [eval(item) for item in proposal_teams_for_it]
            
            new_team_list = [inner_list[:int(input_teams)] for inner_list in proposal_teams_for_it]
            # print(new_team_list)
            
            new_gscore_list = []
            new_gscore_list = [list(map(float, x.strip('][').split(', ')))[:int(input_teams)] for x in goodness_score_for_it]
            print(new_gscore_list)

        return render_template("matching.html", name=it, length=len(proposal_ids_for_it), my_range=range(len(proposal_ids_for_it)), names=names, nsfids=proposal_ids_for_it, nsftitles=proposal_titles_for_it, nsflinks=proposal_links_for_it, years=proposal_years_for_it, itext=it, teams=new_team_list, method=input_method, gscore=new_gscore_list, no_of_teams=int(input_teams), no_of_results=int(input_results), skills = proposal_skills_for_it)
        
    


    elif it in names and input_method == 'M1: String Matching':
        with open('data/teaming_uc1_m1.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
 
            # initialize an empty list to store proposal IDs
            proposal_ids_for_it = []
            proposal_titles_for_it = []
            proposal_links_for_it = []
            proposal_years_for_it = []
            proposal_teams_for_it = []
            goodness_score_for_it = []
            temp_team = []
            # proposal_skills_for_it = []
            print(input_results)
            print(type(input_results))
            print(input_teams)
            print(type(input_teams))
            # loop through each row in the CSV file
            for row in reader:
                # check if the value in the 'researcher_name' column matches the desired value
                if row['researcher_name'] == it:
                    # add the proposal ID to the list
                  if len(proposal_ids_for_it) < int(input_results): # extracts top 5 results
                    proposal_ids_for_it.append(row['proposal_id'])
                    proposal_titles_for_it.append(row['title'])
                    proposal_links_for_it.append(row['proposal_link'])
                    proposal_years_for_it.append(row['year'])
                    proposal_teams_for_it.append(row['team'])
                    goodness_score_for_it.append(row['goodness'])
                    proposal_skills_for_it = (row['skills'])
                  else:
                    # stop the loop if the list has at least 3 IDs for this researcher
                    break
            
            
            proposal_teams_for_it = [eval(item) for item in proposal_teams_for_it]
            
            new_team_list = [inner_list[:int(input_teams)] for inner_list in proposal_teams_for_it]
            # print(new_team_list)
            
            new_gscore_list = []
            new_gscore_list = [list(map(float, x.strip('][').split(', ')))[:int(input_teams)] for x in goodness_score_for_it]
            print(new_gscore_list)

        return render_template("matching.html", name=it, length=len(proposal_ids_for_it), my_range=range(len(proposal_ids_for_it)), names=names, nsfids=proposal_ids_for_it, nsftitles=proposal_titles_for_it, nsflinks=proposal_links_for_it, years=proposal_years_for_it, itext=it, teams=new_team_list, method=input_method, gscore=new_gscore_list, no_of_teams=int(input_teams), no_of_results=int(input_results), skills = proposal_skills_for_it)
   
    elif it in names and input_method == 'M2: Semantic Matching':
        with open('data/teaming_uc1_m2.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
 
            # initialize an empty list to store proposal IDs
            proposal_ids_for_it = []
            proposal_titles_for_it = []
            proposal_links_for_it = []
            proposal_years_for_it = []
            proposal_teams_for_it = []
            goodness_score_for_it = []
            temp_team = []
            # proposal_skills_for_it = []
            print(input_results)
            print(type(input_results))
            print(input_teams)
            print(type(input_teams))
            # loop through each row in the CSV file
            for row in reader:
                # check if the value in the 'researcher_name' column matches the desired value
                if row['researcher_name'] == it:
                    # add the proposal ID to the list
                  if len(proposal_ids_for_it) < int(input_results): # extracts top 5 results
                    proposal_ids_for_it.append(row['proposal_id'])
                    proposal_titles_for_it.append(row['title'])
                    proposal_links_for_it.append(row['proposal_link'])
                    proposal_years_for_it.append(row['year'])
                    proposal_teams_for_it.append(row['team'])
                    goodness_score_for_it.append(row['goodness'])
                    proposal_skills_for_it = (row['skills'])
                  else:
                    # stop the loop if the list has at least 3 IDs for this researcher
                    break
            
            
            proposal_teams_for_it = [eval(item) for item in proposal_teams_for_it]
            
            new_team_list = [inner_list[:int(input_teams)] for inner_list in proposal_teams_for_it]
            # print(new_team_list)
            
            new_gscore_list = []
            new_gscore_list = [list(map(float, x.strip('][').split(', ')))[:int(input_teams)] for x in goodness_score_for_it]
            print(new_gscore_list)

        return render_template("matching.html", name=it, length=len(proposal_ids_for_it), my_range=range(len(proposal_ids_for_it)), names=names, nsfids=proposal_ids_for_it, nsftitles=proposal_titles_for_it, nsflinks=proposal_links_for_it, years=proposal_years_for_it, itext=it, teams=new_team_list, method=input_method, gscore=new_gscore_list, no_of_teams=int(input_teams), no_of_results=int(input_results), skills = proposal_skills_for_it)
   
    elif it in names and input_method == 'M3: Boosted Bandit Matching':
      with open('data/teaming_uc1_m3.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
 
            # initialize an empty list to store proposal IDs
            proposal_ids_for_it = []
            proposal_titles_for_it = []
            proposal_links_for_it = []
            proposal_years_for_it = []
            proposal_teams_for_it = []
            goodness_score_for_it = []
            temp_team = []
            # proposal_skills_for_it = []
            print(input_results)
            print(type(input_results))
            print(input_teams)
            print(type(input_teams))
            # loop through each row in the CSV file
            for row in reader:
                # check if the value in the 'researcher_name' column matches the desired value
                if row['researcher_name'] == it:
                    # add the proposal ID to the list
                  if len(proposal_ids_for_it) < int(input_results): # extracts top 5 results
                    proposal_ids_for_it.append(row['proposal_id'])
                    proposal_titles_for_it.append(row['title'])
                    proposal_links_for_it.append(row['proposal_link'])
                    proposal_years_for_it.append(row['year'])
                    proposal_teams_for_it.append(row['team'])
                    goodness_score_for_it.append(row['goodness'])
                    proposal_skills_for_it = (row['skills'])
                  else:
                    # stop the loop if the list has at least 3 IDs for this researcher
                    break
            
            
            proposal_teams_for_it = [eval(item) for item in proposal_teams_for_it]
            
            new_team_list = [inner_list[:int(input_teams)] for inner_list in proposal_teams_for_it]
            # print(new_team_list)
            
            new_gscore_list = []
            new_gscore_list = [list(map(float, x.strip('][').split(', ')))[:int(input_teams)] for x in goodness_score_for_it]
            print(new_gscore_list)

      return render_template("matching.html", name=it, length=len(proposal_ids_for_it), my_range=range(len(proposal_ids_for_it)), names=names, nsfids=proposal_ids_for_it, nsftitles=proposal_titles_for_it, nsflinks=proposal_links_for_it, years=proposal_years_for_it, itext=it, teams=new_team_list, method=input_method, gscore=new_gscore_list, no_of_teams=int(input_teams), no_of_results=int(input_results), skills = proposal_skills_for_it)