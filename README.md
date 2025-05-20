# AI Animation Video Generator

An advanced web application that generates educational and visualization videos using AI-powered code generation. Built with Streamlit, Groq API, and Manim animation library.

## 🌟 Features

- **AI-Powered Animation Creation**: Enter a prompt describing the animation you want to create
- **Advanced Code Generation**: Leverages Llama3.3 70B Versatile model via Groq API to generate Manim code
- **Educational Visualizations**: Perfect for creating educational content, algorithm visualizations, and technical explanations
- **Customizable Settings**: Control video quality, animation style, and LLM parameters
- **User-Friendly Interface**: Clean, intuitive UI built with Streamlit

## 🎬 How It Works

1. **User Input**: Describe the animation you want to create (e.g., "Show how a binary search algorithm works with 10 numbers")
2. **AI Code Generation**: The application sends your prompt to the Groq API with Llama3.3 70B to generate Manim code
3. **Rendering**: The generated code is executed to produce a high-quality MP4 animation
4. **Download**: Download the finished animation for use in presentations, education, or content

## 📋 Requirements

- Python 3.8+
- Groq API key
- Manim animation library and its dependencies
- FFmpeg for video rendering

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ai-animation-generator.git
   cd ai-animation-generator
   ```

2. Run the setup script to install all dependencies:
   ```bash
   python setup.py
   ```

3. Start the application:
   ```bash
   streamlit run main.py
   ```

## 🛠️ Manual Installation

If you prefer to install dependencies manually:

1. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Install Manim dependencies (system-specific):
   - **Ubuntu/Debian**:
     ```bash
     sudo apt-get update
     sudo apt-get install -y ffmpeg libcairo2-dev pkg-config python3-dev libpango1.0-dev
     ```
   - **macOS**:
     ```bash
     brew install ffmpeg cairo pkg-config pango
     ```
   - **Windows**: Follow the [Manim installation guide](https://docs.manim.community/en/stable/installation/windows.html)

## 🔑 API Key Setup

1. Create an account at [Groq Console](https://console.groq.com/)
2. Generate an API key
3. Enter your API key in the application's sidebar

## 🎨 Example Animations

Here are some example prompts you can try:

- **Computer Networking**:
  - "Create a scene where a browser on the left connects to a server in the middle, which then queries a database on the right. Show the data flow between these components with animated packets."

- **Data Structures & Algorithms**:
  - "Create an animation that demonstrates a binary search algorithm finding the number 42 in a sorted array of 15 numbers. Show each step with appropriate colors."
  - "Visualize a bubble sort algorithm with 10 random numbers."

- **Physics & Science**:
  - "Create an animation showing Earth's orbit around the Sun with proper physics and scales."
  - "Show how an electrical circuit works with a battery, resistor, and LED."

- **Mathematics**:
  - "Animate the transformation of a 2D coordinate system under different matrix operations."
  - "Visualize the Pythagorean theorem with animated squares on each side of a right triangle."

- **Machine Learning**:
  - "Create an educational animation showing forward propagation in a neural network with an input layer (3 neurons), one hidden layer (4 neurons), and an output layer (2 neurons)."



- **Generation Parameters**:
  - Temperature: Controls randomness in code generation
  
- **Animation Settings**:
  - Video Quality: low, medium, high
  - Animation Style: default, educational, technical, colorful



## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

