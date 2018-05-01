# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:48:36 2018

@author: nisar
"""
import requests
import time
#import multiprocessing
#import threading

def fetch(url):
    
    ''' Takes the url as the input. Returns JSON and extracts 'children' and 'reward' values. '''

    #print()
    json_data = requests.get(url).json()
    try:
        
        children = list(json_data['children']) #No duplicate children
 
        for i in children:
            next_url.append(i)
    except:
        print('Tree end')
    #global reward
    reward = json_data['reward']
    '''
    print()
    print('Children = ' + str(children))
    print()
    print('Reward = ' + str(reward))
    '''
    #global reward_list
    reward_list.append(reward)
    
    #return list(next_url), children, reward

reward_list = []
next_url = []

input_url = 'http://algo.work/interview/a'
next_url.append(input_url)

start = time.time()

for url in next_url:
    fetch(url)
 
#t = threading.Thread(target = fetch, args = (next_url,))
 
#t.start()
#t.join()

#print(next_url)
#print(reward_list)
final_ans = sum(reward_list)

end = time.time()

print()
print('****************************************')
print('The toal sum of rewards is = ' + str(final_ans))
print('****************************************')
print('Time = ' + str(end-start))
