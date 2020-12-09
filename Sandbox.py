# MiPiEngine v1.0 licensed under the Apache license 2.0
# Created by Aaron Keith Sanders
# Project start date 11/08/2020
#
# NOTE: The vendors folder will contain all other third party modules that can be used for both free
# and commercial use. Some modules from these folders will have been copied and pasted into the main
# project folder, this is to make importing easier. The licenses for such modules can be found in their
# correct folder in the vendors folder and these folders will also contain all the other files associated
# with such modules. Not all third party modules are used/installed in such a way - i.e. pygame, only the
# ones in which the licenses for them are stored in the vendors folder.
#
# Third party modules: pygame, pygame_gui, pygame_functions

import MiPi


def main():
    # Window initialization
    MiPi.MiPi.EngineInit()
    MiPi.MiPi.Main()


if __name__ == '__main__':
    main()
