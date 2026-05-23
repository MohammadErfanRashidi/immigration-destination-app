# Immigration Destination Finder

A data-driven Streamlit app to help Iranians find the best country to immigrate to, based on 20+ criteria such as safety, healthcare, job opportunities, presence of Iranian diaspora, and more.

## Demo
[Streamlit web-app](https://immigration-destination-app-cus2rp8driafthffvmtkk2.streamlit.app/)

## 📋 Project Overview

- **Goal:** Filter a curated list of countries using binary (Yes/No) and categorical preferences.
- **Data:** Manually collected from multiple sources (World Population Review, WEF, government reports, etc.) and enriched with continent, climate, religion, and race data.
- **App:** An interactive Streamlit dashboard where users select their priorities and instantly see matching countries.

## 📊 Data Sources

The dataset includes 24 binary categories (e.g., “Safest countries”, “Least racist”, “Best healthcare”, “Most Iranians”) and 5 categorical ones (English status, continent, climate, religion, race). All original source links are listed in the project notes.

## 🕹 How the App Works

- **Binary filters (e.g., “Safest”, “Most Iranians”)** – Choose `Yes` (country must have this trait), `No` (must not have it), or leave blank to ignore.
- **Categorical filters (Continent, Climate, Religion, Race, English status)** – Select one or more values to keep only those countries. If nothing is selected, the filter is ignored.
- **Dynamic table** – Only the columns you actively filter on are displayed, keeping the view clean.
- **Reset button** – Clears all filters and returns to the full list.

The filtering is conjunctive: a country must meet **all** active criteria to be shown.

## 📦 Requirements

- Python 3.8+
- streamlit
- pandas

## 📜 License

This project is for personal use. Data remains property of the original sources.
