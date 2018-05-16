
# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages

'''
This algorithm takes a URL as an inout (without quotes) and returns the sum of reaward values that are fetched from the URL and its URL children.

For example:
    Input = http://www.xyz.com/
    Output = 155
'''

import threading
import queue
import requests
import time

def fetch_worker(url_q, reward_list):
    while True:
        try:
            url = url_q.get()

            # controller requests exit
            if url is None:
                return

            # get json data
            json_data = requests.get(url).json()

            # queue more url_q tasks
            for child in json_data.get('children', []): 
                url_q.put(child)

            # add reward to list
            reward_list .append(json_data['reward'])
        finally:
            url_q.task_done()



def fetch(url):
    NUM_WORKERS = 96  # Not much improvement from 64, not too bad compared to 128.
    reward_list = []
    url_q = queue.Queue()
    threads = [threading.Thread(target=fetch_worker, args=(url_q, reward_list))
        for _ in range(NUM_WORKERS)]
    for t in threads:
        t.start()
    url_q.put(url)
    # wait for url and all subordinate urls to process
    url_q.join()
    # kill the workers
    for _ in range(NUM_WORKERS):
        url_q.put(None)
    for t in threads:
        t.join()
    return sum(reward_list)


input_url = input('Enter a URL. \n')
start = time.time()

ans = fetch(input_url)

end = time.time()

print('*************************')
print('Input URL = ' + input_url)
print('Sum of rewards =' + str(ans))
print('Time taken = ' + str(end-start))
print('*************************')
