# Copyright (c) Microsoft Corporation
# All rights reserved.
#
# MIT License
#
# Permission is hereby granted, free of charge,
# to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os

REST_PORT = 51188

HOME_DIR = os.path.join(os.environ['HOME'], 'nni')

METADATA_DIR = os.path.join(HOME_DIR, 'nnictl')

METADATA_FULL_PATH = os.path.join(METADATA_DIR, 'metadata')

LOG_DIR = os.path.join(HOME_DIR, 'nnictl', 'log')

STDOUT_FULL_PATH = os.path.join(LOG_DIR, 'stdout')

STDERR_FULL_PATH = os.path.join(LOG_DIR, 'stderr')

ERROR_INFO = 'ERROR: %s'

NORMAL_INFO = 'INFO: %s'

WARNING_INFO = 'WARNING: %s'

EXPERIMENT_SUCCESS_INFO = '\033[1;32;32mSuccessfully started experiment!\n\033[0m' \
                          '-----------------------------------------------------------------------\n' \
                          'The experiment id is %s\n'\
                          'The restful server post is %s\n' \
                          'The Web UI urls are: %s\n' \
                          '-----------------------------------------------------------------------\n\n' \
                          'You can use these commands to get more information about the experiment\n' \
                          '-----------------------------------------------------------------------\n' \
                          '         commands                       description\n' \
                          '1. nnictl experiment show        show the information of experiments\n' \
                          '2. nnictl trial ls               list all of trial jobs\n' \
                          '3. nnictl log stderr             show stderr log content\n' \
                          '4. nnictl log stdout             show stdout log content\n' \
                          '5. nnictl stop                   stop a experiment\n' \
                          '6. nnictl trial kill             kill a trial job by id\n' \
                          '7. nnictl webui url              get the url of web ui\n' \
                          '8. nnictl --help                 get help information about nnictl\n' \
                          '-----------------------------------------------------------------------\n' \

PACKAGE_REQUIREMENTS = {
    'SMAC': 'smac_tuner'
}

COLOR_RED_FORMAT = '\033[1;31;31m%s\033[0m'

COLOR_GREEN_FORMAT = '\033[1;32;32m%s\033[0m'

COLOR_YELLOW_FORMAT = '\033[1;33;33m%s\033[0m'