#!/usr/bin/env python3
"""
A script to test our grid capabilities.
"""

import indra.utils as utils
import indra.prop_args as props
import indra.grid_env as ge
import grid_model as gm

# set up some file names:
MODEL_NM = "grid_model"
(prog_file, log_file, prop_file, results_file) = utils.gen_file_names(MODEL_NM)

# We store basic parameters in a "property" file; this allows us to save
#  multiple parameter sets, which is important in simulation work.
#  We can read these in from file or set them here.
pa = utils.read_props(MODEL_NM)
if pa is None:
    pa = props.PropArgs(MODEL_NM, logfile=log_file, props=None)
    pa.set("model", MODEL_NM)
    pa.ask("num_agents", "How many agents?", int, default=8,
           limits=utils.AGENT_LIMITS)
    pa.ask("grid_width", "What is the grid width?", int, default=6,
           limits=utils.GRID_LIMITS)
    pa.ask("grid_height", "What is the grid height?", int, default=6,
           limits=utils.GRID_LIMITS)

# Now we create a minimal environment for our agents to act within:
env = ge.GridEnv("Test grid env",
                 pa.get("grid_height"),
                 pa.get("grid_width"),
                 torus=False,
                 model_nm=MODEL_NM,
                 preact=True,
                 postact=True)

# Now we loop creating multiple agents with numbered names
# based on the loop variable:
for i in range(pa.get("num_agents")):
    env.add_agent(gm.TestGridAgent(name="agent" + str(i),
                  goal="taking up a grid space!"))

# let's test our iterator
for cell in env:
    (x, y) = cell.coords
    print("Contents of cell x = " + str(x)
          + " and y = " + str(y)
          + " is " + str(cell.contents))

utils.run_model(env, prog_file, results_file)
