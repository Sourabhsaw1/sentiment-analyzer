# ============================================================
# QSkill Internship - Task 1: Data Analysis with Pandas & Matplotlib
# Author  : Sourabh Saw
# GitHub  : https://github.com/Sourabhsaw1
# Dataset : Students Performance in Exams (Kaggle)
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np
import os

# ── Output folder for saving charts ──────────────────────────
os.makedirs("charts", exist_ok=True)

# Set a clean style
sns.set_theme(style="darkgrid", palette="muted")
plt.rcParams.update({"figure.dpi": 120, "figure.facecolor": "#1e1e2e"})

# ============================================================
# 1. LOAD DATA
# ============================================================
df = pd.read_csv("StudentsPerformance.csv")

print("=" * 60)
print("       STUDENTS PERFORMANCE - DATA ANALYSIS REPORT")
print("=" * 60)

print("\n📄 Dataset Shape:", df.shape)
print("\n📋 First 5 rows:")
print(df.head())

print("\n📊 Column Names:", df.columns.tolist())

# ── Rename columns for easier access ─────────────────────────
df.columns = [
    "gender", "race", "parent_edu", "lunch",
    "test_prep", "math", "reading", "writing"
]

# Add a 'total' and 'average' column
df["total"]   = df["math"] + df["reading"] + df["writing"]
df["average"] = (df["total"] / 3).round(2)

# ============================================================
# 2. BASIC STATISTICS
# ============================================================
print("\n" + "─" * 60)
print("📈 BASIC STATISTICS")
print("─" * 60)

print(f"\n  Math    - Mean: {df['math'].mean():.2f}  |  Max: {df['math'].max()}  |  Min: {df['math'].min()}")
print(f"  Reading - Mean: {df['reading'].mean():.2f}  |  Max: {df['reading'].max()}  |  Min: {df['reading'].min()}")
print(f"  Writing - Mean: {df['writing'].mean():.2f}  |  Max: {df['writing'].max()}  |  Min: {df['writing'].min()}")
print(f"  Average Score (overall): {df['average'].mean():.2f}")

print("\n  Gender Distribution:")
print(df["gender"].value_counts().to_string())

print("\n  Test Prep Completion:")
print(df["test_prep"].value_counts().to_string())

# ============================================================
# 3. BAR CHART — Average Scores by Gender
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor("#1e1e2e")
ax.set_facecolor("#2a2a3e")

gender_avg = df.groupby("gender")[["math", "reading", "writing"]].mean()
gender_avg.plot(kind="bar", ax=ax, color=["#89b4fa", "#a6e3a1", "#f38ba8"],
                edgecolor="white", linewidth=0.5)

ax.set_title("Average Scores by Gender", color="white", fontsize=14, fontweight="bold")
ax.set_xlabel("Gender", color="white")
ax.set_ylabel("Average Score", color="white")
ax.tick_params(colors="white")
ax.legend(["Math", "Reading", "Writing"], facecolor="#2a2a3e", labelcolor="white")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/01_bar_gender_scores.png")
plt.close()
print("\n✅ Chart saved: charts/01_bar_gender_scores.png")

# ============================================================
# 4. BAR CHART — Average Scores by Test Prep
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor("#1e1e2e")
ax.set_facecolor("#2a2a3e")

prep_avg = df.groupby("test_prep")[["math", "reading", "writing"]].mean()
prep_avg.plot(kind="bar", ax=ax, color=["#cba6f7", "#fab387", "#94e2d5"],
              edgecolor="white", linewidth=0.5)

ax.set_title("Impact of Test Preparation on Scores", color="white", fontsize=14, fontweight="bold")
ax.set_xlabel("Test Preparation", color="white")
ax.set_ylabel("Average Score", color="white")
ax.tick_params(colors="white")
ax.legend(["Math", "Reading", "Writing"], facecolor="#2a2a3e", labelcolor="white")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/02_bar_testprep_scores.png")
plt.close()
print("✅ Chart saved: charts/02_bar_testprep_scores.png")

# ============================================================
# 5. SCATTER PLOT — Math vs Reading
# ============================================================
fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor("#1e1e2e")
ax.set_facecolor("#2a2a3e")

colors = {"male": "#89b4fa", "female": "#f38ba8"}
for gender, grp in df.groupby("gender"):
    ax.scatter(grp["math"], grp["reading"], alpha=0.6,
               color=colors[gender], label=gender, edgecolors="none", s=40)

ax.set_title("Math Score vs Reading Score", color="white", fontsize=14, fontweight="bold")
ax.set_xlabel("Math Score", color="white")
ax.set_ylabel("Reading Score", color="white")
ax.tick_params(colors="white")
ax.legend(facecolor="#2a2a3e", labelcolor="white")

