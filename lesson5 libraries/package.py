import cowsay
import sys
import requests
import json

def main():
    #call_cowsay()
    call_api()


#def call_cowsay():
#    if len(sys.argv) == 2:
#        cowsay.cow("hello, " + sys.argv[1])
#        cowsay.trex("hello, " + sys.argv[1])

def call_api():
    if len(sys.argv) != 2:
        sys.exit()
        
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
    #print(json.dumps(response.json(), indent=2))
    #print (response.json()["results"][0]["trackName"])

    o = response.json()

    for result in o["results"]:
        print(result["trackName"])

if __name__=="__main__":
    main()