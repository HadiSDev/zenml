#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
from custom_obj_file.custom_obj_file import SomeObj

from zenml.steps import BaseParameters, Output, step


class StepParams(BaseParameters):
    some_option: int = 4


@step
def some_step(params: StepParams) -> Output(output_1=SomeObj, output_2=int):
    return SomeObj("Custom-Object"), params.some_option
