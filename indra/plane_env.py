"""
plane_env.py
An environment with a complex plane for agent's to move in.
"""

import math
import cmath
import random
import logging
import indra.spatial_env as se

X = 0
Y = 1


def rand_complex(initPos, radius):
    """
    Generates a random complex number
    uniformly picked from a disk of radius 'radius'.
    """
    radius = math.sqrt(radius * random.uniform(0.0, radius))
    theta = random.random() * 2 * math.pi
    return initPos + cmath.rect(radius, theta)


def pos_msg(agent, pos):
    """
    A convenience function for displaying
    an entity's position.
    """
    return("New position for " +
           agent.name + " is "
           + pos_to_str(pos))


def pos_to_str(pos):
    """
    Convert a complex position to a string rep.
    """
    return str(int(pos.real)) + " , " + str(int(pos.imag))


class PlaneEnv(se.SpatialEnv):
    """
    Extends SpatialEnv with entities located in the
    complex plane.
    """
    def __init__(self, name, width, height, preact=True,
                 postact=False, model_nm=None):

        super().__init__(name, width, height, preact=preact,
                         postact=postact, model_nm=model_nm)

    def add_agent(self, agent):
        """
        Add a spatial agent to env
        """
        super().add_agent(agent)
        self.position_agent(agent)

        v = agent.get_type()
        logging.debug("Adding " + agent.__str__()
                      + " of variety " + v)

    def position_agent(self, agent):
        x = random.uniform(0, self.width - 1)
        y = random.uniform(0, self.height - 1)
        agent.pos = complex(x, y)

    def closest_x(self, seeker, prehensions):
        """
        What is the closest entity of target_type?
        """
        pos = seeker.pos
        x = self.max_dist
        closest_target = None
        logging.debug("About to search for closest, among "
                      + str(len(prehensions)))
        for agent in prehensions:
            if seeker is not agent:  # don't locate me!
                if(seeker.exclude is None
                   or (agent not in seeker.exclude)):
                    p_pos = agent.pos
                    d = abs(pos - p_pos)
                    if d < x:
                        x = d
                        closest_target = agent
        logging.debug("Going to return closest = " + str(closest_target))
        return closest_target

    def get_new_wander_pos(self, agent):
        """
        If an agent is wandering in the env,
        this assigns it a new, random position
        based on its current position
        """
        new_pos = rand_complex(agent.pos, agent.max_move)
        x = new_pos.real
        y = new_pos.imag
        if x < 0.0:
            x = 0.0
        if y < 0.0:
            y = 0.0
        if x > self.width:
            x = self.width
        if y > self.height:
            y = self.height
        pos = complex(x, y)
        logging.debug(pos_msg(agent, pos))
        return pos

        return agent.get_pos()