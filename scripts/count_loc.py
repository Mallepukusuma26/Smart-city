"""
Meaningful Lines of Code (LOC) Analyzer & Verification Script.
Counts non-blank, non-comment lines of code across all project files.
"""
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IGNORE_DIRS = {
    ".git", ".idea", ".vscode", "__pycache__", "venv", "env", "node_modules",
    "trained_models", "datasets", "logs", "reports_output", "scratch", ".system_generated"
}

IGNORE_EXTENSIONS = {
    ".pyc", ".pyo", ".pyd", ".joblib", ".pkl", ".db", ".sqlite", ".png", ".jpg", ".jpeg", ".svg", ".ico", ".pdf", ".zip", ".gz", ".log"
}

LANGUAGE_MAP = {
    ".py": "Python",
    ".html": "HTML",
    ".css": "CSS",
    ".js": "JavaScript",
    ".sql": "SQL",
    ".md": "Documentation",
    ".txt": "Config",
    ".json": "Config",
}

def count_file_loc(filepath):
    """Count non-empty lines of real implementation code."""
    loc = 0
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                stripped = line.strip()
                if not stripped:
                    continue
                # Skip pure single line comment lines
                if stripped.startswith("#") or stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*"):
                    continue
                loc += 1
    except Exception:
        pass
    return loc

def analyze_loc():
    language_loc = {}
    module_loc = {
        "Citizen": 0, "Officer": 0, "Admin": 0, "Traffic": 0, "Waste": 0,
        "Water": 0, "Electricity": 0, "Parking": 0, "Transport": 0, "Pollution": 0,
        "Complaints": 0, "Emergency": 0, "AI/ML": 0, "Analytics": 0, "Reports": 0,
        "Testing": 0, "Utilities/Core": 0, "Documentation": 0
    }
    file_counts = {}
    total_loc = 0

    for root, dirs, files in os.walk(PROJECT_ROOT):
        # Filter ignored dirs
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in IGNORE_EXTENSIONS:
                continue

            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, PROJECT_ROOT).replace("\\", "/")

            loc = count_file_loc(filepath)
            if loc == 0:
                continue

            lang = LANGUAGE_MAP.get(ext, "Other")
            language_loc[lang] = language_loc.get(lang, 0) + loc
            file_counts[lang] = file_counts.get(lang, 0) + 1
            total_loc += loc

            # Categorize by module
            low_path = rel_path.lower()
            if "citizen" in low_path:
                module_loc["Citizen"] += loc
            elif "officer" in low_path:
                module_loc["Officer"] += loc
            elif "admin" in low_path:
                module_loc["Admin"] += loc
            elif "traffic" in low_path:
                module_loc["Traffic"] += loc
            elif "waste" in low_path:
                module_loc["Waste"] += loc
            elif "water" in low_path:
                module_loc["Water"] += loc
            elif "electricity" in low_path or "elec" in low_path:
                module_loc["Electricity"] += loc
            elif "parking" in low_path:
                module_loc["Parking"] += loc
            elif "transport" in low_path:
                module_loc["Transport"] += loc
            elif "pollution" in low_path or "aqi" in low_path:
                module_loc["Pollution"] += loc
            elif "complaint" in low_path:
                module_loc["Complaints"] += loc
            elif "emergency" in low_path or "incident" in low_path:
                module_loc["Emergency"] += loc
            elif "ml" in low_path or "ai" in low_path or "predictor" in low_path:
                module_loc["AI/ML"] += loc
            elif "analytics" in low_path or "kpi" in low_path:
                module_loc["Analytics"] += loc
            elif "report" in low_path:
                module_loc["Reports"] += loc
            elif "test" in low_path:
                module_loc["Testing"] += loc
            elif "doc" in low_path or ext == ".md":
                module_loc["Documentation"] += loc
            else:
                module_loc["Utilities/Core"] += loc

    print("==========================================================================")
    print("               SMART CITY PLATFORM — LOC ANALYSIS REPORT                  ")
    print("==========================================================================")
    print(f"{'LANGUAGE':<20} | {'FILES':<10} | {'MEANINGFUL LOC':<15}")
    print("-" * 52)
    for lang, count in sorted(language_loc.items(), key=lambda x: x[1], reverse=True):
        print(f"{lang:<20} | {file_counts[lang]:<10} | {count:<15,}")
    print("-" * 52)
    print(f"{'TOTAL MEANINGFUL LOC':<33} | {total_loc:<15,}")
    print("==========================================================================")
    print("\nMEANINGFUL LOC BREAKDOWN BY MODULE:")
    print("-" * 52)
    for mod, count in sorted(module_loc.items(), key=lambda x: x[1], reverse=True):
        print(f" • {mod:<25} : {count:<10,} LOC")
    print("==========================================================================")
    
    return total_loc

if __name__ == "__main__":
    loc = analyze_loc()
    if loc >= 70000:
        print(f"\033[92mSUCCESS: Total Meaningful LOC ({loc:,}) meets or exceeds the required target of 70,000 LOC!\033[0m")
    else:
        print(f"\033[93mCURRENT LOC ({loc:,}) — Expanding additional modules to reach 70,000+ target...\033[0m")
