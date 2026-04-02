import json
import requests

api_key='27fb1db1'

def highlight(word: str, sentence: str) -> str:
    import re

    return re.sub(re.escape(word), f"**{word}**", sentence, flags=re.IGNORECASE)


#To get movie data
def get_movie_data(name: str) -> dict:
    params_dict={}
    params_dict['apikey']=api_key
    params_dict['t']=name
    params_dict['r']='json'
    movie_resp= requests.get("http://www.omdbapi.com/",params=params_dict)
    #print (movie_resp.url)
    return movie_resp.json()


#To get the Rotten Tomatoes rating score
def rt_rating(movie_data: dict) -> int:
    
    for rating in movie_data['Ratings']:
        if 'Rotten Tomatoes' in rating['Source']:
            result= rating['Value']
            #result= result.replace('%', '')  #To remove percentage
            return (result)
        
    return -1

#To get all jokes based on movie's plot
def get_joke_data(joke: str) -> dict:
    joke_dict={}
    joke_dict['term']=joke
    joke_dict['limit']=2
    headers = {'Accept': 'application/json'}
    joke_resp= requests.get("https://icanhazdadjoke.com/search", params=joke_dict, headers=headers)
    #print (joke_resp.url)
    #joke_data_resp= json.loads(joke_resp.text)#
    #print (json.dumps(joke_data_resp, indent=2))
    
    return joke_resp.json()


def get_jokes(plot: str, verbosity=0) -> tuple[str, list[str]]:
    
    new_words = plot.split()  # split into separate words
    #print (words)
    words=[]
    for w in new_words:
        clean_word= w.strip(",.!;:")
        words.append(clean_word)
    sorted_words= sorted(words, key= lambda word_length: len(word_length), reverse=True)
    #sorted_words= sorted(words, key= lambda word_length: (-len(word_length),word_length) )
    #print (sorted_words)
   

    for joke_data in sorted_words:
        associated_jokes= get_joke_data(joke_data)
        #print (json.dumps(associated_jokes, indent=2))
        
        if len(associated_jokes['results'])>0:
            joke_list=[]
            for all_joke in associated_jokes['results']:
                all_jokes= all_joke['joke']
                joke_list.append(all_joke['joke'])
                
            
            return (joke_data, joke_list)
        
    return (None, None)


def haha_me(movie_title: str, verbosity=0) -> str:
    

    movie_results= get_movie_data(movie_title)
    
    #Check if movie found
    if movie_results['Response']=='False':
        message= "No movie found:" + movie_title
        return message
    
    score_result= rt_rating(movie_results)
    plot_result= movie_results['Plot']
    joke_result= get_jokes(plot_result)
    highlight_result= highlight(joke_result[0], plot_result)
    
    #print (highlight_result)
    
 
    #Movie found with no jokes
    if movie_results['Response']=='True' and joke_result[0] is None:
        message= "I've got no jokes about this movie. It's too serious!"
        return message
  
    #Movie found with jokes
    movie_message=''
    
    if score_result==-1:
        movie_message= "Hope you like them!"
        score_result='-1'
        
    
    else:
        percent_result= score_result.replace('%', '')
        percent_result= int(percent_result)
        
        if percent_result >=70:
            movie_message= "Hope they're as good as the movie!"

        else:
            movie_message= "Hope they're better than the movie!"
        
    aggregated_jokes= '\n'.join(joke_result[1])
    print (aggregated_jokes)

    
    message= (movie_results['Title'] + '\n'+ 
              "Rotten Tomatoes rating:" + ' ' + 
              score_result +'\n' + highlight_result + '\n'+ 
              "Speaking of **" + joke_result[0]+ "**, that reminds me of some jokes."+ '\n' + 
              movie_message + '\n\n' + highlight(joke_result[0], aggregated_jokes))
    
    
    return message.rstrip()

#final_Result= (haha_me("Namak Halaal"))
final_Result= haha_me("Sherlock Holmes")
print (final_Result)