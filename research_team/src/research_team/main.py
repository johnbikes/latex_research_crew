#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from research_team.crew import ResearchTeam

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Cat Detection in Images',
        'current_year': str(datetime.now().year)
    }
    
    try:
        ResearchTeam().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()