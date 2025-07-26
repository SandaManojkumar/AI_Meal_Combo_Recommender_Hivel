# AI Meal Combo Recommender


## 🚀 Live Demo

Explore the app here: **[https://ai-meal-combo-recommender.streamlit.app/](https://ai-meal-combo-recommender.streamlit.app/)**

---

## 🛠️ Features

- **User Preferences Input**: Choose dietary goals, meal types, or ingredients.
- **AI Combo Suggestions**: Recommends balanced combos based on input.
- **Hive-Powered Backend**: Processes food metadata for intelligent matching.
- **Interactive Streamlit Interface**: Friendly and intuitive front-end.

---

## 📚 Architecture Overview

- **Recommendation Engine**: Applies similarity-based logic (e.g. content‑based filtering) to propose meal combinations that enhance nutrition and balance.
- **Frontend (Streamlit)**: Captures user input and visualizes meal combo results in real time.

---

## 🧩 Tech Stack

| Component        | Technology             |
|------------------|------------------------|
| Recommendation   | Python ML |
| Web UI           | Streamlit              |
| Hosting          | Streamlit Cloud        |

---

## 🏃‍♀️ Getting Started (Local)

> Run the project on your local machine

```bash
git clone https://github.com/SandaManojkumar/AI_Meal_Combo_Recommender_Hive.git

cd AI_Meal_Combo_Recommender_Hive


pip install -r requirements.txt

streamlit run app.py
```

---

## 🧠 How It Works

1. **User Input** collected via Streamlit interface.
2. **Fetch Data**: App reads meal entries from Hive.
3. **Generate Recommendations**: Matches combos that align with nutrition, cuisine, and preference criteria.
4. **Display Output**: Shows suggested combos with details like nutrition breakdown, potential allergens, and ingredient list.

---

## ✅ Success Metrics

- User satisfaction per combo feedback
- Balance of macronutrients (calorie, protein, carbs, fats)
- Diversity in ingredients and cuisines

---

## 🎯 Use Cases

- Personal diet planning (e.g., vegetarian, keto, protein-focused)
- Meal suggestions for events or paired dishes
- Culinary creativity—discover interesting dish combinations

---

## 📂 Directory Structure

```

├── AI_Menu_Items1.csv  
├── combo.py     
├── api.py
├── requirements.txt
└── README.md
```

---

## 🧾 Adding New Meal Items

1. Append or upload new meal metadata to the Hive table (e.g., name, ingredients, nutrition values).
2. Re-run ingestion scripts in `data/` if applicable.
3. Restart app to reflect updates in recommendations.

---

## 📌 Contributions & Feedback

Contributions welcome! Please open an issue or submit a pull request with enhancements, bug fixes, or new features like:

- Personalized user profiles
- Dietary restrictions (allergens, low sodium, gluten-free)
- Multi-cuisine combo support
- Nutritional charts and visualizations

---

## 📬 Contact

Feel free to reach out to collaborate or connect!

- 💼 LinkedIn: [Manojkumar Sanda](https://www.linkedin.com/in/manojkumar-sanda-767025213/)
- 🌐 Portfolio: [manojkumarsanda.netlify.app](https://manojkumarsanda.netlify.app/)



---

Enjoy discovering delicious, balanced meal combos—powered by AI and Hive 🥗
