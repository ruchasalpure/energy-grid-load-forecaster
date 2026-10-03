from crewai import Agent

energy_grid_load_forecaster = Agent(
    role="Energy Grid Load Forecaster",
    goal="Deliver high-precision autonomous Energy Grid Load Forecaster operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
