import streamlit as st
import pandas as pd
from io import BytesIO

# Set the page title and layout
st.set_page_config(page_title="📁 File Converter & Cleaner by Hooria Khan", layout="wide")

# Title of the app
st.title("📁 File Converter & Cleaner by Hooria Khan")
st.write("Upload your CSV and Excel Files to clean the data and convert formats effortlessly 🚀")

# Instagram link
st.markdown("Follow me on [Instagram](https://www.instagram.com/hooria_codehub/) for more updates!")

# File uploader
files = st.file_uploader("Upload CSV or Excel Files", type=["csv", "xlsx"], accept_multiple_files=True)

if files:
    for file in files:
        ext = file.name.split(".")[-1]
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

        # Display file preview
        st.subheader(f"🔍 {file.name} - Preview")
        st.dataframe(df.head())

        # Checkbox to fill missing values
        if st.checkbox(f"Fill Missing Values - {file.name}"):
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            st.success("Missing values filled successfully!")
            st.dataframe(df.head())

        # Column selection
        selected_columns = st.multiselect(f"Select Columns - {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]
        st.dataframe(df.head())

        # Chart display option
        if st.checkbox(f"📊 Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        # Format choice for conversion
        format_choice = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        # Download button
        if st.button(f"⬇️ Download {file.name} as {format_choice}"):
            output = BytesIO()
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime = "text/csv"
                new_name = file.name.replace(ext, "csv")
            else:
                df.to_excel(output, index=False)
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = file.name.replace(ext, "xlsx")
            output.seek(0)
            st.download_button("⬇️ Download File", file_name=new_name, data=output, mime=mime)

        # Add a professional sticker at the end
        st.markdown("<br><hr><h5 style='text-align: center; color: #4CAF50;'>Designed with 💚 by Hooria Khan</h5>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #888;'>Stay connected on Instagram for more updates!</p>", unsafe_allow_html=True)
        
        st.success("Processing Completed! 🎉")

