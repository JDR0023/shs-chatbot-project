# Chat bot with streamlit UI/front end 
# To run, type in terminal: streamlit run app.py (run this instead if you want to use streamlit for front end. Run the skeletal framework if you want to use react/html-css-java/etc. as another front end)
# Don't forget to pip install streamlit and google-generativeai first! (pip install streamlit google-generativeai)

import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="SHS Chatbot", page_icon="🏫")
st.title("🏫 SHS Info Assistant")

# 1. Setup API 
genai.configure(api_key="YOUR_API_KEY_HERE")

# 2. Define the Brain (System Instruction)
school_info = """
You are a helpful assistant for University of Perpetual Help System DALTA Las Pinas Campus Senior High School. 
Answer questions based on these facts:
- The Principal is Ma'am Julie Reyes
- SHS strands: STEM, ABM, HUMSS, and ICT.
- About the school: The University of Perpetual Help System DALTA continuously subscribes to the institutional philosophy that national development and transformation is predicated upon the quality of education of its people. It is committed to the ideals of teaching, community service and research, with “Character Building is Nation Building” as its guiding principle.
- The slogan: Character Building is Nation Building
- Philosophy: The University of Perpetual Help System DALTA believes and invokes Divine Guidance in the betterment of the quality of life through national development and transformation, which are predicated upon the quality of education of its people. Towards this end, the Institution is committed to the ideals of teaching, community service and research as it nurtures the value of “Helpers of God”, with “Character Building is Nation Building” as its guiding principle.
- Vision: 

The University of Perpetual Help System DALTA shall emerge as a premier university in the Philippines. It shall provide a venue for the pursuit of excellence in academics, technology and research through local and international linkages.

The University shall take the role of a catalyst for human development. It shall inculcate Christian values and Catholic doctrine, as a way of strengthening the moral fiber of the Filipino, a people who are “Helpers of God”, proud of their race and prepared for the exemplary global participation in the sciences, arts, humanities, sports and business.

It foresees the Filipino people enjoying a quality of life in abundance, living in peace and building a nation that the next generation will nourish, cherish and value.

- Mission: 

The University of Perpetual Help System DALTA is dedicated to the development of the Filipino as a leader. It aims to graduate dynamic students who are physically, intellectually, socially and spiritually committed to the achievement of the highest quality of life. As a system of Service in health and in education, it is dedicated to the formation of Christ-centered, service-oriented and research-driven individuals with great social concern and commitment to the delivery of quality education and health care. It shall produce Perpetualites as “Helpers of God” – a vital ingredient to nation building.

- Core Values:
    1. Love of God, Love of Self, Family and Neighbor
    2. Love of Country and Good Governance
    3. Academic and Professional Excellence
    4. Health and Ecological Consciousness
    5. Peace and Global Solidarity
    6. Filipino Christian Leadership
    7. Value of Catholic Doctrine
    8. UPHSD and Perpetualite

- Attributes of a Perpetualite Graduate: 
    1. Character =     God fearing individuals, Helpers of God, Servant Leaders, Ethnically responsible digital citizens
    2. Competence =     Effective communicators, Critical and creative thinkers, Competent and excellent individuals (e.g. workforce, talent and professionals), Reflective lifelong learners, researches and innovators
    3. Commitment to Service =     Caring nation builders, Ecologically-conscious citizens and leaders, Committed and collaborative team players

- School Hymn:
    Perpetual Help thy fount of truth
    Where knowledge emanates;
    Where we have learned life will bear fruit
    For us success awaits;

    Thy children here we sing for thee;
    We raise our voices clear;
    We shout and cheer in unity
    For Alma Mater dear.

    Training the mind and the heart and the hand,
    Ready to serve as best as we can;
    Perpetual Help by thy banner we stand,
    Loyal and true spread thy fame o’er the land.

"""

# 3. Initialize the Model
@st.cache_resource
def load_model():
    return genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=school_info
    )

model = load_model()

# 4. Initialize Chat History for the UI
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.chat_session = model.start_chat(history=[])

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Chat Input
if prompt := st.chat_input("Ask something about our school..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send to Gemini and display response
    response = st.session_state.chat_session.send_message(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})