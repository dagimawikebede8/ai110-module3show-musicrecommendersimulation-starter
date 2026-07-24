# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

My music recommender recommends songs based on a user's musical preferences. It compares features such as genre, mood, energy, and tempo to find songs that best match the user's preferred vibe. Each song receives a score, and the songs with the highest scores are recommended first.
---

## How The System Works

Real-world recommendation systems use information about users and content to predict what someone might enjoy. Collaborative filtering uses the behavior of similar users, such as likes, skips, saves, and playlists. Content-based filtering uses features of the content itself. My recommender will use a simple content-based approach by comparing each song's features with the user's preferences.

The Song will use:
- Genre
- Mood
- Energy
- Tempo BPM

The UserProfile will store:
- Preferred genre
- Preferred mood
- Preferred energy
- Preferred tempo

The recommender will give more importance to mood, followed by genre and energy, while tempo will have a smaller influence. For energy and tempo, songs with values closer to the user's preferred values will receive higher scores. After every song receives a score, the recommender will rank the songs from highest to lowest and recommend the best matches first.

### Example User Profile

- Favorite genre: lofi
- Favorite mood: chill
- Target energy: 0.40
- Target tempo: 80 BPM

### Algorithm Recipe

- Genre match: +3 points
- Mood match: +4 points
- Energy similarity: up to +2 points based on how close the song's energy is to the user's target.
- Tempo similarity: up to +1 point based on how close the song's tempo is to the user's target.

Each song can receive a maximum score of 10 points. After every song is scored, the recommender sorts the songs from highest score to lowest score and recommends the best matches.

### Data Flow

User Preferences → Compare Each Song → Calculate Score → Rank Songs → Return Top Recommendations

### Potential Bias

This recommender may over-prioritize exact genre and mood matches. As a result, it could overlook songs from different genres that still have a similar energy, tempo, or overall vibe.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

User profile: genre=pop, mood=happy, energy=0.8

```text
Top recommendations:

Sunrise City - Score: 8.96
Because: genre match (+3.0), mood match (+4.0), energy similarity (+1.96)

Rooftop Lights - Score: 5.92
Because: mood match (+4.0), energy similarity (+1.92)

Gym Hero - Score: 4.74
Because: genre match (+3.0), energy similarity (+1.74)

Streetlight Echo - Score: 1.98
Because: energy similarity (+1.98)

Velvet Static - Score: 1.92
Because: energy similarity (+1.92)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---
## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



