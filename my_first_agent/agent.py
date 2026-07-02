from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    # OTHER agents read this to decide if they should delegate here
    description='A helpful assistant for user questions.',
    # THIS agent reads this to know how to behave
    instruction='Answer user questions to the best of your knowledge',
)
