# Utility functions for AI Attendance processing

def scale_down_image(image, max_dim=1024):
    """Downscales PIL image to reduce memory usage"""
    img_w, img_h = image.size
    if max(img_w, img_h) > max_dim:
        ratio = max_dim / max(img_w, img_h)
        return image.resize((int(img_w * ratio), int(img_h * ratio)))
    return image

def validate_audio_length(audio_bytes, min_seconds=2.0):
    """Ensures recorded voice sample is long enough"""
    import io, librosa
    try:
        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        return (len(audio) / sr) >= min_seconds
    except:
        return False

def hash_password(raw_password):
    """Hashes teacher passwords for secure storage"""
    import hashlib
    return hashlib.sha256(raw_password.encode('utf-8')).hexdigest()

def generate_attendance_csv(df):
    """Converts attendance DataFrame to downloadable CSV format"""
    if df.empty:
        return None
    return df.to_csv(index=False).encode('utf-8')

def init_app_state(st_session):
    """Initializes required Streamlit session variables"""
    defaults = {'is_logged_in': False, 'user_role': None, 'attendance_images': []}
    for key, val in defaults.items():
        if key not in st_session:
            st_session[key] = val

def handle_db_response(response):
    """Safely parses Supabase responses"""
    if hasattr(response, 'error') and response.error:
        print(f"Database Error: {response.error}")
        return None
    return response.data if hasattr(response, 'data') else response

def calculate_euclidean_distance(emb1, emb2):
    """Calculates distance between two face embeddings"""
    import numpy as np
    return np.linalg.norm(np.array(emb1) - np.array(emb2))

def apply_noise_gate(audio_signal, threshold=0.01):
    """Zeroes out audio samples below noise threshold"""
    import numpy as np
    return np.where(np.abs(audio_signal) < threshold, 0, audio_signal)

def ensure_rgb_format(image):
    """Ensures image is in RGB format for dlib processing"""
    if image.mode != 'RGB':
        return image.convert('RGB')
    return image

def get_current_academic_term():
    """Returns Fall, Spring, or Summer based on current date"""
    from datetime import datetime
    month = datetime.now().month
    if 8 <= month <= 12: return 'Fall'
    elif 1 <= month <= 5: return 'Spring'
    return 'Summer'

