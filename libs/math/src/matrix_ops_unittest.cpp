/* +------------------------------------------------------------------------+
   |                     Mobile Robot Programming Toolkit (MRPT)            |
   |                          https://www.mrpt.org/                         |
   |                                                                        |
   | Copyright (c) 2005-2019, Individual contributors, see AUTHORS file     |
   | See: https://www.mrpt.org/Authors - All rights reserved.               |
   | Released under BSD License. See: https://www.mrpt.org/License          |
   +------------------------------------------------------------------------+ */

// Note: Matrices unit tests have been split in different files since
// building them with eigen3 eats a lot of RAM and may be a problem while
// compiling in small systems.

#include <mrpt/math/CMatrixFixedNumeric.h>
#include <mrpt/math/CMatrixTemplateNumeric.h>
#include <mrpt/random.h>
#include <gtest/gtest.h>

using namespace mrpt;
using namespace mrpt::math;
using namespace mrpt::random;
using namespace std;

#define CHECK_AND_RET_ERROR(_COND_, _MSG_) EXPECT_FALSE(_COND_) << _MSG_;

TEST(Matrices, setSize)
{
	{
		CMatrixFixedNumeric<double, 6, 6> M;
		EXPECT_TRUE((M.array() == 0).all());
	}
	{
		CMatrixDouble M(5, 5);
		EXPECT_TRUE((M.array() == 0).all());
	}
	{
		CMatrixDouble M(5, 5);
		M.setSize(6, 5);
		EXPECT_TRUE((M.array() == 0).all());
	}
	{
		CMatrixDouble M(5, 5);
		M.setSize(10, 5);
		EXPECT_TRUE((M.array() == 0).all());
	}
	{
		CMatrixDouble M(5, 5);
		M.setSize(5, 6);
		EXPECT_TRUE((M.array() == 0).all());
	}
	{
		CMatrixDouble M(5, 5);
		M.setSize(6, 6);
		EXPECT_TRUE((M.array() == 0).all());
	}
	{
		CMatrixDouble M(5, 5);
		M.setSize(10, 10);
		EXPECT_TRUE((M.array() == 0).all());
	}
}

TEST(Matrices, extractSubmatrixSymmetricalBlocks)
{
	{
		const double vals[] = {
			1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15,
			1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15,
			1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15,
			1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15};
		const CMatrixFixedNumeric<double, 8, 8> M(vals);

		std::vector<size_t> vs;
		vs.push_back(1);
		vs.push_back(3);

		CMatrixDouble E;
		M.extractSubmatrixSymmetricalBlocks(2, vs, E);

		const double valsE[] = {3, 4, 7, 8, 10, 11, 14, 15,
								3, 4, 7, 8, 10, 11, 14, 15};
		const CMatrixDouble44 E_expected(valsE);

		EXPECT_TRUE(E_expected == E);
	}
}

TEST(Matrices, extractSubmatrixSymmetrical)
{
	{
		const double vals[] = {
			1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15,
			1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15,
			1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15,
			1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15};
		const CMatrixFixedNumeric<double, 8, 8> M(vals);

		std::vector<size_t> vs;
		vs.push_back(2);
		vs.push_back(3);
		vs.push_back(6);
		vs.push_back(7);

		CMatrixDouble E;
		M.extractSubmatrixSymmetrical(vs, E);

		const double valsE[] = {3, 4, 7, 8, 10, 11, 14, 15,
								3, 4, 7, 8, 10, 11, 14, 15};
		const CMatrixDouble44 E_expected(valsE);

		EXPECT_TRUE(E_expected == E);
	}
}
