from bs4 import BeautifulSoup
from googletrans import Translator
import mysql.connector

def season(htmlstring12):
    soup = BeautifulSoup(htmlstring12, 'html.parser')
    teams_list = []
    wins_quality = []
    draw_quality = []
    lose_quality = []
    goals_and_conceded=[]
    scoring_goals=[]
    conceded_goals=[]
    goals_1=[]
    points_list1=[]
    translator=Translator()
    # Find all <tr> tags
    tr_tags = soup.find_all("tr")

    # Extract team names and win counts
    for tr_tag in tr_tags:
        td_tags = tr_tag.find_all("td")
        if len(td_tags) > 1:
            # Extract team name and translate
            team_name_tag = td_tags[1].find("a")
            if team_name_tag:
                team_name = team_name_tag.text.strip()
                translation = translator.translate(team_name, src='ru', dest='en')
                translated_team_name = translation.text
                teams_list.append(translated_team_name)
                
            # Extract win count
            wins_tag = td_tags[3]
            if wins_tag:
                wins = wins_tag.text.strip()
                wins_quality.append(wins)
            draw_tag = td_tags[4]
            if draw_tag:
                draw = draw_tag.text.strip()
                draw_quality.append(draw)
            loses_tag = td_tags[5]
            if loses_tag:
                lose = loses_tag.text.strip()
                lose_quality.append(lose)
            goals_tag = td_tags[6]    
            if goals_tag:
                goals = goals_tag.text.strip()
                goals_and_conceded.append(goals)  
            points_tag = td_tags[7]    
            if points_tag:
                points = points_tag.text.strip()
                points_list1.append(points)           

    print(teams_list)
    wins_quality.pop(0)
    wins_list=[int(item) for item in wins_quality]
    print(wins_list)
    draw_quality.pop(0)
    draw_list=[int(item) for item in draw_quality]
    print(draw_list)
    lose_quality.pop(0)
    lose_list=[int(item) for item in lose_quality]
    print(lose_list)
    goals_and_conceded.pop(0)
    for item in goals_and_conceded:
        number=item.split('-')
        goals_1.append(number)
    for item in  goals_1:
        scoring_goals.append(item[0])
        conceded_goals.append(item[1])
    scoring_goals_list=[int(item) for item in scoring_goals]    
    print(scoring_goals_list)
    conceded_goals_list=[int(item) for item in conceded_goals]    
    print(conceded_goals_list) 
    points_list1.pop(0)
    points_list=[int(item) for item in points_list1]
    print(points_list)   
            # Connecting to MySQL
    # cnx = mysql.connector.connect(user='developer', password='1562473890Abc_',
    #                               host='127.0.0.1', database='epl')
    # cursor = cnx.cursor()  
    # # Insert data into the database
    # for i in range(len(teams_list)):
    #     sql = """INSERT INTO season2011_2012 (TeamName, Wins, Draws, Loses, Goals, Conceded, Points)
    #              VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    #     val = (teams_list[i].lower(), wins_list[i], draw_list[i], lose_list[i], scoring_goals_list[i], conceded_goals_list[i], points_list[i])
    #     cursor.execute(sql, val)

    # # Commit the transaction
    # cnx.commit()

    # # Close the cursor and connection
    # cursor.close()
    # cnx.close()

    # print("Data inserted successfully")
    return teams_list[0],points_list[0]
  
