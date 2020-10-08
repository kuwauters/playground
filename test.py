body = "{                \"definitions\": [                    {                    \"target\": \"www.bilibili.com\",                    \"description\": \"bilibili Measurement\",                    \"type\": \"ping\",                    \"af\": 4,                    \"resolve_on_probe\": true,                    \"is_public\": false                    }                ],                \"probes\": [                    {                        \"requested\": 3,                       \"type\": \"probes\",                        \"value\": \"{}\"                   }                ],               \"is_oneoff\": true            }"""

print ("test: {}".format("bla, bli, bloem"))   

txt = "test: {}"
print(body.format("bla, bli, bloem"))