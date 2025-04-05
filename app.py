import streamlit as st

st.title("My Streamlit App")
st.write("Hello, world!")

container = st.container()
with container:
      st.write("This is inside the container.")
      st.button("Click me!")
      st.text_input("Enter some text:")
      st.checkbox("Check me!")
      st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
      st.slider("Select a range:", 0, 100, (25, 75))
      st.radio("Pick one:", ["Choice A", "Choice B", "Choice C"])
      st.date_input("Select a date:")
      st.time_input("Select a time:")
      uploaded_files = st.file_uploader(
         "Choose a CSV file", accept_multiple_files=True
      )
      for uploaded_file in uploaded_files:
         bytes_data = uploaded_file.read()
         st.write("filename:", uploaded_file.name)
         st.write(bytes_data)
      st.color_picker("Pick a color:")
      st.markdown(
            ":orange-badge[⚠️ App might under maintenance]"
      )