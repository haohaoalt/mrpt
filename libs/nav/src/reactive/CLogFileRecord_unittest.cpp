/* +------------------------------------------------------------------------+
   |                     Mobile Robot Programming Toolkit (MRPT)            |
   |                          https://www.mrpt.org/                         |
   |                                                                        |
   | Copyright (c) 2005-2019, Individual contributors, see AUTHORS file     |
   | See: https://www.mrpt.org/Authors - All rights reserved.               |
   | Released under BSD License. See: https://www.mrpt.org/License          |
   +------------------------------------------------------------------------+ */

#include <mrpt/io/CFileGZInputStream.h>
#include <mrpt/nav/reactive/CLogFileRecord.h>
#include <mrpt/system/filesystem.h>
#include <mrpt/serialization/CArchive.h>
#include <gtest/gtest.h>
#include <test_mrpt_common.h>

using namespace mrpt;
using namespace mrpt::nav;
using namespace mrpt::io;
using namespace mrpt::serialization;
using namespace std;

const mrpt::rtti::TRuntimeClassId* lstClasses[] = {
	CLASS_ID(CLogFileRecord),
};

// Create a set of classes, then serialize and deserialize to test possible
// bugs:
TEST(NavTests, Serialization_WriteReadToMem)
{
	for (auto& lstClasse : lstClasses)
	{
		try
		{
			CMemoryStream buf;
			auto arch = archiveFrom(buf);
			{
				auto* o =
					static_cast<CSerializable*>(lstClasse->createObject());
				arch << *o;
				delete o;
			}

			CSerializable::Ptr recons;
			buf.Seek(0);
			arch >> recons;
		}
		catch (const std::exception& e)
		{
			GTEST_FAIL() << "Exception during serialization test for class '"
						 << lstClasse->className << "':\n"
						 << e.what() << endl;
		}
	}
}

// Also try to convert them to octect vectors:
TEST(SerializeTestObs, WriteReadToOctectVectors)
{
	for (auto& lstClasse : lstClasses)
	{
		try
		{
			std::vector<uint8_t> buf;
			{
				auto* o =
					static_cast<CSerializable*>(lstClasse->createObject());
				mrpt::serialization::ObjectToOctetVector(o, buf);
				delete o;
			}

			CSerializable::Ptr recons;
			mrpt::serialization::OctetVectorToObject(buf, recons);
		}
		catch (const std::exception& e)
		{
			GTEST_FAIL() << "Exception during serialization test for class '"
						 << lstClasse->className << "':\n"
						 << e.what() << endl;
		}
	}
}

// Load test datalog
TEST(NavTests, NavLogLoadFromTestFile)
{
	const string navlog_file =
		UNITTEST_BASEDIR + string("/tests/serialize_test_data.reactivenavlog");
	if (!mrpt::system::fileExists(navlog_file))
	{
		cerr << "WARNING: Skipping test due to missing file: " << navlog_file
			 << "\n";
		return;
	}

	CFileGZInputStream f(navlog_file);
	auto arch = archiveFrom(f);

	try
	{
		for (int i = 0; i < 2; i++)
		{
			mrpt::nav::CLogFileRecord lfr;
			arch.ReadObject(&lfr);
		}
	}
	catch (const std::exception& e)
	{
		FAIL() << "Failed to parse stored navlog. Exception was:\n"
			   << e.what() << endl;
	}
}
