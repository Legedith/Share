# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:36:19 2019

@author: DSC
"""
import json

with open('file.json') as json_file:
    data = json.load(json_file)
created_at = []
id_tweet = []
text = []
in_reply_to = []
in_reply_to_user_id = []
coordinates = []
reply =  []
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
for i in data:
    created_at.append(i['created_at'])
    id_tweet.append(i['id'])
    