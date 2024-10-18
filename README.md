# Description
Its an API for calculating Elo rating system.
The [formula](https://www.e-mentor.edu.pl/artykul/index/numer/82/id/1444 "formula") for calculating a new ranking is as follows:

Rn = R + K(O - P)     (1)

Where: Rn is the new value of the rating, R - the actual rating, O - submission outcome (1 - fully correct response, 0 - incorrect response), P - probability of submitting the fully correct response and constant K - the optimal value.

# Requirements
fastapi==0.111.0
pydantic==2.7.2
fastapi-cli==0.0.4
uvicorn==0.27.0

