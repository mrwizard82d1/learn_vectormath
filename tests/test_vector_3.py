#
# This file is part of IMAGEFrac (R) and related technologies.
#
# Copyright (c) 2017-2020 Reveal Energy Services.  All Rights Reserved.
#
# LEGAL NOTICE:
# IMAGEFrac contains trade secrets and otherwise confidential information
# owned by Reveal Energy Services. Access to and use of this information is
# strictly limited and controlled by the Company. This file may not be copied,
# distributed, or otherwise disclosed outside of the Company's facilities
# except under appropriate precautions to maintain the confidentiality hereof,
# and may not be used in any way not expressly authorized by the Company.
#

import unittest

from hamcrest import assert_that, equal_to
import numpy as np
import vectormath as vmath


class Vector3DShould(unittest.TestCase):
    @staticmethod
    def test_canary():
        assert_that(2 + 2, equal_to(4))

    @staticmethod
    def test_vector3d_as_string_is_correct():
        sut = vmath.Vector3(423747, 8142822, -8602)

        assert_that(str(sut), equal_to('[ 423747. 8142822.   -8602.]'))

    @staticmethod
    def test_vector3d_xyz_are_correct():
        sut = vmath.Vector3(423747, 8142822, -8602)

        assert_that(sut.x, equal_to(423747))
        assert_that(sut.y, equal_to(8142822))
        assert_that(sut.z, equal_to(-8602))


if __name__ == '__main__':
    unittest.main()
