1. settings is used to get the env variables inside code 
2. using those env vars app can authenticate external sources (github)
3. apart from external source this can be used for adding local variables for timeouts etc
4. pydantic base settings used so a 5 and "5" can be treated same in the settings picking up env vars
5. for 500 error; server failed so client retries, for 429: the client should say your api rate limit is reached and retry and 404 should say not found; means user does not exist - means no profit in retrying so client failes immediately
6. Use exponential backoff to increase the waiting time for retrying api calls when constant errors are hit - time doubles after each failed attempt and use jitter for randomness, retrying api calls with a random time span - jitter is used when 100 clients all fail at the same time so retrying means putting load on server so now add random jitter to let them all hit api at different time while backoff spreads out how often
7. async/await waits for the coroutine to finish before going to the next one; use asyncio.gather to run concurrent coroutines