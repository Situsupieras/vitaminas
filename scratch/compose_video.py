from moviepy import ImageClip, AudioFileClip, VideoClip, CompositeVideoClip, ColorClip, concatenate_videoclips
import os

# Paths
avatar_path = r"C:\Users\PC\.gemini\antigravity\brain\d6a2a901-3811-45d7-9968-57b02d56dc59\marco_villagran_presenter_1778051760777.png"
audio_path = r"c:\proyectos\vitaminas\Magnesio citrato y glicinato\n8n_output\08_masterclass_section1_pro.mp3"
slides_dir = r"c:\proyectos\vitaminas\scratch\slides"
output_path = r"c:\proyectos\vitaminas\Magnesio citrato y glicinato\n8n_output\08_masterclass_section1_demo.mp4"

def compose():
    if not os.path.exists(audio_path):
        print(f"Audio not found at {audio_path}")
        return

    # 1. Load audio
    audio = AudioFileClip(audio_path)
    duration = audio.duration
    print(f"Audio duration: {duration} seconds")

    # 2. Background
    bg = ColorClip(size=(1920, 1080), color=(26, 26, 46)).with_duration(duration)

    # 3. Avatar
    if not os.path.exists(avatar_path):
        print(f"Avatar not found at {avatar_path}")
        return
    avatar = ImageClip(avatar_path).with_duration(duration)
    avatar = avatar.resized(height=1080)
    if avatar.w > 640:
        avatar = avatar.resized(width=640)
    
    avatar_x = (640 - avatar.w) // 2
    avatar = avatar.with_position((avatar_x, "center"))

    # 4. Slides
    slide_files = [os.path.join(slides_dir, f"slide{i}.png") for i in [1, 2, 3]]
    for sf in slide_files:
        if not os.path.exists(sf):
            print(f"Slide not found: {sf}")
            return

    slide_duration = duration / len(slide_files)
    slide_clips = []
    for sf in slide_files:
        sc = ImageClip(sf).with_duration(slide_duration).resized(width=1280)
        sc = sc.with_position((640, 0))
        slide_clips.append(sc)

    all_slides = concatenate_videoclips(slide_clips)

    # 5. Final Composition
    final_video = CompositeVideoClip([bg, avatar, all_slides])
    final_video = final_video.with_audio(audio)

    # 6. Render
    print("Starting render...")
    final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
    print("Render finished.")

if __name__ == "__main__":
    compose()
