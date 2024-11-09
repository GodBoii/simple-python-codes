import pandas as pd
import numpy as np
import random

class SimpleMusicRecommender:
    def __init__(self):
        self.music_data = {
            'song_id': [1, 2, 3, 4, 5, 6, 7, 8],
            'title': ['Shape of You', 'Bohemian Rhapsody', 'Giant Steps', 
                     'Sweet Child O Mine', 'Thriller', 'Despacito', 
                     'All of Me', 'Hotel California'],
            'artist': ['Ed Sheeran', 'Queen', 'John Coltrane', 
                      'Guns N Roses', 'Michael Jackson', 'Luis Fonsi', 
                      'John Legend', 'Eagles'],
            'primary_genre': ['pop', 'rock', 'jazz', 'rock', 'pop', 'pop', 
                            'r&b', 'rock'],
            'secondary_genre': ['r&b', 'pop', 'r&b', 'metal', 'r&b', 'latin', 
                              'pop', 'country'],
            'popularity': [65, 90, 75, 88, 72, 50, 85, 89]
        }
        self.df = pd.DataFrame(self.music_data)

        self.similar_genres = {
            'pop': ['r&b', 'latin'],
            'rock': ['metal', 'pop'],
            'r&b': ['pop', 'jazz'],
            'jazz': ['r&b', 'classical'],
            'latin': ['pop', 'r&b']
        }
        
        self.user_preferences = {}

    def get_similar_genres(self, genre):
        return [genre] + self.similar_genres.get(genre, [])

    def add_user_preference(self, user_id, liked_songs):
        liked_genres = []
        for song_id in liked_songs:
            song = self.df[self.df['song_id'] == song_id]
            if not song.empty:
                liked_genres.append(song['primary_genre'].iloc[0])
                liked_genres.append(song['secondary_genre'].iloc[0])
        
        self.user_preferences[user_id] = {
            'liked_genres': list(set(liked_genres)),
            'liked_songs': liked_songs
        }

    def get_recommendations(self, user_id, num_recommendations=3):
        if user_id not in self.user_preferences:
            return "User not found. Please add user preferences first."

        user_prefs = self.user_preferences[user_id]
        liked_songs = user_prefs['liked_songs']
        liked_genres = user_prefs['liked_genres']

        expanded_genres = []
        for genre in liked_genres:
            expanded_genres.extend(self.get_similar_genres(genre))
        expanded_genres = list(set(expanded_genres)) 
        candidate_songs = self.df[
            (~self.df['song_id'].isin(liked_songs)) &
            ((self.df['primary_genre'].isin(expanded_genres)) |
             (self.df['secondary_genre'].isin(expanded_genres)))
        ].copy()

        if candidate_songs.empty:
            return "No recommendations available."

        candidate_songs['genre_score'] = candidate_songs.apply(
            lambda x: 2 if x['primary_genre'] in liked_genres else
                     1 if x['secondary_genre'] in liked_genres else 0.5,
            axis=1
        )

        candidate_songs['norm_popularity'] = (candidate_songs['popularity'] - candidate_songs['popularity'].min()) / \
                                          (candidate_songs['popularity'].max() - candidate_songs['popularity'].min())

        candidate_songs['random_factor'] = [random.uniform(0, 0.2) for _ in range(len(candidate_songs))]

        candidate_songs['final_score'] = (candidate_songs['genre_score'] * 0.5 +
                                        candidate_songs['norm_popularity'] * 0.3 +
                                        candidate_songs['random_factor'] * 0.2)

        recommendations = candidate_songs.sort_values('final_score', ascending=False)

        return recommendations[['title', 'artist', 'primary_genre', 'secondary_genre', 'popularity']].head(num_recommendations)

    def print_all_songs(self):
        print("\nAll songs in database:")
        print(self.df[['title', 'artist', 'primary_genre', 'secondary_genre', 'popularity']]
              .sort_values('popularity', ascending=False))

def main():
    recommender = SimpleMusicRecommender()

    recommender.print_all_songs()

    print("\nAdding preferences for user 1 (likes Shape of You and Thriller)...")
    recommender.add_user_preference(user_id=1, liked_songs=[1, 5])

    print("\nFirst set of recommendations:")
    recommendations1 = recommender.get_recommendations(user_id=1, num_recommendations=2)
    print(recommendations1)
    
    print("\nSecond set of recommendations:")
    recommendations2 = recommender.get_recommendations(user_id=1, num_recommendations=2)
    print(recommendations2)

    print("\nAdding preferences for user 2 (likes different songs)...")
    recommender.add_user_preference(user_id=2, liked_songs=[2, 3]) 
    
    print("\nRecommendations for user 2:")
    recommendations3 = recommender.get_recommendations(user_id=2, num_recommendations=2)
    print(recommendations3)

if __name__ == "__main__":
    main()