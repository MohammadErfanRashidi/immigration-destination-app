'''
This app helps the user to filter the countries gathered in the dataset to find the countries
that can meet their criteria.
'''
# Libraries
import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('data/countries_dataset.csv')

df = load_data()

# Cat and bin cols
cat_cols = ['english_status', 'continent', 'climate', 'religion', 'race']
bin_cols = [
    col for col in df.columns
    if col not in ['country'] + cat_cols
    and df[col].dropna().isin([0, 1]).all()
]

# Reset mechanism
if 'reset' not in st.session_state:
    st.session_state.reset = False

if st.session_state.reset:
    for col in bin_cols:
        st.session_state[f'bin_{col}'] = ''
    for col in cat_cols:
        st.session_state[f'cat_{col}'] = []
    st.session_state.reset = False

# Sidebar
st.sidebar.header('Filter Countries')

# Binary filters
st.sidebar.subheader('Binary Criteria')
binary_choices = {}
for col in bin_cols:
    label = col.replace('_', ' ').title()
    choice = st.sidebar.selectbox(
        label,
        options = ['', 'Yes', 'No'],
        index = 0,
        key = f'bin_{col}'
    )
    binary_choices[col] = choice

# Categorical filters
st.sidebar.subheader('Categorical Criteria')
cat_filters = {}
for col in cat_cols:
    options = sorted(df[col].dropna().unique())
    selected = st.sidebar.multiselect(
        f"{col.replace('_', ' ').title()} (select)",
        options = options,
        default = [],
        key = f'cat_{col}'
    )
    if selected:
        cat_filters[col] = selected

# Reset button
if st.sidebar.button('Reset'):
    st.session_state.reset = True
    st.rerun()

# Apply filters
mask = pd.Series(True, index=df.index)

# Binary filters
for col, choice in binary_choices.items():
    if choice == 'Yes':
        mask &= (df[col] == 1)
    elif choice == 'No':
        mask &= (df[col] == 0)

# Categorical filters – THIS WAS MISSING
for col, selected_vals in cat_filters.items():
    mask &= df[col].isin(selected_vals)

filtered_df = df[mask]

# Display
active_display_cols = ['country']
for col in bin_cols:
    if binary_choices[col] != '':
        active_display_cols.append(col)

for col in cat_cols:
    if col in cat_filters:
        active_display_cols.append(col)

# Main page
st.title('Hello beautiful ;)')
if len(filtered_df) > 1:
    st.markdown(f'### I could find **{len(filtered_df)}** countries for you...')
elif len(filtered_df) == 1:
    st.markdown(f'### Oh! only one country could be found!')

if len(filtered_df) == 0:
    st.warning("I'm sorry, but I could not find any country that perfect :(")
else:
    st.dataframe(filtered_df[active_display_cols].reset_index(drop = True))