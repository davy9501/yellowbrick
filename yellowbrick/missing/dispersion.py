# yellowbrick.missing.dispersion
# Missing Values Dispersion Visualizer
#
# Author:  Nathan Danielsen <nathan.danielsen@gmail.com>
# Created: Fri Mar 29 5:17:36 2018 -0500
#
# Copyright (C) 2018 District Data Labs
# For license information, see LICENSE.txt
#
# ID: dispersion.py [] nathan.danielsen@gmail.com.com $

##########################################################################
## Imports
##########################################################################

import numpy as np
import matplotlib.pyplot as plt

from .base import MissingDataVisualizer

# from yellowbrick.style.colors import resolve_colors

##########################################################################
## Feature Visualizer
##########################################################################

class MissingValuesDispersion(MissingDataVisualizer):
    """
    The Missing Values Dispersion visualizer shows the locations of missing (nan)
    values in the feature dataset.

    """

    def __init__(self, alpha=0.5, marker="|", **kwargs):
        """
        """

        super(MissingValuesDispersion, self).__init__(**kwargs)
        self.alpha = alpha
        self.marker = marker

    def get_nan_locs(self, **kwargs):
        """Gets the locations of nans in feature data and returns
        the coordinates in the matrix
        """

        nan_matrix = self.X.astype(float)
        return np.argwhere(np.isnan(nan_matrix))

    def draw(self, X, y, **kwargs):
        """Called from the fit method, this method creates a scatter plot that
        draws each instance as a class or target colored point, whose location
        is determined by the feature data set.
        """

        nan_locs = self.get_nan_locs()
        x, y = list(zip(*nan_locs))
        self.ax.scatter(x, y, alpha=self.alpha, marker=self.marker)

    def finalize(self, **kwargs):
        """
        Finalize executes any subclass-specific axes finalization steps.
        The user calls poof and poof calls finalize.

        Parameters
        ----------
        kwargs: generic keyword arguments.

        """
        # Set the title
        self.set_title(
            'Dispersion of Missing Values by Feature'
        )
        tick_locations = np.arange(len(self.features_))  # the x locations for the groups
        # Remove the ticks from the graph
        self.ax.set_xlabel('Count')
        self.ax.set_yticks(tick_locations)
        self.ax.set_yticklabels(self.features_)
        # Add the legend
        self.ax.legend(loc='best')