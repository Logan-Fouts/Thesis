
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import TextBox

final_tp, final_fp = 0, 0

def submit(fig, tp_box, fp_box):
    global final_tp, final_fp
    try:
        final_tp += int(tp_box.text)
        final_fp += int(fp_box.text)
        plt.close(fig)
    except ValueError:
        print("Invalid input.")

def classify_duplicates(directory):
    groups = [os.path.join(directory, name) for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

    for group_dir in groups:
        images = [os.path.join(group_dir, img) for img in os.listdir(group_dir) if img.endswith(('png', 'jpg', 'jpeg'))]
        fig, axs = plt.subplots(1, len(images), figsize=(15, 10))

        for ax, img_path in zip(axs, images):
            img = mpimg.imread(img_path)
            ax.imshow(img)
            ax.axis('off')  # Turn off axis
            ax.set_title(os.path.basename(img_path))
        
        plt.subplots_adjust(bottom=0.25)  # Adjust the bottom margin

        axbox_tp = plt.axes([0.1, 0.05, 0.1, 0.05])
        text_box_tp = TextBox(axbox_tp, 'Enter TP:', initial="")

        axbox_fp = plt.axes([0.3, 0.05, 0.1, 0.05])
        text_box_fp = TextBox(axbox_fp, 'Enter FP:', initial="")
        text_box_fp.on_submit(lambda text: submit(fig, text_box_tp, text_box_fp))

        plt.show()


base_dir = './classified_images/duplicates_directory'
classify_duplicates(base_dir)
print("Classification results for classified duplicates (TP) - (FP):", final_tp, "-", final_fp)

