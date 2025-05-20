import os
import subprocess
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"

# Initialize GROQ client
client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(page_title="AI Video Generator", layout="wide")
st.title("🎥 AI-driven Educational Video Generator")

st.markdown(
    "Provide a prompt describing the animation or visualization you want. "
    "The AI will generate Manim code, compile it, and produce an MP4 video."
)

# User prompt
title = st.text_input("Video Title (for filename)")
prompt = st.text_area(
    "Describe your scene, e.g. 'Show a browser on left, server in middle, database on right, with arrows.'",
    height=150
)
show_code = st.checkbox("Show generated Manim code")

if st.button("Generate Video"):
    if not prompt.strip():
        st.error("Please enter a prompt.")
    else:
        with st.spinner("Generating Manim script from LLM..."):
            # Use chat completions with explicit messages
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": 
                        "You are an expert at writing Python scripts using the Manim animation library."
                    },
                    {"role": "user", "content": 
                        f"Generate only the complete, self-contained Manim scene as Python code in a single .py file, "
                        f"with no markdown fences or extra text before or after. Scene prompt: {prompt}"
                    }
                ],
                max_tokens=2048,
                temperature=0.3
            )
            code = response.choices[0].message.content.strip()

            # Strip any stray Markdown fences (```)
            lines = code.splitlines()
            if lines and lines[0].startswith("```") or lines[-1].startswith("```"):
                code = "\n".join(lines[1:-1]).strip()

        if show_code:
            st.subheader("Generated Manim Code")
            st.code(code, language="python")

        # Save code to file
        filename = f"manim_script_{title.replace(' ', '_') or 'scene'}.py"
        with open(filename, "w") as f:
            f.write(code)

        with st.spinner("Rendering video with Manim (quick low-res)..."):
            try:
                subprocess.run(["manim", filename, "-ql"], check=True)

                # Locate MP4 output
                out_dir = os.path.join(
                    "media", "videos", os.path.splitext(filename)[0], "480p15"
                )
                mp4_files = [f for f in os.listdir(out_dir) if f.endswith(".mp4")]
                if mp4_files:
                    video_path = os.path.join(out_dir, mp4_files[0])
                    st.success("Video generated successfully!")
                    st.video(video_path)
                else:
                    st.error("No MP4 video found in output directory.")
            except subprocess.CalledProcessError as e:
                st.error(f"Manim rendering failed (code {e.returncode}).")
                if getattr(e, 'stdout', None):
                    st.text(e.stdout)
                if getattr(e, 'stderr', None):
                    st.text(e.stderr)

# Footer
st.markdown("---")
st.caption("Powered by Manim, Streamlit, and Groq LLM")
