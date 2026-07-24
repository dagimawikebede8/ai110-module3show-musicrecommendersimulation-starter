from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def calculate_score(self, user: UserProfile, song: Song) -> float:
        score = 0

        # Genre match
        if song.genre == user.favorite_genre:
            score += 3

        # Mood match
        if song.mood == user.favorite_mood:
            score += 4

        # Energy similarity (up to 2 points)
        difference = abs(song.energy - user.target_energy)
        score += max(0, 2 * (1 - difference))

        # Acoustic preference
        if user.likes_acoustic and song.acousticness >= 0.5:
            score += 1
        elif not user.likes_acoustic and song.acousticness < 0.5:
            score += 1

        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        ranked = sorted(
            self.songs,
            key=lambda song: self.calculate_score(user, song),
            reverse=True,
        )
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("matches your favorite genre")

        if song.mood == user.favorite_mood:
            reasons.append("matches your favorite mood")

        if abs(song.energy - user.target_energy) <= 0.1:
            reasons.append("has similar energy")

        if user.likes_acoustic and song.acousticness >= 0.5:
            reasons.append("matches your acoustic preference")

        if not user.likes_acoustic and song.acousticness < 0.5:
            reasons.append("matches your non-acoustic preference")

        if not reasons:
            return "This song is a reasonable match."

        return "Recommended because it " + ", ".join(reasons) + "."


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song based on the user's preferences."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 3.0
        reasons.append("genre match (+3.0)")

    if song["mood"] == user_prefs["mood"]:
        score += 4.0
        reasons.append("mood match (+4.0)")

    difference = abs(song["energy"] - user_prefs["energy"])
    energy_points = max(0.0, 2.0 * (1.0 - difference))

    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    return score, reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    """
    recommendations = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        recommendations.append((song, score, explanation))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations[:k]