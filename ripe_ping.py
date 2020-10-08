import requests

def main():
    url = 'https://atlas.ripe.net/api/v2/measurements/?key={}'
    api_key="" #key to be put
    headers = {'Content-Type': 'application/json'}
    probes = "1000831,1000460,54983,14076,25097"

    body = """{
                \"definitions\": [
                    {
                    \"target\": \"www.bilibili.com\",
                    \"description\": \"bilibili Measurement\",
                    \"type\": \"ping\",
                    \"af\": 4,
                    \"resolve_on_probe\": true,
                    \"is_public\": false
                    }
                ],
                \"probes\": [
                    {
                        \"requested\": 3,
                        \"type\": \"probes\",
                        \"value\": \"1000831,1000460,54983,14076,25097\"
                    }
                ],
                \"is_oneoff\": true
            }"""
    
    rsp = requests.request("POST",url.format(api_key),headers=headers, data=body)
    print(rsp)
    print(rsp.json())
    result = rsp.json()['measurements']
    print(result)

if __name__ == '__main__':
    main()