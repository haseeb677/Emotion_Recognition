import datetime

# Log a detected emotion (dummy logic for now)
def log_emotion(emotion, timestamp=None):
    if timestamp is None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Emotion Detected: {emotion}")

# Initialize the "database" (placeholder)
def init_db():
    print("Database initialized (placeholder).")

# Fetch logs (dummy logs for now)
def fetch_logs(limit=10):
    # Simulated log entries
    all_logs = [
        {"timestamp": "2025-07-10 20:30:00", "emotion": "happy"},
        {"timestamp": "2025-07-10 20:35:00", "emotion": "sad"},
        {"timestamp": "2025-07-10 20:40:00", "emotion": "neutral"},
        {"timestamp": "2025-07-10 20:45:00", "emotion": "angry"},
        {"timestamp": "2025-07-10 20:50:00", "emotion": "surprised"},
        # ... add more if needed
    ]

    return all_logs[:limit]
