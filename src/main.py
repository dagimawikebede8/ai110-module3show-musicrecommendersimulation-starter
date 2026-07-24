"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9
        },

        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.4
        },

        "Sad but High-Energy": {
            "genre": "rock",
            "mood": "sad",
            "energy": 0.9
        }
    }

    for profile_name, user_prefs in profiles.items():
        print(f"\n=== {profile_name} ===")
        print(
            f"Genre: {user_prefs['genre']}, "
            f"Mood: {user_prefs['mood']}, "
            f"Energy: {user_prefs['energy']}"
        )

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\nTop recommendations:\n")

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()

if __name__ == "__main__":
    main()