import streamlit as st
import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")


llm = ChatGroq(
    groq_api_key=api_key,
    model="openai/gpt-oss-120b",
    temperature=0.1,
)

prompt = PromptTemplate(
    input_variables=[
        "match_situation",
        "batsman",
        "bowler"
    ],

    template="""
You are a professional cricket commentator.

Generate exciting, natural and realistic cricket commentary.

Match Situation:
{match_situation}

Batsman:
{batsman}

Bowler:
{bowler}

REQUIREMENTS:

The commentary must naturally mention both the batsman and bowler. Carefully understand
the given match situation before generating the commentary. If there is a boundary,
describe the shot with excitement. If there is a six, make the moment powerful and
energetic. If there is a wicket, make the dismissal dramatic and highlight its
importance. If it is a dot ball, describe how the bowler has created pressure.

The commentary should have the feel of a professional Indian cricket commentator,
with an energetic, expressive and analytical delivery similar to the qualities often
associated with Akash Chopra's commentary: smart cricket observations, natural
Hindi-influenced expressions where appropriate, memorable cricket metaphors, and
enthusiasm during important moments. Do not imitate or reproduce his exact phrases,
catchphrases, or distinctive wording.

Use simple, fluent and easy-to-understand English. Add short cricket-related analysis
or observations when appropriate. Use creative cricket expressions and metaphors, but
keep them natural and avoid excessive repetition.

Do not invent any specific facts that are not provided. Do not change the batsman's or
bowler's name. Keep the commentary short, around 2 to 4 sentences. Make it sound like
live commentary happening at that exact moment.

Do not use bullet points, headings, explanations or additional information.

Return ONLY the cricket commentary.
"""
)

match_situation = st.text_input("Enter the match situation: ")
batsman = st.text_input("Enter the batsman's name: ")
bowler = st.text_input("Enter the bowler's name: ")

if st.button("Generate Commentary"):
    if not match_situation :
        st.error("Please fill in all the fields.")
    elif not batsman:
        st.error("Please enter batsman name ")
    elif not bowler:
        st.error("Please enter bowler name ")
    else:
        final_prompt = prompt.format(
            match_situation=match_situation,
            batsman=batsman,
            bowler=bowler
        )

        response = llm.invoke(final_prompt)
        st.write("Commentary:")
        st.write(response.content)
