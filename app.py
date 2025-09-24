import streamlit as st
import pandas as pd

st.title("Excel File Comparator")

uploaded_files = st.file_uploader(
    "Upload Excel files", 
    type=["xlsx"], 
    accept_multiple_files=True
)

if uploaded_files and len(uploaded_files) > 1:
    dfs = []
    for file in uploaded_files:
        df = pd.read_excel(file)
        dfs.append(df)

    # Convert each df to set of tuples (rows)
    sets_of_rows = [set([tuple(row) for row in df.values]) for df in dfs]

    # Find same and different rows across all files
    same = set.intersection(*sets_of_rows)
    different = set.union(*sets_of_rows) - same

    st.subheader("Rows that are the SAME across all files")
    if same:
        st.write(pd.DataFrame(list(same)))
    else:
        st.info("No identical rows found across all files.")

    st.subheader("Rows that are DIFFERENT (appear in some, but not all files)")
    if different:
        st.write(pd.DataFrame(list(different)))
    else:
        st.info("No different rows found.")

else:
    st.info("Please upload at least two Excel files to compare.")
