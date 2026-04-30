# ============================================================
#  Smart Cities & Future Transportation Quiz
#  Authors: Sujal & Bikas Poudel
#  Version: 1.0
# ============================================================

import time

# ---------- Question Bank ----------
QUESTIONS = [
    {
        "question": "What technology allows traffic lights to adjust timing based on real-time traffic flow?",
        "options": {
            "A": "Bluetooth Low Energy",
            "B": "Adaptive Traffic Signal Control (ATSC)",
            "C": "GPS triangulation",
            "D": "RFID tagging"
        },
        "answer": "B",
        "explanation": "ATSC systems use sensors and AI to dynamically adjust signal timing, reducing congestion."
    },
    {
        "question": "Which sensor technology do most autonomous vehicles use to create a 3D map of their surroundings?",
        "options": {
            "A": "Infrared cameras",
            "B": "Ultrasonic radar",
            "C": "LiDAR (Light Detection and Ranging)",
            "D": "Sonar"
        },
        "answer": "C",
        "explanation": "LiDAR fires laser pulses to measure distances and build precise 3D environmental maps."
    },
    {
        "question": "What does 'MaaS' stand for in smart city transportation?",
        "options": {
            "A": "Mobility as a Service",
            "B": "Management and Automation System",
            "C": "Multi-Access Autonomous System",
            "D": "Municipal Area Scheduling"
        },
        "answer": "A",
        "explanation": "MaaS integrates various transport services (bus, bike, rideshare) into a single digital platform."
    },
    {
        "question": "Which communication standard is most commonly used for Vehicle-to-Vehicle (V2V) communication?",
        "options": {
            "A": "Wi-Fi 6",
            "B": "DSRC (Dedicated Short-Range Communications)",
            "C": "Bluetooth 5.0",
            "D": "Zigbee"
        },
        "answer": "B",
        "explanation": "DSRC enables fast, low-latency communication between nearby vehicles for safety applications."
    },
    {
        "question": "What is the primary environmental benefit of electric public transit systems?",
        "options": {
            "A": "They are cheaper to build",
            "B": "They reduce greenhouse gas emissions",
            "C": "They require less maintenance",
            "D": "They travel faster than diesel buses"
        },
        "answer": "B",
        "explanation": "Electric transit eliminates direct emissions and, when powered by renewables, significantly cuts carbon output."
    },
    {
        "question": "In a smart city, what role does IoT (Internet of Things) play in transportation?",
        "options": {
            "A": "It replaces human drivers entirely",
            "B": "It connects physical infrastructure to collect and share real-time data",
            "C": "It only monitors parking spaces",
            "D": "It encrypts passenger data"
        },
        "answer": "B",
        "explanation": "IoT sensors embedded in roads, vehicles, and signals share data to optimize the entire transport network."
    },
    {
        "question": "Which city is widely recognized as a global pioneer in smart transportation and urban mobility?",
        "options": {
            "A": "Paris",
            "B": "Tokyo",
            "C": "Singapore",
            "D": "Chicago"
        },
        "answer": "C",
        "explanation": "Singapore's Smart Nation initiative integrates autonomous vehicles, real-time data, and digital transit planning."
    },
    {
        "question": "What is the purpose of a 'digital twin' in smart city transport planning?",
        "options": {
            "A": "A backup server for traffic data",
            "B": "A virtual replica of the transport system used for simulation and planning",
            "C": "A second autonomous vehicle for testing",
            "D": "A duplicate traffic signal system"
        },
        "answer": "B",
        "explanation": "Digital twins let planners simulate scenarios — like road closures or population growth — without real-world risk."
    },
    {
        "question": "What is 'congestion pricing' in the context of smart cities?",
        "options": {
            "A": "A fee charged for late public transit tickets",
            "B": "A dynamic toll system that charges drivers more during peak traffic hours",
            "C": "A penalty for autonomous vehicles exceeding speed limits",
            "D": "A subscription model for electric vehicles"
        },
        "answer": "B",
        "explanation": "Congestion pricing discourages driving during peak hours, reducing traffic and funding public transit improvements."
    },
    {
        "question": "Which of the following best describes a 'hyperloop' transportation system?",
        "options": {
            "A": "A high-speed monorail system above city streets",
            "B": "A network of underground electric buses",
            "C": "A pod system traveling through low-pressure tubes at near-supersonic speeds",
            "D": "A drone-based cargo delivery network"
        },
        "answer": "C",
        "explanation": "Hyperloop uses magnetic levitation and near-vacuum tubes to move pods at speeds exceeding 600 mph."
    },
]

# ---------- Helper Functions ----------

def print_banner():
    print("\n" + "=" * 60)
    print("   🚆  Smart Cities & Future Transportation Quiz  🚗")
    print("=" * 60)
    print("   Test your knowledge of the future of urban mobility!")
    print("   Authors: Sujal & Bikas")
    print("=" * 60 + "\n")


def print_question(index, question_data):
    print(f"\nQuestion {index + 1} of {len(QUESTIONS)}")
    print("-" * 50)
    print(f"  {question_data['question']}\n")
    for key, value in question_data["options"].items():
        print(f"    {key}) {value}")
    print()


def get_user_answer():
    while True:
        answer = input("  Your answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        print("  ⚠️  Invalid input. Please enter A, B, C, or D.")


def evaluate_answer(user_answer, question_data):
    correct = question_data["answer"]
    if user_answer == correct:
        print(f"\n  ✅ Correct! {question_data['explanation']}")
        return True
    else:
        print(f"\n  ❌ Wrong. The correct answer was {correct}.")
        print(f"     {question_data['explanation']}")
        return False


def print_results(score, total):
    percentage = (score / total) * 100
    print("\n" + "=" * 60)
    print(f"   📊 Quiz Complete! Your Score: {score}/{total} ({percentage:.0f}%)")
    print("=" * 60)

    if percentage == 100:
        print("   🏆 Perfect score! You're a Smart City expert!")
    elif percentage >= 80:
        print("   🌟 Great job! You have strong knowledge of future transport.")
    elif percentage >= 60:
        print("   👍 Good effort! Keep exploring smart city trends.")
    elif percentage >= 40:
        print("   📚 Not bad, but there's more to learn. Keep going!")
    else:
        print("   💡 Smart cities are complex — don't give up, keep learning!")

    print("=" * 60 + "\n")


# ---------- Main Quiz Logic ----------

def run_quiz():
    print_banner()
    input("  Press ENTER to start the quiz...\n")

    score = 0

    for i, question_data in enumerate(QUESTIONS):
        print_question(i, question_data)
        user_answer = get_user_answer()
        if evaluate_answer(user_answer, question_data):
            score += 1
        time.sleep(1)

    print_results(score, len(QUESTIONS))


# ---------- Entry Point ----------

if __name__ == "__main__":
    run_quiz()
