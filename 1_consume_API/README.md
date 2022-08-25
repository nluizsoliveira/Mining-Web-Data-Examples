# Consume Open APIs
API stands for Application Programming Interface. In practice, this means a series of routes:

(ex: `user/<userId>`, `/products`, `products/<productId>`)

That provide structured data, through a well defined communication procotol (usually `HTTP`) and architecture (ex: `rest`) that can to be 
consumed by multiple clients (front-ends, mobile apps, IOT devices, etc).

![](https://i.imgur.com/b2JZgrW.png)

APIs may be intern/protected to avoid external use. But sometimes a service purposely provides data for developers.   

Examples: 

1. github
2. spotify
3. reddit 
4. twitter 

They do this to promote an "ecossitem" of third-party apps solutions related to their product in an controlled way. 

APIs usually have some **Authentication process**. From simpler to more complex: 
- No authentication at all
- Login/Password authentication
- Expiring API key 
- OAUTH with Bearer Token 

## Case: Consume League of Legends API
Riot uses an **Expiring API key** to provide API access, that can be obtained at https://developer.riotgames.com/. 

![](https://i.imgur.com/XN4bzk8.png)

## Storing API key for local development
In a perfect world, you would use a **keyvault** service to store your expiring key, such as **Azure Keyvault**.

However, for personal projects, it's enough to store it in a `.env` file that is ignored by git. Then, you can `source` your `.env` file, which will add the key to your environment variables, which can be later accessed in your python script. For instance: 

0. Add a line for `.env` in your `.gitignore` file. 
1. create a `.env` file and add to it: 
    ```bash
    export API_KEY="your_key_here"
    ```
2. add `.env` variables to your environment variables:
    ```bash
    source .env
    ```
3. Recover them from python using: 
    ```python
    import os
    print(os.environ['API_KEY'])
    ```

## How LOL API works? 

It's described in https://developer.riotgames.com/docs/lol

There's a different base url for each server: 

![](https://i.imgur.com/3oJgmSl.png)

The endpoints are described in https://developer.riotgames.com/apis#summoner-v4

![](https://i.imgur.com/aXUbI0x.png)

As described by docs, you should append your personal key as a query parameter: 

```
?api_key=API_KEY
```


## Task: Extract ranked winrate of a summoner
Ranked info is available at `/lol/league/v4/entries/by-summoner/{encryptedSummonerId}` endpoint. 

![](https://i.imgur.com/7hnJQp2.png)

In order to get the `encriptedSummonerId`, we first need to consume a `summoner` info. 


Therefore, we'll have to do two requests. First to:  
```
https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/SUMMONER_NAME?api_key=API_KEY
```

That will response something like: 

```json
{
    "id":"uIB3ZyvMYKpk_6r8woNRonQV6CMSkbgCx7SaPibDbCOR",
    "accountId":"TkQ5nsOGd-WuePTbxoZJi-o_f1Pm88lJNeYJfXgYJYE",
    "puuid":"MKsu8qe6G77VhZdC-kFIVHSKB8Xd8MyujvdKyBmKPbDNXE58_CNArd-1uOhdAfIYRMKA9lHJrbDetg",
    "name":"Kami",
    "profileIconId":5448,
    "revisionDate":1661034302000,
    "summonerLevel":472
}
```

After transforming response to a `json` and storing it `id`, use it to request:

```
https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{encryptedSummonerId}?api_key=API_KEY
```

Which will response something like: 

```json
[
    {
        "leagueId":"0625ee79-ad43-44b6-8a5a-9fc4b593dc46",
        "queueType":"RANKED_FLEX_SR",
        "tier":"PLATINUM",
        "rank":"II",
        "summonerId":"uIB3ZyvMYKpk_6r8woNRonQV6CMSkbgCx7SaPibDbCOR",
        "summonerName":"Kami",
        "leaguePoints":81,
        "wins":10,
        "losses":6,
        "veteran":false,
        "inactive":false,
        "freshBlood":false,"hotStreak":false
    },
    {
        "leagueId":"4a19f364-75d8-3e41-a8f4-a3dd22f59678",
        "queueType":"RANKED_SOLO_5x5",
        "tier":"GRANDMASTER",
        "rank":"I",
        "summonerId":"uIB3ZyvMYKpk_6r8woNRonQV6CMSkbgCx7SaPibDbCOR",
        "summonerName":"Kami",
        "leaguePoints":808,
        "wins":306,
        "losses":276,
        "veteran":false,
        "inactive":false,
        "freshBlood":true,
        "hotStreak":false
    }
]
```

## Consuming the API 
After figuring out the architecture, authentication process, HTTP Method, API base url and route, consuming the API is pretty easy. 
In LOL case, simply use `requests` method to use a HTTP method to the url with your API_KEY as a url parameter. 

Check `script.py` for implementation details. 