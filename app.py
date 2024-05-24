from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from streamlit_mic_recorder import mic_recorder , speech_to_text
os.environ["LANGCHAIN_API_KEY"]="ls__07168e984f3d4a2aba67d63ad1b8e0ea"
os.environ["LANGCHAIN_TRACING_V2"]="True"
os.environ["GOOGLE_API_KEY"]="AIzaSyCTeI7cYv_ix8wEgytqX9FsJ4coqkc0njw"

prompt=ChatPromptTemplate.from_messages(
    [
        ('system',''' your are an ai research agent well trained and having expertise in medical field of general purpose case sheet documentation helping my medical research purpose the patient gives his symptoms make a case sheet based on the data provided by him'''),
        ('user','''here is my data for you to read evaluate analyze and make a case sheet
          patient data: {cssheet}
         
         this is an example case sheet format you should generate 

         {{Case Sheet
Patient Information:

Patient Name: John Smith
Age/Date of Birth: 35 years old / 1989-01-25
Gender: Male
Medical Record Number: 123456
Presenting Complaint:

"Burning sensation when I urinate for the past 2 days."
History of Present Illness (HPI):

Onset: The burning sensation started 2 days ago in the morning.
Duration: It has been present constantly since then.
Character: The burning is a sharp, stinging sensation.
Location: The burning is felt during urination and at the tip of the penis.
Aggravating Factors: Urinating frequently seems to worsen the burning.
Alleviating Factors: Drinking more fluids seems to provide temporary relief.
Associated Symptoms: There is increased urinary frequency, but no fever, chills, or flank pain.
Past Medical History (PMH):

No significant past medical history.
Allergies: None known.
Medications: None currently.
Social History (SH):

Smokes cigarettes (1 pack per day for 10 years).
Drinks alcohol occasionally (2-3 drinks per week).
Denies any illicit drug use.
Drinks plenty of water throughout the day.
Works as a software engineer, sitting for most of the day.
Family History (FH):

No known family history of urinary tract infections (UTIs) or kidney stones.
Physical Examination (PE):

Vital Signs:
Blood pressure: 120/80 mmHg
Pulse: 80 beats per minute
Respiration: 16 breaths per minute
Temperature: 98.6°F (oral)
General: Appears well, not in acute distress.
Genitourinary: Genital exam reveals no external abnormalities.
Assessment/Impression:

Based on the presenting complaint, history, and physical examination findings, the most likely diagnosis is a urinary tract infection (UTI).
Plan:

Laboratory: Urinalysis and urine culture to confirm UTI and identify the causative organism.
Medication: Start ciprofloxacin 500mg twice daily for 7 days (empiric antibiotic treatment for UTI).
Patient Education: Drink plenty of fluids, urinate frequently, and complete the full course of antibiotics even if symptoms improve. Advised to return for a follow-up visit in 3-5 days to discuss lab results and adjust treatment as needed.}}
Note: This is a sample case sheet and the specific details may vary depending on the individual patient and their presentation.
         
         ''')

    ]

)


llm= ChatGoogleGenerativeAI(model='gemini-pro')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


st.title("Case Sheet Generator 🩺")

text = st.text_input('prompt the patient condition')

if text:
    st.write(chain.invoke({'cssheet':text}))