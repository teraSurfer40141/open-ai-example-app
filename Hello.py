# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import requests

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="LimeWire",
        page_icon="✨",
    )
    st.title("Generate your own image!")

    col1,col2 = st.columns([3,5])
    image_style = col2.selectbox('Choose your painting style',["A photo of", "An oil painting of"])
    animal = col2.selectbox('Choose your animal',["fuzzy panda","british shorthair cat","Persian Cat","Shiba Inu Dog","racoon"])
    hat = col2.selectbox("Choose your hat",["wearing a fedora and","wearing a cowboy hat and","wearing a motorcycle helmet and"])
    outfit = col2.selectbox("Choose your outfit",["red shirt","black leather jacket"])
    activity = col2.selectbox("Choose an activity",["playing a guitar","skateboarding","riding a bike"])
    location = col2.selectbox("Choose a location",["on a beach","in a garden","on top of a mountain"])
    prompt = image_style + animal + hat + outfit + activity + location
    image_button = st.button("Generate image!")

    if image_button:
        with col1:
          with st.spinner("Loading..."):
              url = "https://api.limewire.com/api/image/generation"

              payload = {
              "prompt": prompt,
              "aspect_ratio": "1:1"
              }

              headers = {
              "Content-Type": "application/json",
              "X-Api-Version": "v1",
              "Accept": "application/json",
              "Authorization": "Bearer " + st.secrets["LIMEWIRE_KEY"]
              }

              response = requests.post(url, json=payload, headers=headers)
              data = response.json()
              image_url = data["data"][0]["asset_url"]
              st.image(image_url,caption="Generated by LimeWire")

if __name__ == "__main__":
    run()
