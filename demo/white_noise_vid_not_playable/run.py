import cv2
import gradio as gr
import numpy as np


def gif_maker():
    height, width = 50, 50
    img_array = [
        np.random.randint(0, 255, size=(height, width, 3)).astype(np.uint8)
        for _ in range(30)
    ]
    output_file = "test.mp4"
    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), 15, (height, width))
    for item in img_array:
        out.write(item)
    out.release()
    return output_file, output_file


demo = gr.Interface(gif_maker, inputs=None, outputs=[gr.Video(), gr.File()])

if __name__ == "__main__":
    demo.launch()