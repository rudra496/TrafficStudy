"""
TrafficStudy – Educational & Defensive Analysis Module

This module is STRICTLY EDUCATIONAL.
It does NOT generate network traffic.

Purpose:
- Explain traffic flood behavior
- Explain how defenses respond
- Help defenders and learners understand patterns
"""

from statistics import mean
from collections import Counter


# ===============================
# Traffic Pattern Analysis
# ===============================
def analyze_traffic(latencies, statuses):
    print("\n=== Traffic Behavior Analysis ===")

    if not latencies or not statuses:
        print("No data provided.")
        return

    print(f"Total events observed : {len(statuses)}")
    print(f"Average latency (ms)  : {round(mean(latencies), 2)}")
    print(f"Max latency (ms)      : {max(latencies)}")
    print(f"Min latency (ms)      : {min(latencies)}")

    status_count = Counter(statuses)
    print("\nHTTP Status Distribution:")
    for code, count in status_count.items():
        print(f"  {code} -> {count}")

    if 429 in status_count:
        print("\n• Rate limiting behavior detected (HTTP 429).")
    if 403 in status_count:
        print("• Blocking behavior detected (HTTP 403).")
    if 500 in status_count:
        print("• Possible backend saturation (HTTP 5xx).")


# ===============================
# Defensive Interpretation
# ===============================
def interpret_defense(statuses):
    print("\n=== Defensive Interpretation ===")

    if 429 in statuses:
        print("Likely Defense: Rate Limiter / API Gateway")
        print("Explanation   : Request rate exceeded configured thresholds.")

    if 403 in statuses:
        print("Likely Defense: WAF / Firewall")
        print("Explanation   : Security rules triggered by traffic pattern.")

    if 500 in statuses:
        print("Likely Issue  : Server overload or resource exhaustion.")

    if all(code == 200 for code in statuses):
        print("No visible defensive reaction detected.")


# ===============================
# Traffic Pattern Education
# ===============================
def explain_patterns():
    print("\n=== Common Traffic Patterns ===")
    print("• Burst  : Sudden spike, often triggers rate limiting quickly.")
    print("• Ramp   : Gradual increase, tests adaptive defenses.")
    print("• Steady : Constant pressure, exposes capacity limits.")


# ===============================
# Ethical Reminder
# ===============================
def ethical_warning():
    print("\n=== Ethical & Legal Warning ===")
    print("This project is for EDUCATION and DEFENSIVE RESEARCH only.")
    print("Run traffic-generation code ONLY on systems you own")
    print("or where you have explicit written permission.")
    print("Unauthorized use may be illegal.")


# ===============================
# Demo (Safe)
# ===============================
if __name__ == "__main__":
    demo_latencies = [120, 140, 160, 90, 95, 80]
    demo_statuses  = [200, 200, 200, 429, 429, 403]

    ethical_warning()
    explain_patterns()
    analyze_traffic(demo_latencies, demo_statuses)
    interpret_defense(demo_statuses)
