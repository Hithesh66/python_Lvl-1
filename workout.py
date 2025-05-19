from FPDF import FPDF
from datetime import datetime

# Create a PDF class with custom formatting
class WorkoutPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.set_text_color(255, 255, 255)
        self.set_fill_color(30, 144, 255)  # Dodger Blue
        self.cell(0, 10, "5-Day Bulking Workout Plan 💪", ln=True, align="C", fill=True)
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_text_color(255, 255, 255)
        self.set_fill_color(100, 149, 237)  # Cornflower Blue
        self.cell(0, 10, title, ln=True, fill=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 8, body)
        self.ln()

# Create PDF
pdf = WorkoutPDF()
pdf.add_page()

# Introduction
intro_text = (
    "Yo Hiteesh! 👊 Ready to bulk like a beast and flex like a legend?\n\n"
    "This plan blends bodyweight workouts with dumbbell magic (2–5 kg), built for your level. "
    "Train smart, eat big, and watch the gains roll in. Let’s turn those noodles into cannons 💥"
)
pdf.chapter_body(intro_text)

# Weekly Split Section
pdf.chapter_title("Weekly Workout Split 🗓️")
pdf.chapter_body(
    "- Monday: Push (Chest, Shoulders, Triceps)\n"
    "- Tuesday: Pull + Biceps\n"
    "- Wednesday: Legs + Glutes\n"
    "- Thursday: Core + Conditioning\n"
    "- Friday: Full Body Burn\n"
    "- Weekend: Chill & Recover 😎"
)

# Workout Plan Details
days = {
    "Monday – Push Day": [
        ("Elevated Push-Ups", "4 x 12–15", "Feet on a stool for upper chest"),
        ("Dumbbell Floor Press", "3 x 10–12", "Slow press, hold at top"),
        ("Pike Push-Ups", "3 x 10–15", "Shoulder strength"),
        ("Dumbbell Overhead Press", "3 x 10", "Control up/down"),
        ("Dumbbell Lateral Raise", "3 x 12–15", "Shoulder burn"),
        ("Chair Dips", "3 x 10–12", "Elbows back, go deep"),
        ("Overhead Tricep Extension", "3 x 12", "With 1 or 2 dumbbells")
    ],
    "Tuesday – Pull Day": [
        ("Table Rows", "4 x 10–12", "Use table or towel rows"),
        ("Superman Pulses", "3 x 15", "Lift chest + legs"),
        ("Bent Over Rows", "3 x 12", "Squeeze at top"),
        ("Rear Delt Raises", "3 x 15", "Hit upper back"),
        ("Hammer Curls", "3 x 12", "Forearms & biceps"),
        ("Concentration Curls", "3 x 10–12", "Isolate each side")
    ],
    "Wednesday – Legs & Glutes": [
        ("Bodyweight Squats", "4 x 15", "Slow and steady"),
        ("Goblet Squats", "3 x 12", "Dumbbell at chest"),
        ("Bulgarian Split Squats", "3 x 8/leg", "Rear foot on chair"),
        ("Dumbbell RDLs", "3 x 12", "Hinge, not squat"),
        ("Glute Bridges", "3 x 15", "Add DB for challenge"),
        ("Calf Raises", "4 x 20", "Squeeze hard")
    ],
    "Thursday – Core + Conditioning": [
        ("Plank to Push-Up", "3 x 10", "Core & shoulder combo"),
        ("Russian Twists", "3 x 20", "Twist with dumbbell"),
        ("Leg Raises", "3 x 12–15", "Controlled form"),
        ("Side Bends", "3 x 15/side", "Oblique focus"),
        ("Mountain Climbers", "3 x 30s", "Controlled speed"),
        ("Flutter Kicks", "3 x 20", "Keep core tight")
    ],
    "Friday – Full Body Burn": [
        ("Push-Up + Row", "4 x 10", "Push-up then row"),
        ("Squat to Press", "3 x 10", "Full body burn"),
        ("Step-Up + Knee Raise", "3 x 10/leg", "Use chair"),
        ("Curls to Press", "3 x 12", "Combo move"),
        ("Wall Sit Hold", "2 x 60s", "Add DB to spice it up"),
        ("Core Circuit", "3 Rounds", "Plank → Leg Raise → Twist")
    ]
}

# Add each day's workout
for day, exercises in days.items():
    pdf.chapter_title(day)
    for name, reps, note in exercises:
        pdf.set_font("Arial", "B", 11)
        pdf.set_text_color(0, 100, 0)  # Dark green for exercise
        pdf.cell(0, 8, f"{name} – {reps}", ln=True)
        pdf.set_font("Arial", "", 10)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 6, f"  ➤ {note}")
    pdf.ln(2)

# Motivation outro
pdf.chapter_title("Now go get those gains 🦾")
pdf.chapter_body(
    "This is your era, bro. Eat like a beast. Train with intent. Sleep like royalty.\n\n"
    "The only thing standing between you and those gains… is reps. LET’S GET IT! 🚀🔥"
)

# Save the PDF
pdf_path = "/mnt/data/Bulking_Workout_Plan_Hiteesh.pdf"
pdf.output(pdf_path)

pdf_path
