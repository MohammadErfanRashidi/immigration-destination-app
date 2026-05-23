## Problem statement 

The goal of this project is to help choose the most optimum country to immigrate to as an Iranian.

---

## Data gathering

### English speaking countries 

- United Kingdom

- United States

- Canada

- Australia 

- New Zealand

- Ireland

### English as second language
https://www.weforum.org/stories/2019/11/countries-that-speak-english-as-a-second-language/

- Netherlands

- Denmark

- Sweden

- Norway

- Finland

- Luxembourg

- Austria

- Germany 

- Poland

- Belgium

- Switzerland 

- Portugal

- Singapore 

- Malaysia 

- Philippines

### Safest countries 2025 top 15
https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world

- Switzerland

- Norway

- Sweden

- Austria

- Denmark

- Canada 

- Finland

- New Zealand

- Australia 

- Belgium 

- Netherlands

- Ireland

- Iceland

- Luxembourg

- Portugal

### Least racist countries 2026 top 15
https://worldpopulationreview.com/country-rankings/least-racist-countries

- Denmark

- Finland

- New Zealand

- Netherlands

- Canada

- Belgium

- Sweden

- Norway

- Iceland

- Switzerland

- Austria

- Australia

- Ireland

- Luxembourg

- United Kingdom

### Best health care top 15
https://worldpopulationreview.com/country-rankings/best-healthcare-in-the-world

- Taiwan

- South Korea

- Australia 

- Canada

- Sweden

- Ireland

- Netherlands

- Germany

- Norway

- Israel

- Belgium

- Switzerland

- Japan

- Singapore 

- United States

### Wage vs. living cost top 15
https://www.gisma.com/blog/wage-vs-living-costs-in-the-eu-only-one-country-offers-a-livable-minimum-wage

- Belgium

- Netherlands

- France

- Germany

- Greece

- Spain

- Romania

- Luxembourg

- Ireland

- Poland

- Slovenia

- Lithuania 

- Bulgaria

- Latvia

- Hungry

### Countries with largest Iranians
https://en.wikipedia.org/wiki/Iranian_diaspora

- United States

- Kuwait

- United Arab Emirates 

- Germany

- Canada

- Israel 

- Bahrain

- Sweden

- Turkey

- France

- United Kingdom

- Iraq

- Saudi Arabia

- Australia 

- Netherlands

### 10 highest paying countries for psychologists
https://www.instarem.com/blog/highest-paying-countries-for-psychologists/

- United States

- Denmark

- Switzerland

- Canada

- Ireland

- Australia 

- Germany

- United Kingdom

- United Arab Emirates

- Netherlands

### Top education
https://worldpopulationreview.com/country-rankings/education-rankings-by-country

- South Korea

- Japan

- Belgium

- Slovenia

- Netherlands

- Germany

- Finland

- Norway

- Ireland

- Singapore

- France

- China

- Hong Kong

- Sweden

### Best immigrant policies
https://www.cgdev.org/blog/which-countries-have-best-migration-policies

- New Zealand

- Norway

- Australia

- Canada

- Sweden

- Germany

- Luxembourg

- South Korea

- Austria

- Spain

- Portugal

- Italy

- Belgium

- Netherlands

- Switzerland
 
### Top passports
https://www.visualcapitalist.com/ranked-most-powerful-passports-2026/

- Singapore

- Japan

- South Korea

- United Arab Emirates

- Norway

- Switzerland

- EU

- Malaysia

- United Kingdom

- Australia

- Canada

- New Zealand

- Liechtenstein 

- Iceland

- United States

### Most job opportunities
https://www.remitly.com/blog/en-gb/jobs-and-careers/global-job-market-opportunities/

- New Zealand

- Netherlands

- Iceland

- Australia

- Norway

- Switzerland

- Sweden

- Malta

- Denmark

- Ireland

### Migrant acceptance 
https://www.y-axis.com/blog/top-10-most-accepting-countries-for-migrants/

- Canada

- Iceland

- New Zealand

- Australia

- United States

- Sweden

- Ireland

### Best health care cost comparing to salary
https://radarhealthcare.com/news-blogs/healthcare-mapped-report/

- Luxembourg

- Iceland

