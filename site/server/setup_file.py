import pickle

from match_predictor.main import predict_proba
from scraping import get_next_day_matches

matches = []
for match in get_next_day_matches():
    probs = predict_proba(
        match.stage, 4000,
        match.home, match.away
    )
    match.prob_home = probs[1]
    match.prob_away = probs[2]
    match.prob_draw = probs[0]

    matches.append(match)

with open("matches.b", "wb") as f:
    pickle.dump(matches, f)
