CATALOG_DATA = [
    # ==========================================
    # FAMOUS TIER (India Trends Index > 0.70)
    # ==========================================
    
{
  "id": "deathnote",
  "name": "Death Note",
  "india_fame_tier": "famous",
  "india_fame_tier_source": "manual_assumption",
  "vector": {
    "genre_one_hot": {
      "supernatural": 1,
      "suspense": 1,
      "psychological": 1,
      "mystery": 1
    },
    "tag_weights": {
      "anti_hero": 0.94,
      "mind_games": 0.95,
      "police": 0.87
    },
    "demographic_tag": "shonen"
  },
  "mal_score": 8.62,
  "anilist_popularity": 960805,
  "anilist_popularity_rank": 4,
  "trailer_youtube_id": None,
  "trends_india_relative_index": None
}
,
   
{
  "id": "demonslayer",
  "name": "Demon Slayer",
  "india_fame_tier": "famous",
  "india_fame_tier_source": "manual_assumption",
  "vector": {
    "genre_one_hot": {
      "action": 1,
      "adventure": 1,
      "fantasy": 1,
      "supernatural": 1,
      "drama": 1
    },
    "tag_weights": {
      "demons": 0.96,
      "swordplay": 0.88,
      "male_protagonist": 0.82,
      "tragedy": 0.78,
      "revenge": 0.74,
      "mythology": 0.65
    },
    "demographic_tag": "shonen"
  },
  "mal_score": None,
  "anilist_popularity": 1007020,
  "anilist_popularity_rank": 2,
  "anilist_average_score": 82,
  "trailer_youtube_id": None,
  "trends_india_relative_index": None,
  "release_year": 2019,
  "episodes": 26,
  "studio": "ufotable",
  "anilist_id": 101922
}
,
    
{
  "id": "attackontitan",
  "name": "Attack on Titan",
  "india_fame_tier": "famous",
  "india_fame_tier_source": "manual_assumption",
  "vector": {
    "genre_one_hot": {
      "action": 1,
      "drama": 1,
      "fantasy": 1,
      "mystery": 1,
      "suspense": 1
    },
    "tag_weights": {
      "kaiju": 0.93,
      "revenge": 0.93,
      "military": 0.88,
      "post_apocalyptic": 0.84,
      "survival": 0.84,
      "dystopian": 0.77,
      "swordplay": 0.74
    },
    "demographic_tag": "shonen"
  },
  "mal_score": 8.58,
  "anilist_popularity": 1069717,
  "anilist_popularity_rank": 1,
  "anilist_average_score": 85,
  "trailer_youtube_id":None,
  "trends_india_relative_index": None,
  "release_year": 2013,
  "episodes": 25,
  "studio": "WIT Studio",
  "anilist_id": 16498
}
,
   
{
  "id": "naruto",
  "name": "Naruto",
  "india_fame_tier": "famous",
  "india_fame_tier_source": "manual_assumption",
  "vector": {
    "genre_one_hot": {
      "action": 1,
      "adventure": 1,
      "comedy": 1,
      "drama": 1,
      "fantasy": 1,
      "supernatural": 1
    },
    "tag_weights": {
      "ninja": 0.97,
      "coming_of_age": 0.90,
      "male_protagonist": 0.88,
      "orphan": 0.86,
      "super_power": 0.85,
      "martial_arts": 0.81,
      "found_family": 0.80
    },
    "demographic_tag": "shonen"
  },
  "mal_score": None,
  "anilist_popularity": 735317,
  "anilist_average_score": 80,
  "trailer_youtube_id": None,
  "trends_india_relative_index": None,
  "release_year": 2002,
  "episodes": 220,
  "studio": "Studio Pierrot",
  "anilist_id": 20
}
,
    
{
  "id": "onepiece",
  "name": "One Piece",
  "india_fame_tier": "famous",
  "india_fame_tier_source": "manual_assumption",
  "vector": {
    "genre_one_hot": {
      "action": 1,
      "adventure": 1,
      "comedy": 1,
      "drama": 1,
      "fantasy": 1
    },
    "tag_weights": {
      "pirates": 0.98,
      "travel": 0.94,
      "ensemble_cast": 0.93,
      "super_power": 0.90,
      "found_family": 0.88,
      "male_protagonist": 0.83,
      "conspiracy": 0.81,
      "ships": 0.81,
      "prophecy": 0.80
    },
    "demographic_tag": "shonen"
  },
  "mal_score": None,
  "anilist_popularity": 753033,
  "anilist_average_score": 87,
  "trailer_youtube_id": None,
  "trends_india_relative_index": None,
  "release_year": 1999,
  "episodes": None,
  "studio": "Toei Animation",
  "anilist_id": 21
}
,
    
{
  "id": "jujutsukaisen",
  "name": "Jujutsu Kaisen",
  "india_fame_tier": "famous",
  "india_fame_tier_source": "manual_assumption",
  "vector": {
    "genre_one_hot": {
      "action": 1,
      "fantasy": 1,
      "supernatural": 1,
      "drama": 1,
      "horror": 1
    },
    "tag_weights": {
      "curses": 0.98,
      "super_power": 0.95,
      "martial_arts": 0.88,
      "demons": 0.82,
      "school": 0.85,
      "male_protagonist": 0.90,
      "urban_fantasy": 0.92
    },
    "demographic_tag": "shonen"
  },
  "mal_score": None,
  "anilist_popularity": None,
  "anilist_average_score": None,
  "trailer_youtube_id": None,
  "trends_india_relative_index": None,
  "release_year": 2020,
  "episodes": 24,
  "studio": "MAPPA",
  "anilist_id": 113415
}
,
    
{
  "id": "dragonballz",
  "name": "Dragon Ball Z",
  "india_fame_tier": "famous",
  "india_fame_tier_source": "manual_assumption",
  "vector": {
    "genre_one_hot": {
      "action": 1,
      "adventure": 1,
      "fantasy": 1,
      "comedy": 1,
      "science_fiction": 1
    },
    "tag_weights": {
      "martial_arts": 0.99,
      "super_power": 0.98,
      "aliens": 0.95,
      "tournament": 0.90,
      "male_protagonist": 0.92,
      "training": 0.90,
      "friendship": 0.88
    },
    "demographic_tag": "shonen"
  },
  "mal_score": None,
  "anilist_popularity": None,
  "anilist_average_score": None,
  "trailer_youtube_id": None,
  "trends_india_relative_index": None,
  "release_year": 1989,
  "episodes": 291,
  "studio": "Toei Animation",
  "anilist_id": 813
}
,
    
{
  "id": "myheroacademia",
  "name": "My Hero Academia",
  "india_fame_tier": "famous",
  "india_fame_tier_source": "manual_assumption",
  "vector": {
    "genre_one_hot": {
      "action": 1,
      "adventure": 1,
      "comedy": 1,
      "drama": 1,
      "fantasy": 1
    },
    "tag_weights": {
      "superhero": 0.99,
      "super_power": 0.98,
      "school": 0.95,
      "coming_of_age": 0.90,
      "male_protagonist": 0.90,
      "ensemble_cast": 0.87,
      "rivalry": 0.88
    },
    "demographic_tag": "shonen"
  },
  "mal_score": None,
  "anilist_popularity": None,
  "anilist_average_score": None,
  "trailer_youtube_id": None,
  "trends_india_relative_index": None,
  "release_year": 2016,
  "episodes": 13,
  "studio": "Bones",
  "anilist_id": 21459
}
,
 tokyoghoul = {
    "id": "tokyoghoul",
    "name": "Tokyo Ghoul",
    "india_fame_tier": None,
    "vector": {
        "genre_one_hot": {
            "action": 1,
            "drama": 1,
            "horror": 1,
            "supernatural": 1
        },
        "tag_weights": {
            "dark_fantasy": 0.95,
            "gore": 0.90,
            "tragedy": 0.90,
            "psychological": 0.85,
            "monsters": 0.85
        },
        "demographic_tag": "seinen"
    },
    "mal_score": None,
    "anilist_popularity": None,
    "trailer_youtube_id": None,
    "trends_india_relative_index": None
}

hunterxhunter = {
    "id": "hunterxhunter",
    "name": "Hunter x Hunter",
    "india_fame_tier": None,
    "vector": {
        "genre_one_hot": {
            "action": 1,
            "adventure": 1,
            "fantasy": 1
        },
        "tag_weights": {
            "coming_of_age": 0.90,
            "friendship": 0.90,
            "super_power": 0.95,
            "tournament": 0.85,
            "strategy": 0.90,
            "travel": 0.85
        },
        "demographic_tag": "shonen"
    },
    "mal_score": None,
    "anilist_popularity": None,
    "trailer_youtube_id": None,
    "trends_india_relative_index": None
},
    {
        "id": "onepunchman", "name": "One Punch Man", "india_fame_tier": "famous",
        "vector": {"genre_one_hot": {"action": 1, "comedy": 1, "sci-fi": 1}, "tag_weights": {"superheroes": 0.95, "parody": 0.9, "overpowered": 0.99}, "demographic_tag": "seinen"},
        "mal_score": 8.50, "anilist_popularity": 9, "trailer_youtube_id": "Poo5lqsbfRU", "trends_india_relative_index": 0.84
    },
    {
        "id": "haikyuu", "name": "Haikyuu!!", "india_fame_tier": "famous",
        "vector": {"genre_one_hot": {"sports": 1, "drama": 1}, "tag_weights": {"volleyball": 0.99, "school": 0.8, "rivalry": 0.9}, "demographic_tag": "shonen"},
        "mal_score": 8.44, "anilist_popularity": 14, "trailer_youtube_id": "JOGp2c7-cKc", "trends_india_relative_index": 0.78
    },
    {
        "id": "blackclover", "name": "Black Clover", "india_fame_tier": "famous",
        "vector": {"genre_one_hot": {"action": 1, "comedy": 1, "fantasy": 1}, "tag_weights": {"magic": 0.95, "underdog": 0.9, "rivalry": 0.85}, "demographic_tag": "shonen"},
        "mal_score": 8.16, "anilist_popularity": 25, "trailer_youtube_id": "vjuOUcsUxa4", "trends_india_relative_index": 0.76
    },
    {
        "id": "bleach", "name": "Bleach", "india_fame_tier": "famous",
        "vector": {"genre_one_hot": {"action": 1, "adventure": 1, "supernatural": 1}, "tag_weights": {"swordsplay": 0.9, "spirits": 0.95, "afterlife": 0.85}, "demographic_tag": "shonen"},
        "mal_score": 7.91, "anilist_popularity": 32, "trailer_youtube_id": "i0zEQGiKz0", "trends_india_relative_index": 0.88
    },
    {
        "id": "chainsawman", "name": "Chainsaw Man", "india_fame_tier": "famous",
        "vector": {"genre_one_hot": {"action": 1, "fantasy": 1, "horror": 1}, "tag_weights": {"demons": 0.9, "gore": 0.95, "anti_hero": 0.85}, "demographic_tag": "shonen"},
        "mal_score": 8.52, "anilist_popularity": 11, "trailer_youtube_id": "q15CRdE5Bv0", "trends_india_relative_index": 0.80
    },
    {
        "id": "fmab", "name": "Fullmetal Alchemist: Brotherhood", "india_fame_tier": "famous",
        "vector": {"genre_one_hot": {"action": 1, "adventure": 1, "drama": 1, "fantasy": 1}, "tag_weights": {"military": 0.85, "alchemy": 0.99, "philosophy": 0.8}, "demographic_tag": "shonen"},
        "mal_score": 9.09, "anilist_popularity": 10, "trailer_youtube_id": "--IcmZkvL0Q", "trends_india_relative_index": 0.72
    },

    # ==========================================
    # MID TIER (India Trends Index 0.30 - 0.69)
    # ==========================================
    {
        "id": "spyxfamily", "name": "Spy x Family", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"comedy": 1, "action": 1}, "tag_weights": {"found_family": 0.95, "spy": 0.99, "wholesome": 0.9}, "demographic_tag": "shonen"},
        "mal_score": 8.54, "anilist_popularity": 15, "trailer_youtube_id": "CCXngP4VpEE", "trends_india_relative_index": 0.65
    },
    {
        "id": "cyberpunkedgerunners", "name": "Cyberpunk: Edgerunners", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"action": 1, "sci-fi": 1}, "tag_weights": {"cyberpunk": 0.99, "dystopia": 0.9, "tragedy": 0.85}, "demographic_tag": "seinen"},
        "mal_score": 8.60, "anilist_popularity": 42, "trailer_youtube_id": "KvXEQ2p5nho", "trends_india_relative_index": 0.55
    },
    {
        "id": "psychopass", "name": "Psycho-Pass", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"sci-fi": 1, "suspense": 1, "psychological": 1}, "tag_weights": {"cyberpunk": 0.85, "police": 0.95, "dystopia": 0.9}, "demographic_tag": "seinen"},
        "mal_score": 8.33, "anilist_popularity": 45, "trailer_youtube_id": "YztIgRdffzo", "trends_india_relative_index": 0.40
    },
    {
        "id": "steinsgate", "name": "Steins;Gate", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"sci-fi": 1, "suspense": 1, "psychological": 1}, "tag_weights": {"time_travel": 0.99, "thriller": 0.9, "tragedy": 0.8}, "demographic_tag": "seinen"},
        "mal_score": 9.07, "anilist_popularity": 13, "trailer_youtube_id": "uOjvssceK4Q", "trends_india_relative_index": 0.50
    },
    {
        "id": "mobpsycho100", "name": "Mob Psycho 100", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"action": 1, "comedy": 1, "supernatural": 1}, "tag_weights": {"psychic": 0.99, "coming_of_age": 0.9, "school": 0.7}, "demographic_tag": "shonen"},
        "mal_score": 8.49, "anilist_popularity": 18, "trailer_youtube_id": "EXjeKqL022E", "trends_india_relative_index": 0.48
    },
    {
        "id": "drstone", "name": "Dr. STONE", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"adventure": 1, "comedy": 1, "sci-fi": 1}, "tag_weights": {"post_apocalyptic": 0.9, "science": 0.99, "survival": 0.8}, "demographic_tag": "shonen"},
        "mal_score": 8.28, "anilist_popularity": 19, "trailer_youtube_id": "9NXTMWYhRgg", "trends_india_relative_index": 0.58
    },
    {
        "id": "tokyorevengers", "name": "Tokyo Revengers", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"action": 1, "drama": 1, "supernatural": 1}, "tag_weights": {"time_travel": 0.95, "delinquents": 0.99, "gangs": 0.95}, "demographic_tag": "shonen"},
        "mal_score": 7.93, "anilist_popularity": 22, "trailer_youtube_id": "FwbB0o3E8b0", "trends_india_relative_index": 0.62
    },
    {
        "id": "bluelock", "name": "Blue Lock", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"sports": 1, "drama": 1}, "tag_weights": {"soccer": 0.99, "survival_game": 0.85, "ego": 0.9}, "demographic_tag": "shonen"},
        "mal_score": 8.27, "anilist_popularity": 38, "trailer_youtube_id": "w4VuBsEOqaY", "trends_india_relative_index": 0.68
    },
    {
        "id": "kaguyasama", "name": "Kaguya-sama: Love is War", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"comedy": 1, "romance": 1}, "tag_weights": {"school": 0.8, "mind_games": 0.9, "tsundere": 0.95}, "demographic_tag": "seinen"},
        "mal_score": 8.41, "anilist_popularity": 17, "trailer_youtube_id": "5nK1bO3Wqbc", "trends_india_relative_index": 0.55
    },
    {
        "id": "jojo", "name": "JoJo's Bizarre Adventure", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"action": 1, "adventure": 1, "supernatural": 1}, "tag_weights": {"vampires": 0.8, "generations": 0.9, "memes": 0.99}, "demographic_tag": "shonen"},
        "mal_score": 7.90, "anilist_popularity": 40, "trailer_youtube_id": "QEq1-Bngz9k", "trends_india_relative_index": 0.60
    },
    {
        "id": "evangelion", "name": "Neon Genesis Evangelion", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"action": 1, "drama": 1, "sci-fi": 1}, "tag_weights": {"mecha": 0.95, "psychological": 0.99, "philosophy": 0.9}, "demographic_tag": "shonen"},
        "mal_score": 8.35, "anilist_popularity": 28, "trailer_youtube_id": "13nSISwxrY4", "trends_india_relative_index": 0.45
    },
    {
        "id": "codegeass", "name": "Code Geass", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"action": 1, "drama": 1, "sci-fi": 1}, "tag_weights": {"mecha": 0.85, "mind_games": 0.9, "rebellion": 0.95}, "demographic_tag": "shonen"},
        "mal_score": 8.70, "anilist_popularity": 21, "trailer_youtube_id": "O9CX-aNnC54", "trends_india_relative_index": 0.52
    },
    {
        "id": "cowboybebop", "name": "Cowboy Bebop", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"action": 1, "sci-fi": 1}, "tag_weights": {"space": 0.95, "bounty_hunters": 0.99, "jazz": 0.9}, "demographic_tag": "seinen"},
        "mal_score": 8.75, "anilist_popularity": 26, "trailer_youtube_id": "qig4KOK2R2g", "trends_india_relative_index": 0.42
    },
    {
        "id": "vinlandsaga", "name": "Vinland Saga", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"action": 1, "adventure": 1, "drama": 1}, "tag_weights": {"vikings": 0.99, "historical": 0.95, "revenge": 0.9}, "demographic_tag": "seinen"},
        "mal_score": 8.73, "anilist_popularity": 33, "trailer_youtube_id": "f8JBoEFEz80", "trends_india_relative_index": 0.59
    },
    {
        "id": "sao", "name": "Sword Art Online", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"action": 1, "adventure": 1, "fantasy": 1, "romance": 1}, "tag_weights": {"isekai": 0.9, "vr": 0.99, "survival_game": 0.85}, "demographic_tag": "shonen"},
        "mal_score": 7.20, "anilist_popularity": 16, "trailer_youtube_id": "C8JljiTbgcU", "trends_india_relative_index": 0.69
    },
    {
        "id": "yourname", "name": "Your Name.", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"drama": 1, "romance": 1, "supernatural": 1}, "tag_weights": {"body_swapping": 0.95, "disaster": 0.8, "time_manipulation": 0.9}, "demographic_tag": "shonen"},
        "mal_score": 8.84, "anilist_popularity": 20, "trailer_youtube_id": "xU47nhruN-Q", "trends_india_relative_index": 0.65
    },
    {
        "id": "erased", "name": "ERASED", "india_fame_tier": "mid",
        "vector": {"genre_one_hot": {"mystery": 1, "supernatural": 1, "suspense": 1}, "tag_weights": {"time_travel": 0.95, "murder_mystery": 0.99, "school": 0.7}, "demographic_tag": "seinen"},
        "mal_score": 8.30, "anilist_popularity": 34, "trailer_youtube_id": "84_eNqCq7o4", "trends_india_relative_index": 0.44
    },

    # ==========================================
    # LOW / NICHE TIER (India Trends Index < 0.30)
    # ==========================================
    {
        "id": "oddtaxi", "name": "Odd Taxi", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"drama": 1, "mystery": 1, "suspense": 1}, "tag_weights": {"anthropomorphic": 0.9, "yakuza": 0.8, "plot_twist": 0.95}, "demographic_tag": "seinen"},
        "mal_score": 8.63, "anilist_popularity": 386, "trailer_youtube_id": "7L43VAsjwjc", "trends_india_relative_index": 0.12
    },
    {
        "id": "linkclick", "name": "Link Click", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"drama": 1, "mystery": 1, "supernatural": 1}, "tag_weights": {"time_travel": 0.95, "photography": 0.9, "cliffhangers": 0.9}, "demographic_tag": "seinen"},
        "mal_score": 8.75, "anilist_popularity": 210, "trailer_youtube_id": "5nK1bO3Wqbc", "trends_india_relative_index": 0.15
    },
    {
        "id": "monster", "name": "Monster", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"drama": 1, "mystery": 1, "suspense": 1, "psychological": 1}, "tag_weights": {"serial_killer": 0.95, "europe": 0.85, "slow_burn": 0.9}, "demographic_tag": "seinen"},
        "mal_score": 8.88, "anilist_popularity": 140, "trailer_youtube_id": "msTB5r8nUHU", "trends_india_relative_index": 0.22
    },
    {
        "id": "pluto", "name": "PLUTO", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"action": 1, "mystery": 1, "sci-fi": 1}, "tag_weights": {"robots": 0.95, "murder_mystery": 0.9, "philosophy": 0.85}, "demographic_tag": "seinen"},
        "mal_score": 8.45, "anilist_popularity": 450, "trailer_youtube_id": "UoXo-617F5A", "trends_india_relative_index": 0.18
    },
    {
        "id": "frieren", "name": "Frieren: Beyond Journey's End", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"adventure": 1, "drama": 1, "fantasy": 1}, "tag_weights": {"elves": 0.9, "magic": 0.85, "aftermath": 0.99}, "demographic_tag": "shonen"},
        "mal_score": 9.15, "anilist_popularity": 112, "trailer_youtube_id": "qgQJ61K-k3E", "trends_india_relative_index": 0.28
    },
    {
        "id": "apothecarydiaries", "name": "The Apothecary Diaries", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"drama": 1, "mystery": 1}, "tag_weights": {"historical": 0.9, "medicine": 0.95, "detective": 0.85}, "demographic_tag": "seinen"},
        "mal_score": 8.82, "anilist_popularity": 190, "trailer_youtube_id": "w353T_kH0vY", "trends_india_relative_index": 0.25
    },
    {
        "id": "violetevergarden", "name": "Violet Evergarden", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"drama": 1, "fantasy": 1}, "tag_weights": {"war": 0.8, "letters": 0.99, "tearjerker": 0.95}, "demographic_tag": "seinen"},
        "mal_score": 8.67, "anilist_popularity": 48, "trailer_youtube_id": "0CJeDetA-5I", "trends_india_relative_index": 0.26
    },
    {
        "id": "madeinabyss", "name": "Made in Abyss", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"adventure": 1, "drama": 1, "fantasy": 1, "sci-fi": 1}, "tag_weights": {"exploration": 0.95, "dark_fantasy": 0.99, "monsters": 0.85}, "demographic_tag": "seinen"},
        "mal_score": 8.66, "anilist_popularity": 62, "trailer_youtube_id": "AQqXJ7uOIfU", "trends_india_relative_index": 0.20
    },
    {
        "id": "marchcomesinlikealion", "name": "March Comes In Like A Lion", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"drama": 1, "slice_of_life": 1}, "tag_weights": {"board_games": 0.9, "depression": 0.95, "found_family": 0.85}, "demographic_tag": "seinen"},
        "mal_score": 8.38, "anilist_popularity": 170, "trailer_youtube_id": "N7_YVb-4pLw", "trends_india_relative_index": 0.08
    },
    {
        "id": "bocchitherock", "name": "Bocchi the Rock!", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"comedy": 1, "slice_of_life": 1}, "tag_weights": {"music": 0.95, "social_anxiety": 0.99, "school": 0.7}, "demographic_tag": "seinen"},
        "mal_score": 8.71, "anilist_popularity": 130, "trailer_youtube_id": "WzXFzHqQ6hE", "trends_india_relative_index": 0.21
    },
    {
        "id": "heavenlydelusion", "name": "Heavenly Delusion", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"adventure": 1, "mystery": 1, "sci-fi": 1}, "tag_weights": {"post_apocalyptic": 0.95, "monsters": 0.85, "survival": 0.9}, "demographic_tag": "seinen"},
        "mal_score": 8.16, "anilist_popularity": 280, "trailer_youtube_id": "U3M_kO_YgA4", "trends_india_relative_index": 0.14
    },
    {
        "id": "pingpong", "name": "Ping Pong the Animation", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"sports": 1, "drama": 1}, "tag_weights": {"table_tennis": 0.99, "coming_of_age": 0.9, "psychological": 0.8}, "demographic_tag": "seinen"},
        "mal_score": 8.62, "anilist_popularity": 320, "trailer_youtube_id": "p03-Hk-d0E0", "trends_india_relative_index": 0.05
    },
    {
        "id": "tatamigalaxy", "name": "The Tatami Galaxy", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"comedy": 1, "mystery": 1, "romance": 1}, "tag_weights": {"college": 0.9, "time_loop": 0.95, "surreal": 0.99}, "demographic_tag": "seinen"},
        "mal_score": 8.58, "anilist_popularity": 290, "trailer_youtube_id": "f5QZ15C-gEs", "trends_india_relative_index": 0.06
    },
    {
        "id": "mushishi", "name": "Mushishi", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"adventure": 1, "fantasy": 1, "mystery": 1}, "tag_weights": {"spirits": 0.99, "episodic": 0.95, "nature": 0.9}, "demographic_tag": "seinen"},
        "mal_score": 8.67, "anilist_popularity": 215, "trailer_youtube_id": "Vn1yO_M8_U8", "trends_india_relative_index": 0.09
    },
    {
        "id": "sonnyboy", "name": "Sonny Boy", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"sci-fi": 1, "mystery": 1}, "tag_weights": {"survival": 0.8, "surreal": 0.99, "superpowers": 0.85}, "demographic_tag": "seinen"},
        "mal_score": 7.73, "anilist_popularity": 410, "trailer_youtube_id": "5j-w_hX2z7U", "trends_india_relative_index": 0.04
    },
    {
        "id": "baccano", "name": "Baccano!", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"action": 1, "comedy": 1, "mystery": 1}, "tag_weights": {"mafia": 0.95, "immortality": 0.9, "non_linear": 0.99}, "demographic_tag": "shonen"},
        "mal_score": 8.35, "anilist_popularity": 250, "trailer_youtube_id": "8U8Fk_Y9xWw", "trends_india_relative_index": 0.11
    },
    {
        "id": "paranoiaagent", "name": "Paranoia Agent", "india_fame_tier": "low",
        "vector": {"genre_one_hot": {"drama": 1, "mystery": 1, "suspense": 1, "psychological": 1}, "tag_weights": {"surreal": 0.9, "detective": 0.85, "social_commentary": 0.95}, "demographic_tag": "seinen"},
        "mal_score": 7.67, "anilist_popularity": 340, "trailer_youtube_id": "O_B69w_t35I", "trends_india_relative_index": 0.07
    }
]