# Trend line
z = np.polyfit(df["math"], df["reading"], 1)
p = np.poly1d(z)
x_line = np.linspace(df["math"].min(), df["math"].max(), 200)
ax.plot(x_line, p(x_line), color="yellow", linewidth=1.5, linestyle="--", label="Trend")
ax.legend(facecolor="#2a2a3e", labelcolor="white")

plt.tight_layout()
plt.savefig("charts/03_scatter_math_reading.png")
plt.close()
print("✅ Chart saved: charts/03_scatter_math_reading.png")

# ============================================================
# 6. HEATMAP — Correlation Matrix
# ============================================================
fig, ax = plt.subplots(figsize=(7, 5))
fig.patch.set_facecolor("#1e1e2e")
ax.set_facecolor("#2a2a3e")

corr = df[["math", "reading", "writing", "total", "average"]].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            linewidths=0.5, ax=ax,
            annot_kws={"color": "white", "size": 10})

ax.set_title("Correlation Heatmap of Scores", color="white", fontsize=14, fontweight="bold")
ax.tick_params(colors="white")
plt.tight_layout()
plt.savefig("charts/04_heatmap_correlation.png")
plt.close()
print("✅ Chart saved: charts/04_heatmap_correlation.png")

# ============================================================
# 7. SCATTER PLOT — Writing vs Reading
# ============================================================
fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor("#1e1e2e")
ax.set_facecolor("#2a2a3e")

lunch_colors = {"standard": "#a6e3a1", "free/reduced": "#fab387"}
for lunch_type, grp in df.groupby("lunch"):
    ax.scatter(grp["writing"], grp["reading"], alpha=0.5,
               color=lunch_colors[lunch_type], label=lunch_type, s=40)

ax.set_title("Writing Score vs Reading Score (by Lunch Type)", color="white", fontsize=14, fontweight="bold")
ax.set_xlabel("Writing Score", color="white")
ax.set_ylabel("Reading Score", color="white")
ax.tick_params(colors="white")
ax.legend(title="Lunch", facecolor="#2a2a3e", labelcolor="white", title_fontsize=9)
plt.tight_layout()
plt.savefig("charts/05_scatter_writing_reading.png")
plt.close()
print("✅ Chart saved: charts/05_scatter_writing_reading.png")

# ============================================================
# 8. BAR CHART — Average Score by Parental Education
# ============================================================
fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor("#1e1e2e")
ax.set_facecolor("#2a2a3e")

edu_avg = df.groupby("parent_edu")["average"].mean().sort_values(ascending=False)
bars = ax.bar(edu_avg.index, edu_avg.values, color="#cba6f7", edgecolor="white", linewidth=0.5)

ax.set_title("Average Score by Parental Education Level", color="white", fontsize=13, fontweight="bold")
ax.set_xlabel("Parental Education", color="white")
ax.set_ylabel("Average Score", color="white")
ax.tick_params(colors="white")
plt.xticks(rotation=20, ha="right", color="white")

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
            f"{bar.get_height():.1f}", ha="center", color="white", fontsize=9)

plt.tight_layout()
plt.savefig("charts/06_bar_parent_edu.png")
plt.close()
print("✅ Chart saved: charts/06_bar_parent_edu.png")

# ============================================================
# 9. INSIGHTS SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("🔍 KEY INSIGHTS & OBSERVATIONS")
print("=" * 60)

completed = df[df["test_prep"] == "completed"]["average"].mean()
none_prep  = df[df["test_prep"] == "none"]["average"].mean()
print(f"\n1. Test Prep Impact:")
print(f"   Students who completed test prep scored {completed:.2f} on average")
print(f"   vs {none_prep:.2f} for those who didn't — a {completed - none_prep:.2f} point difference!")

std_lunch = df[df["lunch"] == "standard"]["average"].mean()
red_lunch = df[df["lunch"] == "free/reduced"]["average"].mean()
print(f"\n2. Lunch Type Matters:")
print(f"   Standard lunch students: {std_lunch:.2f} avg")
print(f"   Free/reduced lunch students: {red_lunch:.2f} avg")
print(f"   Difference: {std_lunch - red_lunch:.2f} points (socioeconomic factor!)")

print(f"\n3. Correlation:")
print(f"   Reading & Writing are highly correlated ({corr['reading']['writing']:.2f})")
print(f"   Math & Reading: {corr['math']['reading']:.2f}")

top_edu = edu_avg.index[0]
print(f"\n4. Parental Education:")
print(f"   Students with parents having '{top_edu}' scored highest on average ({edu_avg.iloc[0]:.2f})")

print("\n" + "=" * 60)
print("✅ Analysis Complete! Check 'charts/' folder for all visualizations.")
print("=" * 60)
