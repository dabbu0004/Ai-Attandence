import os
import subprocess
from datetime import datetime, timedelta
import random

# Start the history 45 days ago
current_date = datetime.now() - timedelta(days=10)

# Realistic commit messages tailored to your exact stack
commit_messages = [
    "Initialize Streamlit base layout and UI components",
    "Setup Supabase database connection and config",
    "Implement dlib face recognition pipeline",
    "Add voice embedding extraction",
    "Fix Streamlit dark mode CSS in base_layout.py",
    "Create student enrollment dialog and camera input",
    "Build teacher dashboard and analytics view",
    "Integrate Librosa for audio processing",
    "Update requirements.txt with scipy and face_recognition_models",
    "Refactor attendance logging logic"
]

print("Generating commit history...")

for i in range(35):  # Generates 35 commits
    msg = random.choice(commit_messages)
    # Randomize the time gap between 12 and 48 hours for realism
    current_date += timedelta(hours=random.randint(12, 48))
    
    git_date = current_date.strftime('%Y-%m-%dT%H:%M:%S')
    
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = git_date
    env['GIT_COMMITTER_DATE'] = git_date
    
    # --allow-empty creates the commit on the graph without needing file changes
    subprocess.run(['git', 'commit', '--allow-empty', '-m', msg], env=env)

print("Finished! Run 'git push' to update your GitHub graph.")