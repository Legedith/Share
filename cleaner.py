#-*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:36:19 2019
@author: DSC
"""
import json
import csv

csvf = open('icc.csv','w', encoding = 'utf-8',newline='')
writer = csv.writer(csvf)
writer.writerow(['created_at'  ,'id_tweet  ','text  ','in_reply_to_screen_name  ','in_reply_to_user_id'  ,'original_tweet_id','coordinates '    ,'retweet'  ,'favorite  ','user id'  ,'Username'  ,'screen_name'  ,'location ' ,'description  ','verified  ','follower  ','friend  ','user list'  ,'favorite'  ,'status'  ,'created'  ,'hastags'])
with open('data_icc.json') as json_file:
    data = json.load(json_file)
created_at = []
id_tweet = []
text = []
in_reply_to_screen_name = []
in_reply_to_user_id = []
in_reply_to_status_id=[]
coordinates = []

retweet = []
favorite = []
Uid = []
Uname = []
Uscreen_name = []
Ulocation = []
Udescription = []
Uverified = []
Ufollower = []
Ufriend = []
Ulist = []
Ufav = []
Ustatus = []
Ucreated = []
Ehastags = []
for i in data:
    created_at.append(i['created_at'])
    id_tweet.append(i['id'])
    text.append(i["text"])
    in_reply_to_screen_name.append(i["in_reply_to_screen_name"])
    in_reply_to_user_id.append(i["in_reply_to_user_id"])
    in_reply_to_status_id.append(i["in_reply_to_status_id"])
    coordinates.append(i["coordinates"])
    retweet.append(i["retweet_count"])
    favorite.append(i["favorite_count"])
    Uid.append(i["user"]["id"])
    Uname.append(i["user"]["name"])
    Uscreen_name.append(i["user"]["name"])
    Ulocation.append(i["user"]["location"])
    Udescription.append(i["user"]['description'])
    Uverified.append(i["user"]["verified"])
    Ufollower.append(i["user"]["followers_count"])
    Ufriend.append(i["user"]["friends_count"])
    Ulist.append(i["user"]["id"])
    Ufav.append(i["user"]["favourites_count"])
    Ustatus.append(i["user"]["statuses_count"])
    Ucreated.append(i["user"]["created_at"])
    Ehastags.append(i["entities"]["hashtags"])

for q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c in zip(created_at  ,id_tweet  ,text  ,in_reply_to_screen_name  ,in_reply_to_user_id  ,in_reply_to_status_id,coordinates  ,retweet  ,favorite  ,Uid  ,Uname  ,Uscreen_name  ,Ulocation  ,Udescription  ,Uverified  ,Ufollower  ,Ufriend  ,Ulist  ,Ufav  ,Ustatus  ,Ucreated  ,Ehastags):
    row = [q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c]
    writer.writerow(row)
    print(row)
