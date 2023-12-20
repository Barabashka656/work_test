import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def create_ticker(text, output_video_path):
    duration = 3
    fps = 60
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = 32
    frame_width = 100
    frame_height = 100

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(
        output_video_path,
        fourcc,
        fps,
        (frame_width, frame_height)
    )

    y = frame_height - ((frame_height + font_size) // 2)
    frame_count = int(duration * fps)
    for i in range(frame_count):
        image = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(image)

        font = ImageFont.truetype("fonts/ARIAL.TTF", font_size)
        draw = ImageDraw.Draw(pil_image)
        text_width = draw.textlength(text, font=font)

        x = frame_width - (text_width + frame_width) * (i / frame_count)
        draw.text((int(x), y), text, font=font)

        image = np.asarray(pil_image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        out.write(image)

    out.release()


if __name__ == "__main__":
    text = input("input text\n")
    video_path = f"{text}.mp4"
    create_ticker(text, video_path)
    print("Done")
