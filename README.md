# 🎨 ColorReveal

Upload any image and instantly extract its dominant color palette. ColorReveal is a Flask-based web app that uses Python and JavaScript to analyze your image and reveal the colors that define it — perfect for designers, developers, or anyone who works with visuals.

---

## 🚀 Features

- Upload an image file and analyze its colors in seconds
- Preview the top color swatches extracted from the image
- Copy hex codes directly to clipboard with one click
- Responsive design for both desktop and mobile
- Built with a clean, minimal UI

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Pillow (PIL)
- **Frontend:** HTML5, CSS3, JavaScript
- **Tools:** Bootstrap, Flask-WTF

---


## 🧪 Local Setup

1. **Clone the repo**

```bash
git clone https://github.com/raygaither3/ColorReveal.git
cd ColorReveal


2. Create and activate a virtual environment

python -m venv .venv
source .venv/Scripts/activate    # On Windows (Git Bash)
# Or use: .venv\Scripts\activate  (CMD or PowerShell)

3. Install dependencies

pip install -r requirements.txt

4. Run the app

flask run



🔒 Security Notes
This app does not store uploaded images — all processing happens in-memory during the session.

📌 Coming Soon
Live deployment link (Render, Vercel, or Replit)

Optional image compression

Enhanced palette algorithm (cluster detection)

🙌 About the Creator
Ray Gaither – Self-taught Python developer and builder of real-world tools and full-stack apps. Connect with me on LinkedIn.


