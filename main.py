# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:48:36 2018

@author: nisar
"""
import requests
import time
import multiprocessing as mp
#import threading




def fetch(urls, reward_lst):
    for url in urls:
        json_data = requests.get(url).json()
        try:

            children = list(set(json_data['children'])) #No duplicates
            for i in children:
                urls.append(i)
        except:
            print('Tree end')

        reward = json_data['reward']
        reward_lst.append(reward)


def run():
    core_num = mp.cpu_count()
    bucket_size = (len(urls)//core_num) + 1
    reward_lst = mp.Manager().list()
    jobs = []
    for i in range(core_num):
        url_bucket = urls[i*bucket_size,(i+1)*bucket_size]
        p = mp.process(target=fetch, args=(url_bucket,reward_lst,))
        p.start()
        jobs.append(p)
    [p.join() for p in jobs]
    
    

    
#reward_list = []
urls = []
reward_lst = []
input_url = 'http://algo.work/interview/a'
urls.append(input_url)

start = time.time()

if __name__ == '__main__':
    processes = [mp.Process(target=fetch, args=(urls,reward_lst)) for x in range (4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
   
#for url in next_url:
 #   fetch(url)
 
#t = threading.Thread(target = fetch, args = (next_url,))
 
#t.start()
#t.join()

#print(next_url)
#print(reward_list)
#final_ans = sum(reward_lst)

end = time.time()
print('Time = ' + str(end-start))
'''
print()
print('****************************************')
print('The toal sum of rewards is = ' + str(final_ans))
print('****************************************')
print('Time = ' + str(end-start))
'''