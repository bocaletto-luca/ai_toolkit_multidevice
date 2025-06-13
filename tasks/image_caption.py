# tasks/image_caption.py
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
_model     = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def caption_image(image_path: str) -> str:
    """Genera didascalia per l’immagine."""
    img = Image.open(image_path).convert("RGB")
    inputs = _processor(img, return_tensors="pt")
    out    = _model.generate(**inputs)
    return _processor.decode(out[0], skip_special_tokens=True)
