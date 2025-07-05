import cv2
import os

def extract_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # No more frames

        # Save the frame as an image
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        print(f"Saved: {frame_filename}")
        frame_count += 1

    cap.release()
    print(f"Done! Extracted {frame_count} frames.")

# Example usage
video_path = r'D:\projects\drowsiness_detection\dataset\WIN_20250705_12_13_16_Pro.mp4'  # Change this to your video file path
output_folder = r'D:\projects\drowsiness_detection\dataset\images'  # Folder to save the images
extract_frames(video_path, output_folder)
