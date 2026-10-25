# Utility functions for AI Attendance processing

def scale_down_image(image, max_dim=1024):
    """Downscales PIL image to reduce memory usage during dlib inference"""
    img_w, img_h = image.size
    if max(img_w, img_h) > max_dim:
        ratio = max_dim / max(img_w, img_h)
        return image.resize((int(img_w * ratio), int(img_h * ratio)))
    return image

def validate_audio_length(audio_bytes, min_seconds=2.0):
    """Ensures recorded voice sample is long enough for a valid embedding"""
    import io
    import librosa
    try:
        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        return (len(audio) / sr) >= min_seconds
    except Exception:
        return False

