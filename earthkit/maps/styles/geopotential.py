# Copyright 2023, European Centre for Medium Range Weather Forecasts.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from earthkit.maps import styles


GEOPOTENTIAL_IN_M2_PER_S2 = styles.Contour(
    line_colors="#33334d",
    linewidths=[0.5, 0.5, 0.5, 1],
    labels=True,
    level_step=800,
    units="m2 s-2",
    legend_type=None,
)


GEOPOTENTIAL_HEIGHT_IN_M = styles.Contour(
    line_colors="#33334d",
    linewidths=[0.5, 0.5, 0.5, 1],
    labels=True,
    level_step=50,
    units_orverride="m",
    conversion=lambda x: x/9.80665,
    legend_type=None,
)


GEOPOTENTIAL_HEIGHT_IN_DAM = styles.Contour(
    line_colors="#33334d",
    linewidths=[0.5, 0.5, 0.5, 1],
    labels=True,
    level_step=5,
    units_override="dam",
    conversion=lambda x: (x/9.80665)*0.1,
    legend_type=None,
)