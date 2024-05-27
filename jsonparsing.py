import json

data = '{ "id": "chatcmpl-9MUgDhe7CsbEkYQ0eTseSEtu476e3", "choices": [ { "finish_reason": "stop", "index": 0, "logprobs": null, "message": { "content": "1. The Evolution of The Beatles: From Liverpool to International Stardom\\n2. The Fab Four: Exploring the Talents of John, Paul, George, and Ringo\\n3. Beatlemania: How The Beatles Revolutionized Pop Culture\\n4. Sgt. Peppers Lonely Hearts Club Band: A Musical Masterpiece\\n5. The Legacy of The Beatles: Their Impact on Music and Society", "role": "assistant", "function_call": null, "tool_calls": null } } ], "created": 1715148177, "model": "gpt-3.5-turbo-0125", "object": "chat.completion", "system_fingerprint": null, "usage": { "completion_tokens": 81, "prompt_tokens": 22, "total_tokens": 103 } }'
jsondata = json.loads(data)

print(jsondata.get('choices')[0].get('message').get('content'))