#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import newtesting 

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Design companies in chennai',
        'current_year': str(datetime.now().year)
    }
    newtesting().crew().kickoff(inputs=inputs)
    
run()
