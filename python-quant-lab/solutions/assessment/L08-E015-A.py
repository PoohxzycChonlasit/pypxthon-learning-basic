def final_paper_risk_assessment(entry, exit, quantity):
    return {'gross':(exit-entry)*quantity,'fee':(entry+exit)*quantity*.001,'net':(exit-entry)*quantity-(entry+exit)*quantity*.001,'live_trading':False}
