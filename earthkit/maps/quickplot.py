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

from earthkit.maps import Chart

WORKFLOW = [
    "coastlines",
    "land",
    "borders",
    "gridlines",
]


def quickplot(data=None, **kwargs):
    chart = Chart(**kwargs)

    if data is not None:
        raise NotImplementedError

    for item in WORKFLOW:
        getattr(chart, item)()

    chart.show()
