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


class Vector3ArrayShould(unittest.TestCase):
    @staticmethod
    def test_canary():
        assert_that(2 + 2, equal_to(4))

    @staticmethod
    def test_str():
        sut = vmath.Vector3Array([[228953, 2327561, -2185], [241467, 2215499, -2476], [98506, 1035897, -1752]])

        assert_that(str(sut),
                    equal_to('[[ 2.289530e+05  2.327561e+06 -2.185000e+03]\n'
                             ' [ 2.414670e+05  2.215499e+06 -2.476000e+03]\n'
                             ' [ 9.850600e+04  1.035897e+06 -1.752000e+03]]'))

    @staticmethod
    def test_xyz():
        sut = vmath.Vector3Array([[228953, 2327561, -2185], [241467, 2215499, -2476], [98506, 1035897, -1752]])
        assert_that(np.array_equal(sut.x, [228953, 241467, 98506]))
        assert_that(np.array_equal(sut.y, [2327561, 2215499, 1035897]))
        assert_that(np.array_equal(sut.z, [-2185, -2476, -1752]))

    @staticmethod
    def test_length():
        sut = vmath.Vector3Array([[228953, 2327561, -2185], [241467, 2215499, -2476], [98506, 1035897, -1752]])
        expected_lengths = [np.sqrt((i ** 2).sum()) for i in sut]
        assert_that(np.array_equal(sut.length, expected_lengths))


if __name__ == '__main__':
    unittest.main()
