from cog import BasePredictor, Input
from khanomtan_tts import TTS

class Predictor(BasePredictor):
    def setup(self):
        """โหลดโมเดล KhanomTan TTS"""
        self.tts = TTS()

    def predict(self, text: str = Input(description="ข้อความที่ต้องการแปลงเป็นเสียง")) -> str:
        """แปลงข้อความเป็นเสียง"""
        output_path = "output.wav"
        self.tts.text_to_speech(text, output_path)
        return output_path
