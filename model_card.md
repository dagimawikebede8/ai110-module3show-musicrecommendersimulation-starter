# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch 1.0**

---

## 2. Intended Use

VibeMatch is a simple music recommender built for classroom learning. It recommends songs based on a user's preferred genre, mood, and energy level.

The goal is to show how a recommendation system can compare user preferences with song features and rank songs based on how well they match.

This system is only a simulation and is not designed to replace real-world recommendation systems like Spotify or YouTube.

---

## 3. How the Model Works

The recommender gives each song a score based on how closely it matches the user's preferences.

The scoring system uses:

- Genre match: +3 points
- Mood match: +4 points
- Energy similarity: up to +2 points

Mood has the highest weight because I wanted the overall vibe of a song to be important. Genre is also important, while energy helps the system choose between songs with similar characteristics.

After every song receives a score, the songs are ranked from highest score to lowest score. The highest-ranked songs are recommended to the user.

---

## 4. Data

The system uses the songs stored in `data/songs.csv`.

Each song contains information such as:

- Title
- Artist
- Genre
- Mood
- Energy
- Tempo
- Valence
- Danceability
- Acousticness

I expanded the starter dataset by adding more songs with different genres and moods.

The dataset is still small compared with a real music streaming service. Because of this, some user preferences may not have a song that matches them well.

---

## 5. Strengths

The system works well when the dataset contains songs that closely match the user's preferences.

For example, the Chill Lofi profile recommended Midnight Coding first because it matched the lofi genre, chill mood, and target energy.

The High-Energy Pop profile also produced reasonable recommendations because Sunrise City matched both the preferred genre and mood.

The scoring system is simple and makes it easy to understand why each song was recommended.

---

## 6. Limitations and Bias

One limitation of my recommender is that it depends heavily on the weights I choose. During my experiment, increasing the energy weight caused songs with similar energy levels to receive high scores even when their genre or mood did not match the user.

The small song dataset also limits the variety of recommendations and could cause users to keep seeing similar types of songs. The Sad but High-Energy profile showed this weakness because the system could not find a song that matched all of the user's preferences.

A larger and more diverse dataset could make the recommendations more balanced.

---

## 7. Evaluation

I tested the recommender with three profiles: High-Energy Pop, Chill Lofi, and Sad but High-Energy.

For High-Energy Pop, Sunrise City ranked first because it matched the pop genre, happy mood, and had similar energy.

For Chill Lofi, Midnight Coding ranked first because it matched the lofi genre, chill mood, and target energy. The difference between these two profiles showed that changing the user's preferences produced different recommendations that made sense.

The Sad but High-Energy profile was more challenging. Storm Runner ranked first because it matched the rock genre and high energy preference, even though it did not match the sad mood.

I also experimented with the scoring weights. I reduced the genre weight from 3.0 to 1.5 and increased energy from a maximum of 2.0 to 4.0. Songs with similar energy became much more competitive even when their genre or mood did not match. I decided to return to my original weights because they produced more balanced recommendations.

---

## 8. Future Work

If I continued developing this recommender, I would:

- Add more songs and genres to the dataset.
- Use more features such as tempo, danceability, valence, and acousticness in the scoring system.
- Add multiple favorite genres and moods instead of requiring one exact preference.
- Add user listening behavior such as likes, skips, and previous plays.

These changes could make the recommendations more personalized and diverse.

---

## 9. Personal Reflection

My biggest learning moment was seeing how changing a few scoring weights could change the recommendations. I learned that a recommendation system does not simply find a correct answer. The rules and weights chosen by the developer influence what the user sees.

AI tools helped me understand scoring ideas, write and debug parts of the program, and think about different ways to test the recommender. I still needed to run the code, check the results, and decide whether the suggestions actually made sense for my project.

I was surprised that a simple point-based algorithm could produce recommendations that felt reasonable. Even though this system is much simpler than a real streaming platform, ranking songs by user preferences already creates a basic personalized experience.

If I continued this project, I would experiment with more song features, a larger dataset, and user behavior such as likes and skips.