- Norway

- Denmark

- Japan

- Netherlands

- New Zealand

- Sweden

- United Kingdom

- Germany

- France

- Israel

- Australia

- Finland

- Switzerland

### Lowest tolerance on drugs
https://people.howstuffworks.com/11-countries-that-impose-severely-harsh-drug-penalties.htm

- Sweden

- North Korea

- Japan

- Vietnam

- China

- Iran

- Singapore

- Malaysia

- Saudi Arabia

- Indonesia

- United Arab Emirates

### Most annual reading 
https://booketic.com/countries-by-reading-rate/

- Norway

- Sweden

- Finland

- Netherlands

- Japan

- United Kingdom

- Australia

- United States

- Canada

- Germany

- France

- South Korea

- Austria

- Switzerland

- Spain

### Best mental health care
https://www.theceomagazine.com/business/health-wellbeing/countries-with-the-best-mental-health-care/

- Sweden 

- Germany

- Finland

- France 

- Netherlands

- Italy

- Canada

- Norway

- Slovenia

- Australia

### Most psychologists per capita (more demand for psychology)
https://www.latinometrics.com/articles/argentina-has-the-most-psychologists-per-capita-2023-12-02-0

- Argentina

- Costa Rica

- Netherlands

- Guatemala

- Cuba

- United States

- Brazil

- Peru

- Greece

- Ecuador

### Healthiest 
https://worldpopulationreview.com/country-rankings/healthiest-countries

- Singapore

- Japan

- South Korea

- Taiwan

- China

- Israel

- Norway

- Iceland

- Sweden

- Switzerland

- Netherland

- Luxembourg

- Germany

- Hong Kong

- Germany

### Most prosperous 
https://www.visualcapitalist.com/ranked-the-worlds-most-prosperous-countries-in-2026/

- Norway

- Iceland

- Denmark

- Sweden

- Ireland

- Switzerland

- Belgium

- Finland

- Netherlands

- Slovenia

- Luxembourg

- Czechia

- Germany

- Australia

- New Zealand

### Best public transport
https://www.william-russell.com/blog/global-transport-index/

- France

- Sweden

- Hong Kong

- United States

- Norway

- Belgium

- United Kingdom

- Germany

- Argentina

- Spain

- Singapore

- Austria

- Australia

- Canada

### Cleanest 
https://worldpopulationreview.com/country-rankings/cleanest-countries-in-the-world

- Estonia

- Luxembourg

- Germany

- Finland

- United Kingdom

- Sweden

- Norway

- Austria

- Switzerland

- Denmark

- Greece

- France

- Netherlands

- Malta

- Belgium

### Pregnancy leave paid above 20 weeks
https://worldpopulationreview.com/country-rankings/maternity-leave-by-country

- Croatia

- United Kingdom

- Australia

- Ireland

- Norway

- Slovakia

- Bulgaria

- Czechia

- Poland

- Hungry

- Italy

### Best work life balance
https://remote.com/resources/research/global-life-work-balance-index

- New Zealand

- Ireland

- Belgium

- Germany

- Norway

- Denmark

- Canada

- Australia

- Finland

- Spain

- Netherlands

- Portugal

- United Kingdom

- Argentina

- Austria

### Countries above 40 percent tax
https://worldpopulationreview.com/country-rankings/highest-taxed-countries

- Finland

- Japan

- Denmark

- Austria

- Sweden

- Belgium

- Slovenia

- Netherlands

- Portugal

- Norway

- Spain

- Iceland

- China

- Germany

- United Kingdom

- France

- South Africa

- South Korea

- Australia

- Greece

- Italy

- Ireland

---

## Create the dataframe

We now create a dataframe with country names as rows
We will then add columns for each attribute and give a binary number if the country was present in that category

We will also add categorical columns that we do not have the data for yet like

- Climate

- Continent

- Religion

- Race

---

## Create the web app using streamlit

Our dataset is mostly binary, the user must be able to choose if they want the 1 in that filter for instance,
does the user want to live in a country where there are many Iranians? if yes they choose 1, if no they dont want Iranians to be there, they choose 0, or if they do not care whether there are Iranians or not, they they leave indifferent and the filter does not apply at all. 
